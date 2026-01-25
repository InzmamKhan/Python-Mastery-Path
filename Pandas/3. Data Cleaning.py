import pandas as pd
pokeData = pd.read_csv("C:\\Users\\khani\\OneDrive\\Desktop\\Practice Code\\PYTHON\\Databases\\Pandas\\Source File - Kanto_Region.csv")
print("My PokeData :")
print(pokeData)
print()



# === Data Cleaning and Manipulation Operations ===

# 1. Renaming a column for clarity
# The '.rename()' method is used with a dictionary mapping old column names to new ones.
pokeData = pokeData.rename(columns={'Evolutions': 'Evolution_Count'})

# 2. Removing a column
# The '.drop()' method is used with the column name and 'axis=1' to specify it's a column.
pokeData = pokeData.drop(columns=['Weight'])

# 3. Handling missing data (if any)
# The '.fillna()' method is used to replace any missing 'NaN' values in the 'Height' column with the mean height.
# While the provided data has no missing values, this is a standard and crucial step.
mean_height = pokeData['Height'].mean()
pokeData['Height'] = pokeData['Height'].fillna(mean_height)

# Display the cleaned and manipulated DataFrame
print("Cleaned and Manipulated PokeData:")
print(pokeData)