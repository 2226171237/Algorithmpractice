
class Solution:
    def question(self , a , b ):
        # write code here
        for k in range(1,501):
            x=(a+k)**0.5
            y=(b+k)**0.5
            if int(x)==x and int(y)==y:
                return k


if __name__ == '__main__':
    s=Solution()
    print(s.question(100,200))