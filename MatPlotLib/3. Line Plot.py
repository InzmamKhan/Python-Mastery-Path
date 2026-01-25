import matplotlib.pyplot as plt

pokemon = ['Pikachu', 'Charizard', 'Bulbasaur', 'Squirtle', 'Jigglypuff', 'Meowth', 'Psyduck', 'Snorlax', 'Eevee', 'Gengar']
values = [0.4, 1.7, 0.7, 0.5, 0.5, 0.4, 0.8, 2.1, 0.3, 1.5]

# Line Plot
plt.plot(pokemon, values)
plt.xlabel('Pokemon')
plt.xticks(rotation=45)
plt.ylabel('Heights')
plt.title('Line Graph of Pokemon-Height')
plt.show()