#problem 1:

sums=0
for i in range(1,1000):
    if (i%3==0 or i%5==0):
        sums=sums+i

print(sums)

#problem 2:

a=0
b=1
sum=0
c=0
while (c<4000000000):
    c=a+b
    a=b
    b=c
    if (c%2==0):
        sum=sum+c

print(sum)