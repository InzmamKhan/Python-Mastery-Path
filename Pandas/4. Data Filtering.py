import pandas as pd

pokeData = pd.read_csv("C:\\Users\\khani\\OneDrive\\Desktop\\Practice Code\\PYTHON\\Databases\\Pandas\\Source File - Kanto_Region.csv")
print("My PokeData :")
print(pokeData)
print()



# --- Data Filtering ---

# 1. Filter for Pokemons with more than 1 evolution
filtered_pokeData = pokeData[pokeData['Evolutions'] > 1]
print("Pokemons with more than 1 evolution:")
print(filtered_pokeData)
print("-" * 30)

# 2. Filter using the .loc[] accessor for Fire type Pokemons and select 'Name' and 'Height' columns
fire_pokemon = pokeData.loc[pokeData['Type'] == 'Fire', ['Name', 'Height']]
print("\nFire type Pokemons and their heights:")
print(fire_pokemon)
print("-" * 30)

# 3. Filter with multiple conditions for Water type Pokemons with height > 0.5
water_and_tall_pokemon = pokeData[(pokeData['Type'] == 'Water') & (pokeData['Height'] > 0.5)]
print("\nWater type Pokemons taller than 0.5m:")
print(water_and_tall_pokemon)
print("-" * 30)