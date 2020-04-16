'''
如何对由大小写字母组成的字符数组排序？
由一个有大小写字母组成的字符串，请对它进行重新组合，使得其中得所有小写字母排在大写字母的前面
（大写字母或小写字母之间不要求保持原来的次序）
'''

def reversedStr(s):
    s=list(s)
    low=0
    high=len(s)-1
    while low <high:
        while low<high and 'A'<=s[high]<='Z':
            high-=1
        while low<high and 'a'<=s[low]<='z':
            low+=1
        tmp=s[high]
        s[high]=s[low]
        s[low]=tmp
    return ''.join(s)

if __name__ == '__main__':
    s='fedeANdBna'
    print(reversedStr(s))