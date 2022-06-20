from flask import Flask, render_template
from infopokemons import *

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html", pikachu_ab=pikachu_abilities, squirtle_ab=squirtle_abilities, charmander_ab=charmander_abilities, bulbasaur_ab=bulbasaur_abilities, random_img=random_pokemon(random.choice(list_of_pokemons)), pokemon_randomly=pokemon_randomly)



if __name__ == "__main__":
    app.run(debug=True)