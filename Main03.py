import pandas as pd

df = pd.read_csv("zamowienia.csv")

# 1
# print(df.drop_duplicates(subset=['Sprzedawca'], keep='first').tolist())

# 2
# print(df.groupby(['Utarg']).tail)

# 3
# print(df[df.Sprzedawca].count(df.Zamowienia))

# 4
# print(df[df.Kraj].count([df.Zamowienia]))

# 5
# print(df[(df.Rok == "2005") & (df.Kraj == "Polska")])

# 6
# print((df[(df.Rok == "2004")].sum()) / (df[(df.Rok == "2004")].count()))

# 7
# dane2004 = df[(df.Rok == '2004')].to_csv('zamówienia_2004.csv')
# dane2005 = df[(df.Rok == '2005')].to_csv('zamówienia_2005.csv')
