import random
def swap(n):
    slovo=n
    slovo_list=list(slovo)
    swapping=random.sample(slovo_list,len(slovo_list))
    return swapping
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
def uporyad(n):
    s = n.split()
    for i in range(1, len(s)):
        word = s[i]
        j = i - 1
        while j >= 0 and len(s[j]) > len(word):
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = word

    sorted_sentence = ' '.join(s)
    return sorted_sentence
print("Список функций, которые вы можете использовать:")
print("1. Перемешать все символы строки в случайном порядке.")
print("2. Строка, состоящая из символов латиницы. Проверить, образуют ли прописные символы этой строки палиндром.")
print("3. Строка, в которой записаны слова через пробел. Упорядочить слова по количеству букв в каждом слове.")
n=int(input("Введите номер функции: "))
match n:
    case 1:
        n=input("Введите строку: ")
        print(swap(n))
    case 2:
        n = input("Введите строку: ")
        print(polindr(n))
    case 3:
        n = input("Введите строку: ")
        print(uporyad(n))
