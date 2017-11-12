
#Problem 3
def is_prime(n):   #600851475143
    for i in range(2, n):
        if (n%i==0):
            return 0
    return 1
n=13195   #600851475143
l=[]
for j in range(2,int(n/2)+1):
    if (n%j==0):
        if (is_prime(j)==1):
            l.append(j)
print(max(l))

#Problem 4
x = 999
p = []
min = 99
while x > min:
     for i in range(x,min,-1):
         product = x*i
         candidate = str(product)
         if candidate == candidate[::-1]:
             p.append(product)
             min = i
             break
     x -= 1
print(max(p))