import requests
import random

pikachu = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu').json()
pikachu_abilities = []

squirtle = requests.get('https://pokeapi.co/api/v2/pokemon/squirtle').json()
squirtle_abilities = []

charmander = requests.get('https://pokeapi.co/api/v2/pokemon/charmander').json()
charmander_abilities = []

bulbasaur = requests.get('https://pokeapi.co/api/v2/pokemon/bulbasaur').json()
bulbasaur_abilities = []


for a in pikachu["abilities"]:
    pikachu_abilities.append(a["ability"]["name"])

for a in squirtle["abilities"]:
    squirtle_abilities.append(a["ability"]["name"])

for a in charmander["abilities"]:
    charmander_abilities.append(a["ability"]["name"])

for a in bulbasaur["abilities"]:
    bulbasaur_abilities.append(a["ability"]["name"])


list_of_pokemons = ["bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard", "squirtle", "wartotle", "blastoise", "caterpie", "metapod", "butterfree", "weedle", "kakuna", "beedrill", "pidgey", "pidgeotto", "pidgeot", "rattata", "raticate", "spearow", "fearow", "ekans", "arbok", "pikachu", "raichu", "sandshrew", "sandslash", "nidoran-f", "nidorina", "nidoqueen", "nidoran-m", "nidorino", "nidoking"]
pokemon_randomly = []


def random_pokemon(pokemon):
    pokemon_randomly.clear()
    pokemon_randomly_requested = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
    posicion_pokemon = '%03d' % (list_of_pokemons.index(pokemon) + 1)
    image_randomly = f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{posicion_pokemon}.png"
    for a in pokemon_randomly_requested["abilities"]:
        pokemon_randomly.append(a["ability"]["name"])
    return image_randomly


random_img = random_pokemon(random.choice(list_of_pokemons))
