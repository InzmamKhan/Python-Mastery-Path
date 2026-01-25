import pandas as pd
pokeData = pd.read_csv("C:\\Users\\khani\\OneDrive\\Desktop\\Practice Code\\PYTHON\\Databases\\Pandas\\Source File - Kanto_Region.csv")
print("My PokeData :")
print(pokeData)
print()




# -- Data Description --

print("My PokeData : ")
print(pokeData)
print()

print("Descriptive Statistics:")
print(pokeData.describe())
print()

print("Minimum Values:")
print(pokeData.min(numeric_only=True))
print()

print("Maximum Values:")
print(pokeData.max(numeric_only=True))
print()

print("Mean Values:")
print(pokeData.mean(numeric_only=True))
print()

print("Count of Values:")
print(pokeData.count())