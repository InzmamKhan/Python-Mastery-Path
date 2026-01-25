import pandas as pd
pokeData = pd.read_csv("Source File - Kanto_Region.csv")
print("My PokeData :")
print(pokeData)
print()




# -------------------- Data Grouping --------------------
# Use the `groupby()` method to group the data by 'Type' and calculate the
# average 'Height' and 'Weight' for each Pokémon type.
grouped_data = pokeData.groupby('Type')[['Height', 'Weight']].mean()

# Print the resulting grouped data
print("Grouped Data (Average Height and Weight per Type):")
print(grouped_data)

print("-" * 50)

# -------------------- Making a Pivot Table --------------------
# Use the `pivot_table()` method to create a table that summarizes the data.
# The `index` is 'Type', the `columns` are 'Evolutions', and the `values`
# are the 'Height', with the `aggfunc` (aggregation function) set to `mean`.
pivot_table = pokeData.pivot_table(
    index='Type',
    columns='Evolutions',
    values='Height',
    aggfunc='mean'
)

# Print the resulting pivot table
print("\nPivot Table (Average Height per Type and Evolution Count):")
print(pivot_table)