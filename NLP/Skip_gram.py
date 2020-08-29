import torch
import torch.utils.data as Data
from torch import nn
import numpy as np
import os
import collections
import math
import random
import sys
import time

# 读取数据
dataset_dir='E:\Sourcecode\Dive-into-DL-PyTorch-master\data\ptb'
with open(os.path.join(dataset_dir,'ptb.train.txt'),'r') as f:
    lines=f.readlines()
    raw_dataset=[st.strip().split(' ') for st in lines]
print('# sentenses:%d' % len(raw_dataset))
for st in raw_dataset[:3]:
    print("# token %d " % len(st),st[:5])

# 为了计算简单，我们只保留在数据集中至少出现5次的词。
counter=collections.Counter([tk for st in raw_dataset for tk in st])
counter=dict(filter(lambda x:x[1]>=5,counter.items()))

# 然后将词映射到整数索引。
idx_to_token=[tk for tk,_ in counter.items()]
token_to_idx={tk:idx for idx,tk in enumerate(idx_to_token)}
dataset=[[token_to_idx[tk] for tk in st if tk in token_to_idx] for st in raw_dataset]
num_tokens=sum([len(st) for st in dataset])
print('# tokens: %d' % num_tokens)  # 887100

# 二次采样,二次采样中丢弃词w_i，并且越高频的词被丢弃的概率越大。
def discard(idx):
    p=max(0,1-math.sqrt(1e-4/counter[idx_to_token[idx]]*num_tokens))
    return random.uniform(0,1)<p
subsampled_dataset=[[tk for tk in st if not discard(tk)] for st in dataset]
print('# tokens: %d' % sum([len(st) for st in subsampled_dataset]))  # 375535

def compute_counts(token):
    return '# %s: before=%d,after=%d' % (token,
                                         sum([st.count(token_to_idx[token]) for st in dataset]),
                                         sum([st.count(token_to_idx[token]) for st in subsampled_dataset]))
print(compute_counts('the'))
print(compute_counts('join'))

# 提取中心词和背景词
def get_centers_and_contexts(dataset,max_window_size):
    centers,contexts=[],[]
    for st in dataset:
        if len(st)<2:  #每个句子至少要有2个词才可能组成一对“中心词-背景词”
            continue
        centers.extend(st)
        for center_i in range(len(st)):
            window_size=random.randint(1,max_window_size)
            indices=list(range(max(0,center_i-window_size),min(len(st),center_i+window_size+1)))
            indices.remove(center_i) # 中心词去掉
            contexts.append([st[idx] for idx in indices])
    return centers,contexts

all_centers,all_contexts=get_centers_and_contexts(subsampled_dataset,5)

# 负采样
# 对于一对中心词和背景词，我们随机采样K个噪声词（实验中设K=5）。
# 根据word2vec论文的建议，噪声词采样概率P(w)设为w词频与总词频之比的0.75次方
def get_negatives(all_contexts,sampling_weights,K):
    all_negatives,neg_candidates,i=[],[],0
    population=list(range(len(sampling_weights)))
    for contexts in all_contexts:
        negatives=[]
        while len(negatives)<len(contexts)*K:
            if i==len(neg_candidates):
                # 根据每个词的权重（sampling_weights）随机生成k个词的索引作为噪声词。
                # 为了高效计算，可以将k设得稍大一点
                i,neg_candidates=0,random.choices(population,sampling_weights,k=int(1e5))
            neg,i=neg_candidates[i],i+1
            if neg not in contexts:
                negatives.append(neg)
        all_negatives.append(negatives)
    return all_negatives

sampling_weights=[counter[w]**0.75 for w in idx_to_token]
all_negatives=get_negatives(all_contexts,sampling_weights,K=5)


# 读取数据
class MyDataset(Data.Dataset):
    def __init__(self,centers,contexts,negatives):
        super(MyDataset, self).__init__()
        self.centers=centers
        self.contexts=contexts
        self.negatives=negatives

    def __len__(self):
        return len(self.centers)

    def __getitem__(self, index):
        return self.centers[index],self.contexts[index],self.negatives[index]

