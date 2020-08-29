
import  sys

def solve(S):
    mainS={'A','H','I','M','O','T','U','V','W','X','Y'}
    i=0
    j=len(S)-1
    while i<len(S) and j>=0:
        if S[i]==S[j] and S[i] in mainS:
            i+=1
            j-=1
        else:
            return 'NO'
    return 'YES'

s=sys.stdin.readline().strip()
while len(s):
    print(solve(s))
    s = sys.stdin.readline().strip()

if __name__ == '__main__':
    print(solve('AOOA'))
