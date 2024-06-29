from FirePokemon import FirePokemon

class Charmulion(FirePokemon):
    MIN_LVL = 16
    MAX_LVL = 31
    MIN_ATTACK_POWER = 64
    MAX_ATTACK_POWER = 83
    MIN_DEF_POWER = 58
    MAX_DEF_POWER = 77
    MIN_HIT_POINTS = 58  # Corrected the range for Charmulion
    MAX_HIT_POINTS = 77

    def __init__(self, name, catch_rate, pokemon_type, lvl, hit_points, attack_power, def_power):
        super().__init__(name, catch_rate, pokemon_type)
        self.__validate_int_param(lvl, "lvl", self.MIN_LVL, self.MAX_LVL)
        self.__validate_int_param(attack_power, "attack power", self.MIN_ATTACK_POWER, self.MAX_ATTACK_POWER)
        self.__validate_int_param(def_power, "def power", self.MIN_DEF_POWER, self.MAX_DEF_POWER)
        self.__validate_int_param(hit_points, "hit points", self.MIN_HIT_POINTS, self.MAX_HIT_POINTS)

        self.__hit_points = int(hit_points)
        self.__attack_power = int(attack_power)
        self.__def_power = int(def_power)
        self.__lvl = int(lvl)
        self.__current_hit_points = int(hit_points)

    @staticmethod
    def __validate_int_param(value, name, min_value, max_value):
        if not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
        if value < min_value or value > max_value:
            raise ValueError(f"{name} must be between {min_value} and {max_value}")

    def __repr__(self):
        return f'The charmilion {self._name} of level {self.__lvl} with {self.__hit_points} HP'

    def get_hit_points(self):
        return self.__hit_points

    def get_defense_power(self):
        return self.__def_power

    def can_fight(self):
        return self.__hit_points >= self.__current_hit_points / 10

    def get_damage(self, other):
        eff = 2 if self.get_pokemon_type() in other.get_effective_against_me() else 0.5
        damage = (((self.__lvl * 2) / 5) + 2) * ((self.__attack_power / other.get_defense_power()) * eff)
        return damage

    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.__hit_points -= self.__current_hit_points / 10
            damage = self.get_damage(other)
            other.absorb(damage)

    def absorb(self, damage):
        self.__hit_points -= damage

    def level_up(self, lvl_gain):
        if 1 <= lvl_gain < 16:
            self.__lvl += lvl_gain
            if self.__lvl > 31:
                return None  # or handle further evolution if applicable
        return None

    def evolve(self):
        #need to add later when creating a charizard
        return None