def batchify(data):
    """用作DataLoader的参数collate_fn: 输入是个长为batchsize的list,
        list中的每个元素都是Dataset类调用__getitem__得到的结果
    """
    max_len=max(len(c)+len(n) for _,c,n in data)
    centers,contexts_negatives,masks,labels=[],[],[],[]
    for center,context,negative in data:
        cur_len=len(context)+len(negative)
        centers.append(center)
        contexts_negatives.append(context+negative+[0]*(max_len-cur_len))
        masks.append([1]*cur_len+[0]*(max_len-cur_len))
        labels.append([1]*len(context)+[0]*(max_len-len(context)))
    return torch.tensor(centers).view(-1,1),torch.tensor(contexts_negatives),torch.tensor(masks),torch.tensor(labels)

batch_size=512
dataset=MyDataset(all_centers,all_contexts,all_negatives)
data_iter=Data.DataLoader(dataset,batch_size=batch_size,shuffle=True,collate_fn=batchify)

for batch in data_iter:
    for name,data in zip(['centers','context_negatives','masks','labels'],batch):
        print(name,'shape:',data.shape)
    break

# 跳字模型
# 嵌入层
#embed=nn.Embedding(num_embeddings=len(idx_to_token),embedding_dim=50)
embed_size=100
net=nn.Sequential(
    nn.Embedding(num_embeddings=len(idx_to_token),embedding_dim=embed_size),
    nn.Embedding(num_embeddings=len(idx_to_token),embedding_dim=embed_size)
    )
# 跳字节前向计算
def skip_gram(center,context_negatives,embed_v,embed_u):
    v=embed_v(center) # (bn,1,50)
    u=embed_u(context_negatives) # (bn,len,50)
    pred=torch.bmm(v,torch.transpose(u,1,2))  # (bn,1,len)
    return pred.view(v.shape[0],-1)  # (bn,len)

# 定义损失
class SigmoidBinaryCrossEntropy(nn.Module):
    def __init__(self):
        super(SigmoidBinaryCrossEntropy, self).__init__()

    def forward(self,inputs,targets,mask=None):
        """
        input – Tensor shape: (batch_size, len)
        target – Tensor of the same shape as input
        """
        inputs,targets,mask=inputs.float(),targets.float(),mask.float()
        res=nn.functional.binary_cross_entropy_with_logits(inputs,targets,reduction='none',weight=mask) # (batch_size, len)
        loss= res.mean(dim=1)*mask.shape[1]/torch.sum(mask,dim=1) # (batch_size,)
        return loss.mean()  # scaler


loss=SigmoidBinaryCrossEntropy()

def train(net,lr,num_epochs):
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('train on ',device)
    net=net.to(device)
    optimizer=torch.optim.Adam(net.parameters(),lr=lr)
    for epoch in range(num_epochs):
        start,l_sum,n=time.time(),0.0,0
        for batch in data_iter:
            centers,context_negatives,mask,labels=[d.to(device) for d in batch]
            pred=skip_gram(centers,context_negatives,net[0],net[1])

            los=loss(pred,labels,mask)
            optimizer.zero_grad()
            los.backward()
            optimizer.step()
            l_sum+=los.cpu().item()
            n+=1
        print('epoch %d,loss %.2f,time %.2fs' % (epoch+1,l_sum/n,time.time()-start))

# train(net,0.01,10)
# torch.save(net.state_dict(),'net.pth')

# 应用词嵌入模型
def get_similar_tokens(query_token,k,embed):
    W=embed.weight.data
    x=W[token_to_idx[query_token]]
    similar=nn.CosineSimilarity()
    cos=similar(W,x.view(1,-1)).view(-1)
    _,topk=torch.topk(cos,k=k+1)
    topk=topk.cpu().numpy()

    for i in topk[1:]:  # 除去输入词
        print("cosine sim=%.3f: %s" % (cos[i],idx_to_token[i]))


net.load_state_dict(torch.load('net.pth'))
get_similar_tokens('chip',7,net[0])
