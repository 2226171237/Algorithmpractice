'''
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for x in  num:
            while len(stack) and stack[-1]>x and k>0:
                stack.pop()
                k-=1
            stack.append(x)
        final_stack=stack if k==0 else num[:-k]
        return ''.join(final_stack).lstrip('0') or '0'

if __name__ == '__main__':
    s=Solution()
    print(s.removeKdigits('01432219',3))
