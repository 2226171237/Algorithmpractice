'''
给定一棵树的根节点, 在已知该树最大深度的情况下, 求节点数最多的那一层并返回具体的层数。
如果最后答案有多层, 输出最浅的那一层，树的深度不会超过100000。实现代码如下，请指出代码中的多处错误：
struct Node{
    vector < Node * > sons;
};

void dfsFind(Node * node, int dep, int counter[])
{
    counter[dep] + +;
    for (int i = 0; i < node.sons.size();i + +)
    {
        dfsFind(node.sons[i], dep, counter);
    }
}


int find(Node * root, int maxDep)
{
    int depCounter[100000];
    dfsFind(root, 0, depCounter);
    int max, maxDep;
    for (int i = 1; i <= maxDep; i++)
    {
        if (depCounter[i] > max)
        {
            max = depCounter[i];
            maxDep = i;
        }
    }
    return maxDep;
}
'''

class Node:
    def __init__(self,x,childs=[]):
        self.x=x
        self.childs=childs

def dfsFind(root,dep,counter):
    counter[dep]+=1
    for node in root.childs:
        dfsFind(node,dep+1,counter)

def find(root,maxDep):
    depConter=[0 for _ in range(maxDep)]
    dfsFind(root,0,depConter)
    max=depConter[0]
    level=1
    for i,x in enumerate(depConter):
        if x>max:
            max=x
            level=i+1
    return level

if __name__ == '__main__':
    node1=Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    root=node1
    root.childs=[node2,node3,node4,node5,node6]
    node2.childs=[node7]
    node3.childs=[node8,node9]

    print(find(root,10))