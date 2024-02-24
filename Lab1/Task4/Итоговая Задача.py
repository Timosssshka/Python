def K_simv(n):
    k=1
    m=1
    for i in range(1,len(n)):
        if (n[i]==n[i-1]):
            k+=1
        else:
            if m<k:
                m=k
    return m

def minchis(n):
    min=999999999
    for i in range(1,len(n)):
        if(n[i]<n[i-1]):
            promezh=n[i]
    if len(promezh)<min:
        min=promezh
    return min


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
print("Список функций, которые вы можете использовать:")
print("1. Необходимо найти наибольшее количество идущих подряд символов кириллицы.")
print("2. Дана строка. Необходимо найти минимальное из имеющихся в ней натуральных чисел.")
print("3. Дана строка. Необходимо найти наибольшее количество идущих подряд цифр.")
n=int(input("Введите номер функции: "))
match n:
    case 1:
        n=input("Введите строку: ")
        print(K_simv(n))
    case 2:
        n = input("Введите строку: ")
        print(minchis(n))
    case 3:
        n = input("Введите строку: ")
        print(k_podr(n))
