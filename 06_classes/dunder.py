
class Monster:

######## Dunder Method ##########
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def __len__(self):
        return self.health
    
    def __abs__(self):
        return 'I have returend the value'
    
    def __call__(self):
        print ('The monster was called')

    def __add__(self, other):
        return self.health + other
    
    def __str__(self):
        return (f'our Monster1 has health {self.health}: and energy: {self.energy}')
    #############################
   

    #methods
#monster1 
    def m1properties(self, attack, speed):
        print('\nmonster1 has attacked.')
        print(f'monster1 health: {self.health}')
        #self.energy -= 10
        print(f'monster1 energy: {self.energy}')
        print(f'damage was dealt: {attack}')
        print(f'monster1 speed: {speed}')
        
        
#monter2
    def m2properties(self, regain_power, death_attack):
        print(f'\nmonster2 health:: {self.health}')
        print(f'monster1 energy: {self.energy}')
        print(f'monster2 power regined: {regain_power}')
        print(f'final attack: {death_attack}')
        
#################################################
#monster1 
monster1 =  Monster(health=100,energy=50)
monster1.m1properties(40,50)
print(len(monster1))
print(abs(monster1))
monster1()
print(monster1 + 20)
print(str(monster1))

#monster2
monster2 = Monster(health=50,energy=25)
monster2.m2properties(5,50)












