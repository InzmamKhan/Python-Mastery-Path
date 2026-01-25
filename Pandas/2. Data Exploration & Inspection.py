import pandas as pd
pokeData = pd.read_csv("C:\\Users\\khani\\OneDrive\\Desktop\\Practice Code\\PYTHON\\Databases\\Pandas\\Source File - Kanto_Region.csv")
print("My PokeData :")
print(pokeData)
print()
  


  
# --- Data Exploration and Inspection ---

print("Top 5 rows:")
print(pokeData.head())
print("-" * 30)

print("Bottom 5 rows:")
print(pokeData.tail())
print("-" * 30)

print("DataFrame Info:")
pokeData.info()
print("-" * 30)

print("Descriptive Statistics:")
print(pokeData.describe())
print("-" * 30)

print("DataFrame Shape (rows, columns):")
print(pokeData.shape)
print("-" * 30)

print("Columns and Data Types:")
print(pokeData.dtypes)
print("-" * 30)

if 'Region' in pokeData.columns:
    print("Unique values in 'Region' column:")
    print(pokeData['Region'].unique())
else:
    print("'Region' column not found.")
print("-" * 30)

if 'Type' in pokeData.columns:
    print("Value Counts for 'Type' column:")
    print(pokeData['Type'].value_counts())
else:
    print("'Type' column not found.")
print("-" * 30)