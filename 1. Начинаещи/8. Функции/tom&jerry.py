
КойКого=[]
def КойКогоИзяде(КОЙ='Том', КОГО='Джери'):
    # КОЙ и КОГО като формални ключови параметри, т.е. имат стойности по подразбиране
    global КойКого
    # КойКого e глобална променлива списък, която променяме в хода на изпълнение на функцията:
    КойКого.append((КОЙ,КОГО))
    # в този случай нямаме нужда нито от print(), нито от return

for i in range(5):
    x=input('КОЙ: ') # реален параметър x
    y=input('КОГО: ') # реален параметър y
    КойКогоИзяде(x,y) # подаваме реалните параметри като формални

for i in range(5):
    print(КойКого[i])