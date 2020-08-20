

class Solution:
    def IsValidExp(self , s ):
        # write code here
        stack=[]
        ops={')':'(','}':'{',"]":"["}
        for ch in s:
            if ch in '[({':
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False
                else:
                    if stack[-1]==ops[ch]:
                        stack.pop()
                    else:
                        return False
        return len(stack)==0

if __name__ == '__main__':
    s=Solution()
    print(s.IsValidExp('{[()())]}'))
