def minchisl(n):
    while n>0:
        if n % 2==0:
            cn=n%10
            k=10000000
            n = n // 10
            if (cn<k):
                k=cn
        else:
            nn=n%10
            m=99999999
            n = n // 10
            if (nn<m):
                m=nn
    return m
print(minchisl(125))
