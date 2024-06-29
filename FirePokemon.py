# File: FirePokemon.py
from abc import ABC, abstractmethod
from Pokemon import Pokemon

class FirePokemon(Pokemon):
    def __init__(self, name, catch_rate, pokemon_type):
        super().__init__(name, catch_rate)
        self.__effective_against_me = ["Water"]
        self.__effective_against_others = []
        if pokemon_type != 'Fire':
            raise ValueError("For a fire pokemon, type must be Fire")
        self.__type = pokemon_type

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def absorb(self, damage):
        pass

    @abstractmethod
    def attack(self, other):
        pass

    @abstractmethod
    def can_fight(self):
        pass

    @abstractmethod
    def get_damage(self, other):
        pass

    @abstractmethod
    def get_defense_power(self):
        pass

    @abstractmethod
    def get_hit_points(self):
        pass

    def get_pokemon_type(self):
        return self.__type

    @abstractmethod
    def level_up(self):
        pass

    def get_effective_against_me(self):
        return self.__effective_against_me

    def get_effective_against_others(self):
        return self.__effective_against_others
