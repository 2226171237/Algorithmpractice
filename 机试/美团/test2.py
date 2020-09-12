

def solve(txt):
    small=0
    big=0
    for x in txt:
        if 'a'<=x<='z':
            small+=1
        else:
            big+=1
    small,big=min(small,big),max(small,big)
    return big-(small+big)//2

import sys
txt=sys.stdin.readline().strip()
print(solve(txt))
