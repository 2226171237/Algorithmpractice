


def isPrimes(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def  countPrimes(n):
    primes=[False for _ in range(n+1)]
    cnt=0
    for i in range(2,n+1):
        if primes[i]==False:
            if isPrimes(i):
                cnt+=1
                j=i*2
                while j<n+1:
                    primes[j]=True
                    j+=i
    return cnt

def  countPrimes2(n):
    primes=[True for _ in range(n+1)]
    cnt=0
    for i in range(2,n+1):
        if primes[i]:
            cnt+=1
            j=i*2
            while j<n+1:
                primes[j]=False
                j+=i
    return cnt

print(countPrimes(1000000))
print(countPrimes2(1000000))