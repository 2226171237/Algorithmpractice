import numpy as np

def compute_intersection(set_1,set_2):
    '''计算两个集合之间的交集
    :param set_1: a array of dimensions (n1, 4), anchor表示成(xmin, ymin, xmax, ymax)
    :param set_2: a array of dimensions (n2, 4), anchor表示成(xmin, ymin, xmax, ymax)
    :return intersection: a array of shape (n1,n2)
    '''
    lower_bounds=np.maximum(set_1[:,:2].reshape(-1,1,2),set_2[:,:2].reshape(1,-1,2)) # (n1,n2,2)
    upper_bounds=np.minimum(set_1[:,2:].reshape(-1,1,2),set_2[:,2:].reshape(1,-1,2)) # (n1,n2,2)

    intersection=np.clip(upper_bounds-lower_bounds,a_min=0,a_max=None)  # (n1,n2,2)

    return intersection[:,:,0]*intersection[:,:,1]


def compute_iou(set_1,set_2):
    '''计算两个集合之间的IOU
    :param set_1: a array of dimensions (n1, 4), anchor表示成(xmin, ymin, xmax, ymax)
    :param set_2: a array of dimensions (n2, 4), anchor表示成(xmin, ymin, xmax, ymax)
    :return iou: a array of shape (n1,n2)
    '''
    intersection=compute_intersection(set_1,set_2) # (n1,n2)
    area_set_1=(set_1[:,2]-set_1[0])*(set_1[:,3]-set_1[:,1])   # (n1,)
    area_set_2 = (set_2[:, 2] - set_2[0]) * (set_2[:, 3] - set_2[:, 1]) # (n2,)

    union=area_set_1.reshape(-1,1)+area_set_2.reshape(1,-1)-intersection # (n1,n2)

    return intersection/union # (n1,n2)

from collections import namedtuple
Pred_BB_Info = namedtuple("Pred_BB_Info", ["index", "class_id", "confidence", "xyxy"])

def non_max_suppression(bb_info_list,nms_threshold=0.5):
    '''非极大值抑制
    :param bb_info_list: Pred_BB_Info的列表, 包含预测类别、置信度等信息
    :param nms_threshold: 阈值
    :return:
        output: Pred_BB_Info的列表, 只保留过滤后的边界框信息
    '''
    output=[]
    # 现根据置信度从高到低排序
    sorted_bb_info_list=sorted(bb_info_list,key=lambda  x:x.confidence,reverse=True)

    while len(sorted_bb_info_list)!=0:
        best=sorted_bb_info_list.pop(0)
        output.append(best)
        if len(sorted_bb_info_list)==0:
            break
        bb_xyxy=[]
        for bb in sorted_bb_info_list:
            bb_xyxy.append(bb.xyxy)
        iou=compute_iou(np.array(best.xyxy).reshape(1,-1),np.array(bb_xyxy))[0] # shape: [len(sorted_bb_info_list),]
        n=len(sorted_bb_info_list)
        sorted_bb_info_list=[sorted_bb_info_list[i] for i in range(n) if iou[i]<=nms_threshold]

    return output



def multiBoxDetection(cls_prob,loc_pred,anchor,nms_threshold=0.5):
    '''输出预测的边框
    :param cls_prob: 经过softmax后得到的各个锚框的预测概率, shape:(bn, 预测总类别数+1, 锚框个数)
    :param loc_pred: 预测的各个锚框的偏移量, shape:(bn, 锚框个数*4)
    :param anchor:  multiAnthorBoxGenerator输出的默认锚框, shape: (1, 锚框个数, 4)
    :param nms_threshold: 非极大抑制中的阈值
    :return:
        所有锚框的信息, shape: (bn, 锚框个数, 6)
        每个锚框信息由[class_id, confidence, xmin, ymin, xmax, ymax]表示,值域在0到1之间
        class_id=-1 表示背景或在非极大值抑制中被移除了
    '''
    bn=cls_prob.shape[0]

    def multiBoxDetection_one(c_p,l_p,anc,nms_threshold=0.5):
        """
        multiBoxDetection的辅助函数, 处理batch中的一个
        Args:
            c_p: (预测总类别数+1, 锚框个数)
            l_p: (锚框个数*4, )
            anc: (锚框个数, 4)
            nms_threshold: 非极大抑制中的阈值
        Return:
            output: (锚框个数, 6)
        """
        pred_bb_num=c_p.shape[1]
        anc=anc+l_p.reshape(-1,4)  # 加上偏移量  ?? 直接相加吗?????

        class_id=np.argmax(c_p,axis=0)
        confidence=np.max(c_p,axis=0)

        pred_bb_info=[Pred_BB_Info(index=i,
                                   class_id=class_id[i]-1,  # 正类从0开始
                                   confidence=confidence[i],
                                   xyxy=[*anc[i]])  # xyxy是一个列表
                      for i in range(pred_bb_num)]
        # 正类的index
        obj_bb_idx=[bb.index for bb in non_max_suppression(pred_bb_info,nms_threshold)]

        output=[]
        for bb in pred_bb_info:
            output.append([
                (bb.class_id if bb.index in obj_bb_idx else -1),
                bb.confidence,
                *bb.xyxy
            ])
        return np.array(output)  # shape: (锚框个数, 6)

    batch_output=[]
    for b in range(bn):
        batch_output.append(multiBoxDetection_one(cls_prob[b],loc_pred[b],anchor[0],nms_threshold))
    return np.stack(batch_output)
