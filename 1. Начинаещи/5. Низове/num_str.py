# Работа с числа и символни низове
# имаме едно реално число, и трябва да вземем от него само дробната му част

# int()-превръща реално число или символен низ от числа в цяло число
# float() - превръща цяло число или символен низ от числа в реално число
# input() - въвеждане от клавиатурата, връща винаги символен низ
# round(число-обикновено е реално число, брой знака след десетичната запетая)

# Дадено е едно реално число, да се отпечата числото и неговата дробна част под формата на цяло число
# a=4.56
a=input('Въведете реално число: ')
st=a # st е 'str'
a=float(st) # а е 'float'

# или това е същото като:
# a=input('Въведете реално число: ')
# a=float(a)

# или:
# a=float(input('Въведете реално число: '))

print(type(a))
print(a)
#
# a=round(a,2)
# print('След закръглянето до втория знак става: '+str(a))
# b=int(a) #т.е. b  е цялата част от реалното число (напр. int(3.75) ще върне 3
# d=(a-b)*100 #дробната час, умножена по 100 (напр. (3.75-3.00)*100 ще върне 75.0
# c=int(round(d,2)) # т.е. връща 75, не прави разлика между 07=>7 и 70=>70
# # round(d,2) го използваме, за да закръглим до втората цифра, защото в противен случай получаваме дълга дробна част
#
# print(c)
#
# #----------------------------------------------
# вариант, когато използваме стрингове
for i in range(len(st)):
    # len(st) - връща броя на символите в текстовата променлива или броя на елементите в някакъв контейнер (списъци,множества,редици,речници)
    # range(start=0,stop, step=1) - общия формат
    # от start+step създава поредни цели числа, като последното число=stop-1
    # пример: range(1,5,1) е същия като range(1,5) и създава поредицата от числа: 1,2,3,4
    # пример: range(0,5,1) е същия като range(5) и създава поредицата от числа: 0,1,2,3,4
    # т.е. ако st=3.701 => len(st)=5 => range(5) => 0,1,2,3,4
    # i е индекса на елементите и се променя от нула до броя на елементите на символния низ st -1
      if st[i]=='.':
          # ако намерим символа точка, тогава отпечатваме всички останали символи след индекса на намерената точка до края

          print(int(st[i+1::]))
          break #и прекъсваме изпълнението на цикъла, защото вече сме намерили точката

# list: списък []
# set: множество {}
# tuple: редица ()
# dictionary: речник {key_1: val_1,key_2: val_2}
# достъпът до елементите ВИНАГИ става чре []
# функция или метод, ВИНАГА се използват с ()

