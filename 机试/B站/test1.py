from operator import mul,add,sub,truediv
class Solution:
    def Game24Points(self , arr ):
        # write code here
        if len(arr)==0:
            return False
        if len(arr)==1:
            return abs(arr[0]-24)<1e-6
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i!=j:
                    B=[arr[k] for k in range(len(arr)) if k!=i and k!=j]
                    for opt in (mul,sub,add,truediv):
                        if (opt==mul or opt==add) and j<i:continue
                        if opt!=truediv or arr[j]:
                            B.append(opt(arr[i],arr[j]))
                            if self.Game24Points(B):
                                return True
                            B.pop()
        return False

if __name__ == '__main__':
    s=Solution()
    print(s.Game24Points([7,2,1,10]))