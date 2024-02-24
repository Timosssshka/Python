def polindr(n):
    f=1
    s=len(n)
    for i in range (s):
        if n[i].isupper():
            if n[i]!=n[s-1-i]:
                f=0
    if f!=0:
        return "Polindrom"
    else:
        return "Ne polindr"
n = input("Введите строку: ")
print(polindr(n))
