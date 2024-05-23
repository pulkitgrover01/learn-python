
class Monster:

    #attributes
    health = 90
    energy = 40

    #methods
#monster1 
    def m1properties(self, attack, speed):
        print('\nmonster1 has attacked.')
        print(f'monster1 health: {monster1.health}')
        monster1.energy -= 10
        print(f'monster1 energy: {monster1.energy}')
        print(f'damage was dealt: {attack}')
        print(f'monster1 speed: {speed}')
        
        
#monter2
    def m2properties(self, regain_power, death_attack):
        print(f'\nmonster2 health:: {monster2.health}')
        print(f'monster1 energy: {monster2.energy}')
        print(f'monster2 power regined: {regain_power}')
        print(f'final attack: {death_attack}')
        
#################################################
#monster1 
monster1 =  Monster()
monster1.m1properties(40,50)

#monster2
monster2 = Monster()
monster2.m2properties(5,50)

















