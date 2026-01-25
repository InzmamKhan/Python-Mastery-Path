import matplotlib.pyplot as plt

pokemon = ['Pikachu', 'Charizard', 'Bulbasaur', 'Squirtle', 'Jigglypuff', 'Meowth', 'Psyduck', 'Snorlax', 'Eevee', 'Gengar']
values = [0.4, 1.7, 0.7, 0.5, 0.5, 0.4, 0.8, 2.1, 0.3, 1.5]

# Assign specific colors to each Pokémon
colors = {
    'Pikachu': 'yellow',
    'Charizard': 'orange',
    'Bulbasaur': 'green',
    'Squirtle': 'blue',
    'Jigglypuff': 'pink',
    'Meowth': 'purple',
    'Psyduck': 'cyan',
    'Snorlax': 'brown',
    'Eevee': 'magenta',
    'Gengar': 'red'
}

# Map the colors to the Pokémon
bar_colors = [colors[poke] for poke in pokemon]

# Histogram
plt.hist(values, bins=5, color='skyblue')
plt.xlabel('Pokemons')
plt.ylabel('Heights')
plt.title('Historgram of Pokemon-Height')
plt.show()