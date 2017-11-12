#Problem 9

for a in range(1,1000):
    for b in range(a,1000):
        c=1000-a-b
        if (c*c==a*a+b*b):
            print(a*b*c)

#Problem 10

summ=0
for j in range(2,2000000):
    for i in range(2,j):
        if (j%i==0):
            break
    else:
        summ+=j


print(summ)