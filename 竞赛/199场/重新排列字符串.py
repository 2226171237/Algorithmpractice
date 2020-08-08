
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res=[' ' for _ in range(len(s))]
        for i,id in enumerate(indices):
            res[id]=s[i]
        return ''.join(res)

