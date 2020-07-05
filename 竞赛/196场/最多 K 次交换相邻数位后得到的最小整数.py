'''
给你一个字符串 num 和一个整数 k 。其中，num 表示一个很大的整数，字符串中的每个字符依次对应整数上的各个 数位 。
你可以交换这个整数相邻数位的数字 最多 k 次。
请你返回你能得到的最小整数，并以字符串形式返回。

 
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def getMinIndex(num,i,k):
    id=i
    for j in range(i+1,min(len(num),i+k+1)):
        if ord(num[j])<ord(num[id]) and j-i<=k :
            id=j
    return id


class Solution(object):
    def minInteger(self, num, k):
        """
        贪心算法，每次找到可以到的最小值，计算要交换多少次，然后执行下一个循环
        :type num: str
        :type k: int
        :rtype: str
        """
        num=list(num)
        i=0
        if 0.5*len(num) ** 2-0.5*len(num): return ''.join(sorted(list(num))) # 不加会时
        while k>0 and i<len(num):
            id=getMinIndex(num,i,k)
            if id==0:
                return ''.join(num)
            x=num.pop(id)
            num.insert(i,x)
            k-=id-i
            i+=1
        return ''.join(num)



if __name__ == '__main__':
    s=Solution()
    print(s.minInteger('9438957234785635408',23))


