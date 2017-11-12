"""
#Problem 5

def hcf(a,b):
    max=1
    if (a>b):
        for i in range(1,b+1):
            if (a%i==0 and b%i==0):
                if (max<i):
                    max=i
        return max
    else:
        for i in range(1,a+1):
            if (a%i==0 and b%i==0):
                if (max<i):
                    max=i
        return max
ans=1
for i in range(2,20+1):
    lcm=(ans*i)//hcf(ans,i)
    ans=lcm

print(lcm)
"""
#problem 6
n=100
sum=(n*(n+1)*(2*n + 1))/6
square=((n*(n+1))/2)**2
print(square-sum)

