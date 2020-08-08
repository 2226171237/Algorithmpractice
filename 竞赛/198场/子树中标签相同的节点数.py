from collections import defaultdict
class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        tree=defaultdict(list)
        node_set=set()
        for e in edges:
            if e[1]==0:
                tree[e[1]].append(e[0])
                node_set.add(e[0])
                continue
            if e[1] not in node_set:
                tree[e[0]].append(e[1])
                node_set.add(e[1])
            else:
                tree[e[1]].append(e[0])
                node_set.add(e[0])

        res=[0 for _ in range(n)]

        def afterOrder(root):
            if root not in tree:
                res[root]=1
                return {labels[root]:1}
            tmp=[]
            for child in tree[root]:
                tmp.append(afterOrder(child))
            tmp_dict=dict()
            for x in tmp:
                for y in x:
                    tmp_dict[y]=tmp_dict.get(y,0)+x[y]
            tmp_dict[labels[root]]=tmp_dict.get(labels[root],0)+1
            res[root]=tmp_dict[labels[root]]
            return tmp_dict
        print(afterOrder(0))
        return res

if __name__ == '__main__':
    s=Solution()
    print(s.countSubTrees(25,[[4,0],[5,4],[12,5],[3,12],[18,3],[10,18],[8,5],[16,8],[14,16],[13,16],[9,13],[22,9],[2,5],[6,2],[1,6],[11,1],[15,11],[20,11],[7,20],[19,1],[17,19],[23,19],[24,2],[21,24]]
,"hcheiavadwjctaortvpsflssg"))
