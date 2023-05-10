from collections import Counter


def pokemons(pokemon_names: list[str]):
    pokemons_to_sell = 0

    pokemon_counter = Counter(pokemon_names)
    for v in pokemon_counter.values():
        pokemons_to_sell += v - 1

    return pokemons_to_sell


pokemon_names = [card.strip() for card in open(0)]
print(pokemons(pokemon_names))
