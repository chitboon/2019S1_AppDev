class Player:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def __str__(self):
        return '{}'.format(self.get_name())

class BasketBallPlayer(Player):
    positions = ['Guard', 'Center', 'Forward']
    def __init__(self, name):
        Player.__init__(self, name)
        self.__position = ''

    def get_position(self):
        return self.__position

    def set_position(self, position):
        if position in self.__class__.positions:
            self.__position = position
        else:
            print('Invalid position for basketball player')
    def __str__(self):
        return '{} playing as a {}'.format(self.get_name(), self.get_position())


basketball_team = []
basket_name = input('Enter the basketball team name: ')
for position in BasketBallPlayer.positions:
    name = input('Which player is playing as a '+ position)
    player = BasketBallPlayer(name)
    player.set_position(position)
    basketball_team.append(player)

print('Team', basket_name, 'consists of the following players:')
for player in basketball_team:
    print(player)





