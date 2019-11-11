import Monster
import FireMonster
import WaterMonster
import GrassMonster


def display_info(monster):
   if isinstance(monster,FireMonster.FireMonster):
       print('%s is a Fire Type monster' %monster.get_name())
   elif isinstance(monster, WaterMonster.WaterMonster):
       print('{} is a Water Type monster'.format(monster.get_name()))
   else:
       print('{} is a Grass Type monster'.format(monster.get_name()))


m1 = FireMonster.FireMonster()
m2 = WaterMonster.WaterMonster()

display_info(m1)
display_info(m2)

