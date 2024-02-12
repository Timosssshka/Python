def k_del(n):
    k=0
    for i in range(1, n+1):
        if (n % i) == 0:
            if i%3!=0:
                k+=1
    return k
print(k_del(5))
