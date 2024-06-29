from FirePokemon import FirePokemon
from Charmander import Charmander
from Charmilion import Charmulion

if __name__ == "__main__":
    charmy = Charmander("charmy", 41, "Fire", 6, 50, 54, 51)
    charmilious = Charmander("charmilious", 42, "Fire", 13, 45, 55, 47)

    # Display initial states
    print(charmy)  # The Charmander charmy of level 6 with 50 HP
    print(charmilious)  # The Charmander charmilious of level 13 with 45 HP

    # Charmilious gets damage from charmy
    damage = charmilious.get_damage(charmy)
    print(f"Damage: {damage}")

    # Charmilious attacks charmy
    charmilious.attack(charmy)

    # Display states after the attack
    print(charmy)  # The Charmander charmy of level 6 with 47 HP
    print(charmilious)  # The Charmander charmilious of level 13 with 41 HP

    # Level up charmy
    evolved_charmy = charmy.level_up(5)
    if evolved_charmy is not None:
        charmy = evolved_charmy

    # Display state after leveling up
    print(charmy)  # The Charmander charmy of level 11 with 47 HP

    # Level up charmy again
    evolved_charmy = charmy.level_up(5)
    if evolved_charmy is not None:
        charmy = evolved_charmy

    # Display final state
    print(charmy)  # The Charmeleon charmy of level 16 with 66 HP
