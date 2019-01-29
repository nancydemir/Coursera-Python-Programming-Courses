def appendsums(lst):
    n=0
    x=0
    sum=0
    while n<25:
            a=lst[len(lst)-1]
            b=lst[len(lst)-2]
            c=lst[len(lst)-3]
            x=a+b+c
            lst.append(x)
            n=n+1
sum_three = [0, 1, 2]
appendsums(sum_three)
print (sum_three[20])
