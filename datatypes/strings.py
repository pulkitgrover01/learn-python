'''
test_var1 = 'check'
test_var2 = "check_again"
print(test_var1) 
print(test_var2)

#quote inside the strings

test_var3 = "lets 'check' again" 
print(test_var3)


test_var4 = '1 line: Hello \n2 Line: Bye \n3 Line: Comeback'
print(test_var4)

test_var5 = 'hello' + ' ' + 'play'
print(test_var5)


test_var6 = 'Heya' ' ' * 20
print(test_var6)


name = 'Aman'
age = 25
height = 5.7
zodic= 'Scorpian'
#bio_data = 'Hello {}, \nYou are {} year old and your height is {}.'.format(name,age,hight)
#print(bio_data)

bio_data_better = f'Hello {name}, \nYou are {age} year old and after 10 years, your age will be {age +10}. \nYour height is {height}.\nYour zodic sign is {zodic}.'
print(bio_data_better)
'''

#exercise
name = 'Ego'
hobby = 'Writing a programming language'
name_and_hobby = f'Hello, My name is {name}. \nMy hobby is {hobby}.'
print(name_and_hobby)