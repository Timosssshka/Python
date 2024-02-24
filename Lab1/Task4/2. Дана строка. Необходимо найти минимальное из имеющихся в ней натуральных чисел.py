def minchis(n):
    min=999999999
    for i in range(1,len(n)):
        if(n[i]<n[i-1]):
            promezh=n[i]
    if len(promezh)<min:
        min=promezh
    return min
print(minchis('999821230'))
