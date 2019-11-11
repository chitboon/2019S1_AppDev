class Monster:
    def __init__(self, name, health, attack, defence):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__defence = defence

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_attack(self):
        return self.__attack

    def set_attack(self, attack):
        self.__attack = attack

    def get_defence(self):
        return self.__defence

    def set_defence(self, defence):
        self.__defence = defence


    def health_damage(self, attack_value):
        damage = attack_value - self.__defence
        self.__health -= damage
        print('{} suffers {} damage, the health is {} now'.format(self.__name, damage, self.__health))
        return self.__health


