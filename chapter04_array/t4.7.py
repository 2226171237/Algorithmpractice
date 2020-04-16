#-*-coding=utf-8-*-
'''
如何求数组中两个元素的最小距离？
给定一个数组，数组中含有重复元素，给定两个数字num1,num2,
求这两个数字在数组中出现的位置的最小距离。
'''
# 蛮力法
def minDistance1(arr,num1,num2):
    min=len(arr)

    for i,x in enumerate(arr):
        if x==num1:
            j=0
            while j<len(arr):
                if arr[j]==num2:
                    d=abs(j-i)
                    if d<min:
                        min=d
                j+=1
    return min

# 动态规划的方法
def minDistance2(arr,num1,num2):
     minD=len(arr)+1
     lastPost1=-1
     lastPost2=-1
     for i,x in enumerate(arr):
         if x==num1:
             lastPost1=i
             if lastPost2>=0:
                 tmp=abs(lastPost2-lastPost1)
                 if tmp<minD:
                     minD=tmp
         if x==num2:
             lastPost2=i
             if lastPost1>=0:
                 tmp = abs(lastPost2 - lastPost1)
                 if tmp < minD:
                     minD = tmp
     return minD


if __name__ == '__main__':
    arr=[4,5,6,4,7,4,6,4,7,3,8,5,6,4,3,8]
    print(minDistance1(arr,8,4))
    print(minDistance2(arr,8,4))