#-*-coding=utf-8-*-
'''
如何从数组中找出满足a+b=c+d的两个数对。
给定一个数组，找出数组中是否有两个数对(a,b)和(c,d)，使得a+b=c+d,
其中a,b,c,d为不同的元素。如果有多个答案，打印任一个即可。
例：[3,4,7,10,20,9,8]
输出：(3,8)和(4,7)
'''

# 有bug
def find(data):
    hash_d=dict()
    for i,x in enumerate(data):
        j=i
        for y in data[i+1:]:
            j+=1
            if x+y in hash_d:
                if i not in hash_d[x+y][2] and j not in hash_d[x+y][3]:
                    print(hash_d[x+y][:2],(x,y))
                    hash_d[x + y][2].add(i)
                    hash_d[x + y][3].add(j)

            else:
                hash_d.update({x+y:[x,y,set([i]),set([j])]})

if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,8,9]
    find(arr)


