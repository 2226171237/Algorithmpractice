
def cntPrime(n):
    primes=[True for _ in range(n+1)]
    for i in range(2,n+1):
        if primes[i]:
            for j in range(2*i,n+1,i):
                primes[j]=False
    cnt=0
    for i in range(2,n+1):
        if primes[i]:
            cnt+=1
    return cnt

def cntPrime2(n):
    primes=[True for _ in range(n+1)]
    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i,n+1,i):
                primes[j]=False
    cnt=0
    for i in range(2,n+1):
        if primes[i]:
            cnt+=1
    return cnt

print(cntPrime(65535))
print(cntPrime2(65535))