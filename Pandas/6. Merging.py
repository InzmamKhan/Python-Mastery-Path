import pandas as pd
johto_data = pd.read_csv("C:\\Users\\khani\\OneDrive\\Desktop\\Practice Code\\PYTHON\\Databases\\Pandas\\Source File - Johto_Region.csv")
print("My PokeData for Johto Region:")
print(johto_data)
print()

hoenn_data = pd.read_csv("C:\\Users\\khani\\OneDrive\\Desktop\\Practice Code\\PYTHON\\Databases\\Pandas\\Source File - Hoenn_Region.csv")
print("My PokeData for Johto Region:")
print(hoenn_data)
print()

kanto_data = pd.read_csv("C:\\Users\\khani\\OneDrive\\Desktop\\Practice Code\\PYTHON\\Databases\\Pandas\\Source File - Kanto_Region.csv")
print("My PokeData for Johto Region:")
print(kanto_data)
print()




# -------------------- Merging DataFrames --------------------

# 1. Merging and Joining

# Inner Join
inner_join_df = pd.merge(hoenn_data, johto_data, on='Name', how='inner')
print("Inner Join (only common names):")
print(inner_join_df)
print("\n" + "="*50 + "\n")

# Outer Join
outer_join_df = pd.merge(hoenn_data, johto_data, on='Name', how='outer')
print("Outer Join (all names):")
print(outer_join_df)
print("\n" + "="*50 + "\n")

# Right Join
right_join_df = pd.merge(hoenn_data, johto_data, on='Name', how='right')
print("Right Join (all names from Johto_data):")
print(right_join_df)
print("\n" + "="*50 + "\n")

# Left Join
left_join_df = pd.merge(hoenn_data, johto_data, on='Name', how='left')
print("Left Join (all names from Hoenn_data):")
print(left_join_df)
print("\n" + "="*50 + "\n")



# 2. Concatenation
all_data = pd.concat([kanto_data, johto_data, hoenn_data], ignore_index=True)
print("Concatenation (all dataframes stacked):")
print(all_data)