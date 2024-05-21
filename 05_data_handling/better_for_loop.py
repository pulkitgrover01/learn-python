
'''

inventory_names = ['plastic','metal','rubber','sheet','paper','glass']
inventory_numbers = [52,9,56,60,85,42]


for name, number in zip(inventory_names, inventory_numbers):
    print(f'{name}- in stock: {number}')




for index, name in enumerate(inventory_names):
    print(f'{index}: {name}')
    if index == len(inventory_names) // 2:
        print('half way done')

'''















