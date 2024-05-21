
'''
capacity = 10

def test_fuction():
    capacity = 2
    print(capacity)

def test_function1():
    capacity = 20
    print(capacity)

test_fuction()
test_function1() 

'''



'''
############ Global method #############

capacity = 20

def test_function2():
    global capacity
    capacity += 5
    print(capacity)
 
test_function2()

############## Without Global Method #########

capacity = 20

def test_function2(capacity):
    
    capacity += 5
    print(capacity)

test_function2(capacity)
 
#print(test_function2())



######## Return the value to Global#########

a = 5

def test_funct(a):
    a +=4
    return a

result = test_funct(a)
print(result)

#print(test_funct(a))



multiplier = 5
has_calculated = False

def multiply_calculator(number):
    global has_calculated
    has_calculated = True
    result = multiplier * number
    return result



result = multiply_calculator(6)
print(result)
print(has_calculated)

'''


divider = 50
its_done = True

def solver(number):
    result = divider / number
    global its_done
    its_done = False
    return result

res = solver(5)
print(int(res))
print(its_done)

















