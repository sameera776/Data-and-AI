def power(a,b,ans):
    if(b==0):
        return ans
    ans=ans*a
    return power(a,b-1,ans)

    
def isPrime(n,i):
    if(i*i>n):
        return True
    if(n%i==0):
        return False
    return isPrime(n,i+1)
    

a=5
b=2
ans=1
print(power(a,b,ans))
m=3
print(isPrime(m,2))