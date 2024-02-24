import random
def swap(n):
    slovo=n
    slovo_list=list(slovo)
    swapping=random.sample(slovo_list,len(slovo_list))
    return swapping
n=input("Введите строку: ")
print(swap(n))
