# Задача 1:
#
# Да се напише програма, която създава списък
# Списъкът е от случайни числа в интервала от 1 до 10000 включително

# Текст за принтиране:
p_1=' Числата да бъдат кратни (да се делят точно) на 2'
p_2=' Числата да НЕ бъдат кратни (да НЕ се делят точно) на 2'
p_3=' Числата да съдържат цифрата 1'
p_4=' Числата //3 да бъдат нечетни'
p_5=' не съдържат "11"'
p_6=' се делят точно на 3'
p_7=' са 3-цифрени или 4-цифрени числа, чиято трета цифра е 3'
p_8=' всички едноцифрени'
p_9=' всички двуцифрени'
p_10=' всички трицифрени'
p_11=' всички четицифрени'
p_12=' всички двуцифрени или трицифрени, които се делят точно на 3'

print_list=[p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,p_12]
# print_list е списък с текстовете на условия за принтиране

import random as rd
n=100 # брой на случайните числа в списъка
# n=int(input('Въведете брой на случайните числа: ))
L=[rd.randint(1,10000) for i in range(n)] # основен списък
# print('Първоначален списък')
# print(L)

L_1= lambda a: a%2==0
L_2= lambda a: a%2!=0
L_3= lambda а: '1' in str(а)
L_4= lambda a: (a//3)%2!=0 # dali a//3 e нечетно число
L_5= lambda а: '11' not in str(а) 
L_6= lambda a: a%3==0
L_7= lambda a: (len(str(a))>=3 and str(a)[2]=='3')
L_8= lambda a: len(str(a))==1
L_9= lambda a: len(str(a))==2
L_10= lambda a: len(str(a))==3 
L_11= lambda a: len(str(a))==4 
L_12= lambda a: (len(str(a))>=2 and len(str(a))<4 and a%3==0)

lambda_list=[L_1,L_2,L_3,L_4,L_5,L_6,L_7,L_8,L_9,L_10,L_11,L_12]
# Всеки елемент на lambda_list е конкретна lambda функция

map_list=[list(map(l_l,L)) for l_l in lambda_list]
# Всеки елемент на map_list е списък от филтрираните числа от списъка L посредством поредната функция ламбда

filter_list=[list(filter(l_l, L)) for l_l in lambda_list]
# Всеки елемент на filter_list е списък от филтрираните

# print('\n Задача 1: списъци с map и filter\n')
# for i in range(len(print_list)):
#     print(print_list[i])
#     print(map_list[i])
#     print(filter_list[i])


# # Задача 2:
# #
# # Да се напише програма, която създава речник
# # Ключовете на речника са числата от 0 до 9 включително
# # Стойността за всеки ключ е списък, който съдържа числата от
# # списъка от зад.1, които:
# # test_1: завършват с цифра=ключа
# # test_2: започват с цифра=ключа
# # test_3: първата им цифра % 3=ключа
# # test_4: завършват с цифра=ключа +1 или последната цифра-1=ключа
#
# t_1=' завършват с цифра=ключа'
# t_2=' започват с цифра=ключа'
# t_3=' първата им цифра % 3=ключа'
# t_4=' завършват с цифра=ключа +1 или последната цифра-1=ключа'
# print_txt=[t_1,t_2,t_3,t_4]
#
# # За да може функцията filter да се справи ще използваме zip-на параметрите на lambda, като
# # key=zipped[0] и number=zipped[1]
# test_1=lambda zipped: zipped[0]==int(str(zipped[1])[-1])
# test_2=lambda zipped: zipped[0]==int(str(zipped[1])[0])
# test_3=lambda zipped: zipped[0]==int(str(zipped[1])[0])%3
# test_4=lambda zipped: zipped[0]+1==int(str(zipped[1])[-1])
# test=[test_1,test_2,test_3,test_4]
#
# print('\n Задача 2: речници с filter\n')
# dic_list=[{},{},{},{}]
# number_of_keys=10
# for dl in range(len(dic_list)):
#     for i in range(number_of_keys):
#         zipped=zip([i] * len(L), L)
#         # За всеки ключ се създава вектор с дължина L , за да могат да бъдат тествани всички стойности от L
#         values_4dic_dl=list(filter(test[dl], zipped))
#         # values_4dic_dl е списък от редици, всяка с по 2 елемента:  ключ и число от случайния списък
#         # Пример: [(0,4),(0,5),(0,6),(0,7)]
#         # Връща списък от зипнати двойки: ключ-стойност, като ключът е постоянен
#         if len(values_4dic_dl)>0:
#             dic_list[dl][i] = list(zip(*values_4dic_dl))[1]
#             # за да може да се разделят зипнатите двойки на два списъка:
#             # list(zip(*values_4dic_dl))
#             # и тогава, първият списък ще съдържа ключовете
#             # а вторият - случайните числа, отговарящи на условието
#     print(print_txt[dl])
#     print(dic_list[dl])

print('\n Задача 3: редици с filter\n')
# # Задача 3:
# #     Като използвате функцията lambda, map, reduce и filter:
# # 	* намерете числата и сумата на аритметична прогресия с а0=1 , d=3, n=20
# # 	* произведението на аритметична прогресия с а0=1 , d=3, n=20
# # 	* намерете числата и сумата на геометрична прогресия с а0=1 , q=3, n=20
# # 	* произведението на геометрична прогресия с а0=1 , q=3, n=20
# # 	* числата и сумата на фибоначи за първите 20 числа
# # 	* четните числа на Фибоначи за първите 100 числа
#
r_1=' намерете числата и сумата на аритметична прогресия с: а0=1 , d=3, n=20'
r_2=' произведението на аритметична прогресия с: а0=1 , d=3, n=20'
r_3=' намерете числата и сумата на геометрична прогресия с: а0=2 , q=3, n=20'
r_4=' произведението на числата от геометрична прогресия с: а0=1 , q=3, n=20'
r_5=' първите 20 числа числа на фибоначи и тяхната сума'
r_6=' четните числа на Фибоначи от първите 100 числа на Фибоначи'

from functools import reduce
# print_txt=[r_1,r_2,r_3,r_4,r_5,r_6]
# n=20
# lam_1_redica=lambda i,a=1,d=3: a+d*i
lam_1_suma=lambda a,b: a+b
# lam_2=lambda a,b: a*b
# res_1_1=list(map(lam_1_redica,list(range(n))))
# res_1_2=reduce(lam_1_suma,res_1_1)
# res_1_3=reduce(lam_2,res_1_1)
# res_1=(res_1_1,res_1_2,res_1_3)
# print(r_1,res_1)
#
# lam_3_redica=lambda i,a=2,q=3: a*(q**i)
# res_3_1=list(map(lam_3_redica,list(range(n))))
# res_3_2=reduce(lam_1_suma,res_3_1)
# res_3_3=reduce(lam_2,res_3_1)
# res_1=(res_3_1,res_3_2,res_3_3)
# print(r_3,res_1)
#
# # Lambda + Reduce: връща списък с числата на фибоначи, като x[-1] е 0, а x[-2] е 1
# lam=lambda x, _: x+[x[-1]+x[-2]]
# lam_5=lambda n: list(reduce(lam,range(n-2), [0, 1])) # list
# lam_5_2=reduce(lam_1_suma,lam_5(n)) #sum
# lam_7_1=lambda x: x%2==0
# lam_7=list(filter(lam_7_1,lam_5(100)))
# print(r_5,[lam_5(7),lam_7])


# Lambda + Map: връща списък с числата на Фибоначи
# алтернатива на ред 142: lam_5
fib_list = [0, 1]
print('Initial Fibonacci list: ',fib_list)
count=7
fib_lam=lambda _: fib_list.append(sum(fib_list[-2:]))
# fib_list и count трябва да бъдат глобални променливи !!!
# ламбда функция, която добавя към глобалния списък следващото число на Фибоначи
# формулата за поредното число на Фибоначи е: ако k е индекса на търсеното поредно число, то:
# f(k)=f(k-1)+f(k-2), т.е. на сумата последните две преди него
# => последните две числа в един списък с числа на Фибоначи са основа за изчисляване на следващото такова
# или sum(fib_list[-2:])
lam_6=list(map(fib_lam,range(2, count)))
# в lam_6 функцията fib_lam в map() се изпълнява len(range(2, count)) брой пъти
# т.е. толкова пъти се изчислява ново число на Фибоначи
# lam_6 е списък от стойности None, които се генерират от функцията .append()
print('+ Next '+str(count-2)+' Fibonacci numbers: ',fib_list)
lam_5_2=reduce(lam_1_suma,fib_list) #sum
# т.к. fib_lam модифицира глобалната променлива от тип списък fib_list, то в reduce трябва да използваме fib_list като контейнер
print('Sum of first '+str(count)+' Fibonacci numbers: ',lam_5_2)

# Друг вариант с потребителска функция и map:
def fibonacci(count):
    sequence = [0, 1]
    any(map(lambda _: sequence.append(sum(sequence[-2:])), range(2, count)))
    return sequence[:count]
# print(fibonacci(10))