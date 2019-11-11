import Monster

class GrassMonster(Monster.Monster):
   def __init__(self):
       super().__init__(name='grasshopper', health=20, attack=5, defence=3)
