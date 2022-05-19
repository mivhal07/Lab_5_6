import pandas as pd

df = pd.read_excel("imiona.xlsx")

# 1
# for x in df:
#     rok = 2000
#     liczba = df[df.where(df.Rok == rok)].count(df.Imie)
#     print(liczba)
#     rok = +1

# 2
# print(df[df.Imie == 'MICHAŁ'])

# 3
# print(df.Liczba.count())

# 4
# suma = df[(df.Rok >= 2000) & (df.Rok <= 2005)]
# print(suma.Liczba.count())

# 5
# chlop = df[(df.Plec == 'M')]
# dziew = df[(df.Plec == 'K')]
# print('Chłopcy: ' + str(chlop.Liczba.count()))
# print('Dziewczęta: ' + str(dziew.Liczba.count()))

# 6
