# Да се напише функция, която има два входни параметъра:
# списък от цели числа L и цяло число N. Тя връща като резултат
# списък от тези числа от списъка L, за които остатъка от делението
# им на N не е нула.
# Демонстрирайте приложението на тази функция,
# като въведете списък L от цели числа от клавиатурата, след което въведете
# цяло число N, и след като приложите функцията, изведете на екрана полученият резултат.

my_list = [12,2,3,123,35,10]
N=12

# Вариант 1:
def myf(L,n):
    copyL=L.copy()
    for l in copyL:
        if l%n==0: L.remove(l)

myf(my_list,N)
print(my_list)

# Вариант 2:
mylam=lambda x: x%N!=0
res=list(filter(mylam,my_list))
print(res)