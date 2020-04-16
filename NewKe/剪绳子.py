'''
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入一个数n，意义见题面。（2 <= n <= 60）
'''

# 递推式 f(n)=max(f(i),f(n-i)) 1<=i<n

class Solution:
    def cutRope(self, number):
        # write code here
        if number<2: # 绳子长度大于2
            return 0
        if number==2:
            return 1
        if number==3:
            return 2
        product=[]
        product.extend([0,1,2,3])  # 长度为0，1，2，3

        for i in range(4,number+1):
            maxs=0
            for j in range(1,i//2+1):
                prod=product[j]*product[i-j]
                if maxs<prod:
                    maxs=prod
            product.append(maxs)
        return product[-1]

if __name__ == '__main__':
    S=Solution()
    print(S.cutRope(4))




