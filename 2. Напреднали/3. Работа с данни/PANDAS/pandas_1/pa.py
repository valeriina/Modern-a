import pandas as pd
import numpy as np

pth='/Users/valerina/PycharmProjects/1386/PANDAS/'
fn='invoice_2019_5.xls'
fo='invoice_2019_5_out.xls'
sn='details_1'
df=pd.read_excel(pth+fn,sn)
# df=pd.read_excel(fn,sn)

# Извеждане на броя на редовете и колоните
n=df.shape
print(n)

# показва типа на данните от всяка колона
dts=df.dtypes
print(dts)

# Извеждане имената на колоните, достъпни са както списъците
a=df.columns
df.columns=[i for i in range(10)]
print(df.columns)
# връща всички редове (записи, но показва само колоните, които са посочени в списъка
slice_1=df[a[0:3]]

# показва уникалните стойности за колоната, и коя уникална стойност колко пъти се среща
df[a[0]].value_counts()

# първите няколко записа от данните, по подразбиране => са първите 5 записа, но може да укажем и друго число
h=df.head()

# последните 5 записа от данните
df.tail(5)

# Кратка статистика за всички данни
df.describe()

# Сортиране чрез използване на измеренията:редове и колони:
# axis=0 е по редове
# axis=1 е по колони
df.sort_index(axis=1, ascending=False, inplace=False)
# inplace=True запазва сортирането в df
# inplace=False само показва как ще изглежда сортирането в df, False е стойността по подразбиране

# Сортиране по стойности чрез използване на името на дадена колона
df.sort_values(by=a[1], inplace=False) # по дата

# Селекция (филтриране)
# .at - чрез него се задават точни позиции и работи по-бързо от останалите
# .iat - селекция по позиция
# .loc - селекция по етикет (име на колона)
# .iloc - селекция по позиция

# Извежда конкретна колона
df['Избран номер']

# Извежда първите 10 реда
df[:10]

# само с df и някакъв слайс можем да изведем информация
# -или САМО за определени колони и всички редове,
# -или само за определени редове и всички колони

# Извеждане на конкретни изброени редове, за всички колони
df.loc[[1,5,7],:]

# Извеждане на конкретни изброени редове, и конкретни изброени колони
df.loc[[1,5,7],[a[0],a[1]]]

# При използването на .loc номерата на редове се подават или под формата на списък или на итератор (напр. с range)

# работим само с индекси
df.iloc[3] # връща всички колони от третия ред

df.iloc[[1,5,7],:2]
df.iloc[[1,5,7],[0,1]]
#
# "всички" се означава с двуеточние :
# двуеточието може и да се пропусне, когато искаме да изведем всички колони !!!

df.iloc[[1,5,7],:]
df.iloc[1,2]
df.iat[1,2]

# Съставяне на условия за филтриране на данните, т.нар. WHERE условия
cond=df.iloc[:,8]>0
filtered_data=df[cond]
col=[0,1,3,4,8]
filtered_data.iloc[:,col]

# Филтриране чрез isin(): isin() е метод. В скобите се указват конкретни стойности,
# по които искаме да филтрираме и които се съдържат в избраната колона, спрямо която
# пускаме метода. Например: Да се изведат всички обаждания към номер 359898263883.
# В нашия dataframe колоната с набраните номера е от стрингове.
df2=df[df[a[3]].isin(['359898263883'])]

# Промяна или задаване на нови стойности: по етикет (име на колона: at, loc), по позиция (чрез номер на ред и колона: iloc, iat)
# Задача: Да се променят всички стойности от набран номер (колона с индекс 3), които имат стойност 00359899142513, на 359899142513
d13=df[df[a[3]].isin(['00359899142513'])].copy() # общо 40 записа
# използваме .copy() метода, за да избягаме от конфликт с промяната на данните
# d13 ще върне тази част данните, в които избраният номер е 00359899142513
d13.iloc[:,3]='359899142513'
# В момента промяната е изолирана, т.к. никъде не сме променили/присвоили резултата на основната променлива df.
# за да стане това трябва да изпълним:
df[df[a[3]].isin(['00359899142513'])]=d13

# или: DA go porwerq !!!!!!!!!!!!!!!!!!!!!
# cond=df[a[3]].isin(['00359899142513']).copy()
# dfc=df[cond]
# df[cond]=dfc.iloc[:,3]='359899142513'
# и проверка чрез: df[a[3]].value_counts().head()

# Създаване на копие на dataframe с различно id:
dfna=df.reindex()

# Обработка на липсващи данни (имат стойност NaN) чрез методи:
#   -премахване на записи (редове) чрез dropna(how='any')
dfna=df.reindex()
dfna.head()
dfna1=dfna.dropna(1) # ще премахне колоните, в които има стойности NaN
dfna.dropna(0) # ще премахне редовете, в които има стойности NaN, и ако има колона, в която всички стойности са такива, то ще получим празно множество от данни
dfna.dropna() # същото като dropna(0)
dfna.head()
# Кои са премахнатите колони
b=dfna1.columns
dropped_cols=set(a)-set(b)
#
#
#   -запълване на записи, съдържащи NaN ст-ти чрез: fillna(value=...)
dfna=df.reindex()
dfna.head()
dfna.fillna(value='#')
dfna.head()

