

def solve(s):
    encode_map=dict()
    t=0
    for i in range(ord('a'),ord('z')+1):
        t+=1
        encode_map[chr(i)]=t
    for i in range(ord('A'),ord('Z')+1):
        t+=1
        encode_map[chr(i)] = t
    for i in range(ord('0'),ord('9')+1):
        t+=1
        encode_map[chr(i)]=t

    result=[]

    i=0
    num = 0
    while i<len(s):
        x=s[i]
        code=encode_map[x] if x in encode_map else 0
        num=num<<6 ^ code
        if (i+1)%5==0:
            result.append(num)
            num=0
        i+=1
    if len(s)%5!=0:
        result.append(num)
    return ' '.join(map(str,result))

import sys
s=sys.stdin.readline().strip()
print(solve(s))




