# зад.1: lambda функции: да се напишат:
#     -  l_1: събиране на две числа => числов резултат, два входни параметъра-по един за всяко число
#     -  l_2: увеличаване на число с 3 =>числов резултат, един входен параметър
#     -  l_3: повдигане на степен 3=>числов резултат, един входен параметър
#     -  l_4: проверка дали числото се дели точно на 3 => резултат: True/False, един входен параметър
#     -  l_5: намира x//y => числов резултат, два входни параметъра-по един за всяко число
#     -  l_6: намира x%y => числов резултат, два входни параметъра-по един за всяко число
#
# зад.2: Създайте един списък L с числата от 1 до 1000
# зад.3: Приложете функцията map върху списъка L със всяка една от ламбда функциите
# зад.4: Приложете функцията filter върху списъка L със ламбда функцията l_4
# зад.5: Приложете функцята reduce върху L със всяка една от подходящите ламбда функциите

l_1= lambda a,b: a+b # може да се използва с map, reduce
l_2= lambda a: a+3 # може да се използва с map
l_3= lambda a: a**3 # може да се използва с map
l_4= lambda a: a%3==0 # може да се използва с map и filter, защото резултатът е от булев тип, т.е. True или False
l_5= lambda a,b: a//b # може да се използва с map, reduce
l_6= lambda a,b: a%b # може да се използва с map, reduce
l_7= lambda a,b: [a+b, a-b, b-a, a**b, b**a, a//b, a%b, b//a, b%a, a%b==0, b%a==0]
# l_7 връща списък с резултатите от операциите върху две числа
# може да се използва с map


l_8= lambda a,b: (a//b,a%b)
# l_8 връща редица от двете операции
# може да се използва с map
l_9= lambda a,b: (abs(a-b)//a) +1
# abs(a) връща абсолютната стойност на a, например: abs(-5)=5 и abs(5)=5
# може да се използва с map

L_1=[i for i in range(1,1000)]
L_3=list(range(1,1000))
print(list(map(l_7,L_1[:10],L_3[:10])))
print(L_3)
# map(име на функция,списък): пресмята функцията за всеки един елемент от списъка
# резултатът, който връща map трябва задължително да се конвертира с функцията list(), за да стане четим
# list(map(име на функция,списък))

# filter(име на функция,списък): пресмята функцията за всеки един елемент и ако резултатът е True,
# то елементът бива добавен в списъка, който се връща
# резултатът, който връща map трябва задължително да се конвертира с функцията list(), за да стане четим
# list(filter(име на функция,списък))

# # Пример за разликата между map и filter
# result_l4_map=list(map(l_4,L_3))
# result_l4_filter=list(filter(l_4,L_3))
# print(result_l4_map)
# print(result_l4_filter)

# решение чрез специалната функция map
# result_l2_map=list(map(l_2,L_3))
# print(result_l2_map)
#
#
# # итеративно решение, защото използва цикъл
# result_l2_for=[]
# for i in L_3:
#     result_l2_for.append(i+3)
# print(result_l2_for)

# # Пример за използване на map с две променливи за функцията:
# # list(map(име на функция,списък-1,списък–2)):

# Lh=L_1[::-1]
# L_2=list(map(l_9,Lh,L_1)) # списък от 1-ци
# # print(L_2)
# # #
#
# # Циклична обработка на едни и същи данни с множество lambda функции, запазени като елементи на списъци:
# F_1=[l_1,l_5,l_6,l_7,l_8] # списък на функциите, които имат две променливи
# F_2=[l_2,l_3,l_4] # списък на функциите, които имат една променлива
#
#
# # reduce се използва, когато трябва да обработим някакъв списък, но резултатът трябва
# # да бъде една единствена стойност, а не множество от стойности (напр. списък от стойности):
#
# from functools import reduce
# # # е за ламбда функциите с две променливи
# for i in range(len(F_1)-2): # l_1,l_5,l_6
#     print('l_'+str(i+1)+': ',list(map(F_1[i],L_1,L_2))) # връща поредица от стойности
#     print('l_'+str(i+1)+': ',reduce(F_1[i],L_1)) # връща една единствена стойност
#     # ВАЖНО!!! reduce използва един списък със стойности, независимо, че
#     # функцията изисква да се подадат 2 стойности
#
# # е за ламбда функциите с една променлива
# for i in range(len(F_2)):
#     print('l_'+str(i+1)+': ',list(map(F_2[i],L_1)))
#
# # ************************************************************************
# # ЗАДАЧА: връща всички числа а**3, ако а%3==0
# # ************************************************************************
#
# # Вариант 1: чрез кратката форма за for:
ll=[i**3 for i in range(1,1000) if i%3==0] # a%3==0
# #
# # Вариант 2: чрез map и filter: (a**3)%3==0
k=list(map(l_3,L_1)) # списък, който искам да филтрирам, т.е. а**3
# p=list(filter(l_4,k)) # списък с условията за филтриране, T/F
# #
# # Вариант 3: смесено използване на map и filter в един израз: (a**3)%3==0
# p=list(filter(l_4,map(l_3,L_1)))
# #
# # Проверка, дали всяка стойност от ll съответства на стойност от p:
# is_all_in_list_true=lambda x,y: x&y
# a_is_b=lambda a,b: a==b
#
# ab=list(map(a_is_b,ll,p)) #Списък от True и False
# result=reduce(is_all_in_list_true,ab)
# print(result)
# # АлтернативнИ проверкИ:
# print(ll==p) # => True, защото от математическа гледна точка ако а%3==0, то и (а**3)%3==0
# print(all(ab)) # функцията all(контейнер) проверява дали всички елементи на контейнера са True
#
# Вариант 4: филтиране на k, чрез 2 map-a и for:

p=list(map(l_4,L_1)) # a%3==0, списък от стойности True и False
print(len(k),len(L_1),len(p))
for i in range(len(p)):
    if p[i]==False:
        k.pop(i)
print(k)

# Вариант 5: Филтриране посредством чрез 2 map-a и речник и for:
k=list(map(l_3,L_1))
p=list(map(l_4,L_1))
dic=dict(zip(k,p))
for i in dic.items():
    if i[1]==False: dic.pop(i[0])
#     i връща двойката (ключ, стойност)
#     i[1] е стойността
#     i[0] е ключа
#     при .pop(ключ) - се изтрива ключа и неговата стойност, т.е. целия item
#
# Вариант 6: Филтриране на речника чрез filter:
k=list(map(l_3,L_1))
p=list(map(l_4,L_1))
dic=dict(zip(k,p))
dic_true=list(filter(l_4,dic))
print(dic_true)
# функцията за филтриране l_4 се изпълнява върху ключовете на речника
# резултатът е списък от ключовете
#
# # # Вариант 7:
# # # Филтриране на речника чрез кратката форма за for:
# # dic_true = [k for (k,v) in dic.items() if v==True]
# # # k е ключ, v е стойност за ключа, dic.items() са двойките ключ:стойност
# # print('dic:', dic_true)


