# Да се напише функция, която получава един входен параметър от тип списък,
# и връща като резултат нов списък, който се получава по следния начин:
# • проверява дали поредният елемент от входния списък е стринг:
#   ако е стринг, то в списъка-резултат към него се добавя в края текст от типа “: n”,
#   където n е броя на елементите на стринга от входния списък.
# • проверява дали поредният елемент от входния списък е число:
#   ако е число, то в списъка-резултат към него се добавя броя на
#   цифрите на числото от входния списък.
# • във всички останали случаи на елемент от входния списък, записваме в
#   списъка-резултат като пореден елемент числото -1.

vhod=[1,2,3,'1','2','3',10.5,[1,2,3]]

def func(my_list):
    L=[]
    for x in my_list:
        if isinstance(x,str):
            L.append(x+": "+str(len(x)))

        elif isinstance(x,int):
            L.append("%d: %d" %(x,len(str(x))))

        elif isinstance(x,float):
            L.append("%f: %d" %(x,len(str(x))-1))

        else:
            L.append(-1)
    return L

print(func(vhod))
