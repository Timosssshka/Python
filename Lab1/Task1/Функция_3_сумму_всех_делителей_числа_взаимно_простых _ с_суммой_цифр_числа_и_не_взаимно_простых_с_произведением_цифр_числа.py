def sums(n):
    s=0
    while n > 0:
        k=n%10
        s+=k
        n//10
        return s
def proiz(n):
    pr=1
    while n>0:
        k=n%10
        pr*=k
        n//10
        return pr
def GOD(n1,n2):
    nod=0
    for i in range(1, min(n1,n2)+1):
        if(n1%i==0 and n2%i==0):
            nod=i
            return nod
def allsum(n):
    s=0
    n_sum = sums(n)
    n_proizv=proiz(n)
    for i in range(2, n+1):
        if(n%i==0 and GOD(n_sum,i)==1):
            s+=i
    for i in range(2, n + 1):
        if (n % i == 0 and GOD(n_proizv, i) != 1):
            s+=i
    return s
print(allsum(65))
