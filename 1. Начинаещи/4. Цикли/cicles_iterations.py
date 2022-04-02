S="Честита първа пролет и поредн сняг ;)!"
# for i in range(len(S)): #индиректен достъп до елементите, чрез индекси
#     str="%d : %s" %(i,S[i])
#     print(str)
#
# i=0
# for s in S: # директен достъп до елементите, БЕЗ индекси
#     str = "%d : %s" % (i, s)
#     print(str)
#     i=i+1
#
# for i,s in enumerate(S):
#     str = "%d : %s" % (i, s)
#     print(str)
#
# for item in enumerate(S):
#     print(item)
#     # item връща редица с два елемента: индекс и стойност елемента за конкретния индекс

# for: когато знаем броя на елементите,
# т.е. в 99% когато трябва да достъпим елемнти на някакъв контейнер:
# списъци, редици, множества и речници

# while: избягваме да го използваме ако можем да си послучим с for
# или не знаем колко са елементите, или имаме някакво специфично
# условие, което което динамично определя броя на циклите, т.е.
# когато не можем да кажем колко цикъла трябва да извъртим
# while="докато" <условие>-то е вярно

# i=0
# while i<len(S):
#     str = "%d : %s" % (i, S[i])
#     print(str)
#     # тук следва да организираме изход от цикъла, т.е. промяна на условието,
#     # така че в някакъв момент условието да не бъде повече вярно:
#     i=i+1

# зад–1: да се напише цикъл, чрез който да се създаде
# списък (или множество) от 10 различни случайни числа, в интервала [0;50]

from random import randint
# wariant 1

l=[]
n=10
i=0
br_rnd=0
while i<n:
    rnd=randint(0,50)
    if rnd not in l:
        l.append(rnd)
        i+=1
    # else: pass
    br_rnd+=1
print('Брой случайни числа: %d'%(br_rnd))
print(l)

# Вариант 2:
l=set() #празно множество
n=10
br_rnd=0
while len(l)<n:
    rnd=randint(0,50)
    l.add(rnd)
    br_rnd+=1
print('Брой случайни числа: %d'%(br_rnd))
print(l)

# итерация = поредното завъртане на цикъла
# break: прекъсва цикъла и излиза от него, независимо от местоположението си в самия цикъл,
# предава изпълнението на първата команда след цикъла
# continue: пропуска всички команди след себе си и преминава на следващата итерация от цикъла,
# pass: нещо като празна команда, нищо не прави

# Вариант 3
print('Вариант 3')
l=set()
br_rnd=0
n=10
for i in range(50):
    rnd = randint(0, 50)
    l.add(rnd)
    br_rnd += 1
    if len(l)==n: break
print('Брой случайни числа: %d'%(br_rnd))
print(l)

# Вариант 4
print('Вариант 4')
l=set()
br_rnd=0
n=10
for i in range(50):
    if len(l) == n: break
    else:
        rnd = randint(0, 50)
        l.add(rnd)
        br_rnd += 1

print('Брой случайни числа: %d'%(br_rnd))
print(l)

# zad. za continue
k=[]
for ll in l:
    if ll%3==0:continue
    else: k.append(ll)
    print(ll)
    # в този случай действието на continue се изразява в:
    # 1. пропускане на отпечатването на всички числа, които се делят точно на 3
    # 2. пропускане на клаузата else, т.е. else въобще не се проверява

# print(k)

# Алтернтивно решение:
# k=[]
# for ll in l:
#     if ll%3!=0:k.append(ll)
# print(k)

# редици: (), tuple
t=() # празна редица
t=tuple() # празна редица
t=(4,) # редица с един елемент
# има само два метода:
# .index(търсена стойност) => връща позицията на първото срещане
# .count(проверявана стойност) => връща броя на срещанията на проверяваната стойност
# достъп до елементите на редицата - по същия начин както при списъка
# ! не може да се променят стойностите на елементите в една редица

# пример с редици:
# да се на направи списък от редици, които имат следния формат:
# -първият елемент е винаги фак.номер
# -вторият елемент е име
# -третият елемент факултет

# ако разполагаме с 5 човека:
l1=[12,13,14,15,19]
l2=['Ани','Ива', 'Мима', 'Ники','Кирил']
l3=['ГГФ','ФМИ', 'ГГФ','ФЗФ','ГГФ']

# l=[]
# for i in range(len(l1)):
#     t=(l1[i],l2[i],l3[i])
#     l.append(t)
# print(l)

# модифициране на място:
n=len(l3)
i=n-1
while i>=0:
    if l3[i]!='ГГФ':
        l1.pop(i)
        l2.pop(i)
        l3.pop(i)
        i=i-1

print(l1)
print(l2)
print(l3)
l=[]
for i in range(len(l1)):
    t=(l1[i],l2[i],l3[i])
    l.append(t)
print(l)