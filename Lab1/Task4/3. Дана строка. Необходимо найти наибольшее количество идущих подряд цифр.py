def k_podr(n):
    max=1
    k=1
    for i in range (1,len(n)):
        if (n[i]==n[i-1]):
            k+=1
        else:
            k=1
        if (k>max):
            max=k
    return max
print(k_podr('5555555555123555331234666666666666666666666666'))
