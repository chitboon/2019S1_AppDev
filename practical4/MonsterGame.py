import Monster
import FireMonster
import WaterMonster
import GrassMonster
import random


class MonsterGame:
   def __init__(self):
       self.player_monster = self.choose_monster()
       self.computer_monster = self.generate_monster()

   def generate_monster(self):
       choice = random.randint(0,2)
       if choice == 0:
            return FireMonster.FireMonster()
       elif choice == 1:
            return WaterMonster.WaterMonster()
       else:
            return GrassMonster.GrassMonster()

   def choose_monster(self):
       type = input('Choose your monster (F, W or G): ')

       if type.upper() == 'F':
           return FireMonster.FireMonster()
       elif type.upper() == 'W':
           return WaterMonster.WaterMonster()
       elif type.upper() == 'G':
           return GrassMonster.GrassMonster()

   def play(self):
       while True:
           health = self.computer_monster.health_damage(self.player_monster.get_attack())
           if health <= 0:
               print('You won!')
               break
           health = self.player_monster.health_damage(self.computer_monster.get_attack())
           if health <= 0:
               print('You lost!')
               break


ma = MonsterGame()
print(ma.player_monster.get_name())
print(ma.computer_monster.get_name())
ma.play()