#   -проверка и запълване чрез булеви стойности: isna(dataframe)
dfna=df.reindex()
dfna.head()
pd.isna(dfna)
dfna.head()
#    Задача: да се променят всички стойности NaN с нули:
# колони 5 и 9 съдържат стойности NaN
cond=dfna[a[5]].isna()
d14=dfna[cond].copy()
d14.iloc[:,5]=0
dfna[cond]=d14

cond=dfna[a[9]].isna() # 1. Създаване на условие, по които търсим в конкретна колона
d14=dfna[cond].copy() # 2. Филтриране по условието, като създаме нов dataframe обикновено с по-малко редове от първоначалния
d14.iloc[:,9]=0 # 3. В новия дейтафрейм заменяме стойностите със желаната
dfna[cond]=d14 # 4. На филтрирания оригинален дейтафрейм присвояваме този с модифицираните стойности от т.3
# dfna[cond]=0 # ne raboti !!!
dfna.head()

# Статистическа обработка на данните: не се взимат предвид NaN стойностите
# Когато се пресмятат статистически показатели, приложими само за чила, Pandas първо проверява за кои данни
# изчисленията са приложими и пресмята показателите само за тях !
dfna=df.reindex()
# Всички изчисления да се направят върху данните, за които в колона стойност имаме число различно от нула

# - пресмятане на средно:
# --по колони: dataframe_name.mean() или dataframe_name.mean(0)
# --по редове: dataframe_name.mean(1)
#
# # - пресмятане на максимум и минимум:
# # --по колони: dataframe_name.max() или dataframe_name.max(0)
# # --по редове: dataframe_name.max(1)
# # --по колони: dataframe_name.min() или dataframe_name.min(0)
# # --по редове: dataframe_name.min(1)
#
# # - пресмятане на стандартно отклонение:
# # --по колони: dataframe_name.std() или dataframe_name.std(0)
# # --по редове: dataframe_name.std(1)
#
cond=dfna.iloc[:,8]>0
filtered_data=dfna[cond].iloc[:,[0,1,3,8]]
me=round(filtered_data.iloc[:,3].mean(),2)
mi=round(filtered_data.iloc[:,3].min(),2)
ma=round(filtered_data.iloc[:,3].max(),2)
st=round(filtered_data.iloc[:,3].std(),2)
#
# Масово прилагане на други функции върху данните чрез APPLY
# В скобите след apply може да стои и ламбда функция
filtered_data.apply(np.sum)

# Генериране на хистограми (разпределение на данните по бройки)
# Правихме го чрез метода .value_counts()


# Обединение на dataframe-и
# pd.concat([списък от dataframe-и]), залепва един ПОД друг
# pd.concat([списък от dataframe-и],0), залепва един ПОД друг
# pd.concat([списък от dataframe-и],1), залепва един ДО друг
d1=filtered_data.iloc[:,0:2]
d2=filtered_data.iloc[:,3]
d=pd.concat([d1,d2],1)
d3=filtered_data.iloc[:10]
d4=filtered_data.iloc[10:]
d=pd.concat([d4,d3])

# Промяна на имена на колони:
# 1. ИЗвличаме имената на колоните и превръщаме в списък
# 2. Модифицираме списъка
# 3. Присвояваме списъка на имената на колоните
ДДС=round(filtered_data.iloc[:,3]*0.2,2)
Стойност_с_ДДС_1=round(filtered_data.iloc[:,3]*1.2,2)
Стойност_с_ДДС_2=filtered_data.iloc[:,3]+ДДС
new_data=pd.concat([filtered_data,ДДС, Стойност_с_ДДС_1,Стойност_с_ДДС_2],1)
new_cols=new_data.columns
new_cols=list(new_cols)
new_cols[4]="ДДС"
new_cols[5]="Стойност–с-ДДС-1"
new_cols[6]="Стойност–с-ДДС-2"
new_data.columns=new_cols
print(new_data.iloc[1,:])

# Групиране на данни и обобщени справки
# dataframe_name.groupby([писък от имена на колони]).агрегатна функция
# агрегатни функции са всички статистики, напр.: min, max, sum и т.н.
dfs=df.iloc[:,[0,3,4,8]]
dfs.columns=['a','b','c','d']
k=dfs.groupby(['a','c']).sum()

# Pivot таблици
# pd.pivot_table() връща дейтафрейм, който може да бъде запазен
pivot_1=pd.pivot_table(dfs, values='d',index=['a','c'])
pivot_2=pd.pivot_table(dfs, values='d',index=['a'],columns=['c'])

# Записване на данните във файл

sn= 'филтрирани_данни'
# ExcelWriter 1
with pd.ExcelWriter(pth+fo) as writer:
    filtered_data.to_excel(pth+fo,sheet_name=sn,index=False)

# ExcelWriter 2: реално презаписва файла, ако на двете места е един и същ
with pd.ExcelWriter(pth+fo) as writer:
    # всеки един дейтафрем се добавя като отделен лист в новия файл
    pivot_1.to_excel(writer, sheet_name="normal_pivot")
    pivot_2.to_excel(writer, sheet_name="cross_pivot")
    k.to_excel(writer, sheet_name="group_by_example")
