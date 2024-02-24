def K_simv(n):
    k=1
    m=1
    for i in range(1,len(n)):
        if (n[i]==n[i-1]):
            k+=1
        else:
            if m<k:
                m=k
            k=1
return m
print(K_simv("Аятутаагавввдд"))
