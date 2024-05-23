
#Map function = Changes values with a function inside of a  iterable
my_list = [4,2,6,1,8,5,7]


'''
def power_function(num):
    return num **2
print(list(map(power_function, my_list)))

print(list(map(lambda num: num**2, my_list)))


#Filter = finter our values for a condition

def get_below4(num):
    if num < 6:
        return True
    else:
        False

#Map
print(list(sorted(filter(get_below4, my_list))))
#without Map
print(list(sorted(filter(lambda num: num < 6, my_list))))

'''
#finter
print(sorted([num ** 2 for num in my_list]))
#Without filter
print(sorted([num for num in my_list if num < 6]))







