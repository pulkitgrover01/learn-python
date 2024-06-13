#by default python takes the inputs in string. to add the integers you have to use int or float. 3. is the example

1.
#you hvae to ender your name in the terminal
# name = input('Enter_your_name:')
# print('Hello', name)


2.
#To check the type of the input
# val = int(input('Enter_your_name:'))
# print(type(val), val)



3.
# name = input('Enter your name:')
# age = int(input('Your age:'))
# marks = float(input('your scored:'))

# print('Hello', name)
# print('Your age is:', age)
# print('You scored:', marks)

############################################ Exercies ###############################
4.
# val1 = int(input('Enter your value1:'))
# val2 = int(input('Enter your value2:'))

# print('Here is the sum of both:', val1+val2)

5.
# square = float(input('Enter one side of the squares:'))
# print('Here is the size of the square:', square * square)
# ################### or ###################
# print('Here is the size of the square:', square **2)


6.
# First = float(input('First Value:'))
# Second = float(input('Second Value:'))

# print('Here is the average', (First+Second)/2)

7.
# first = int(input('First value:'))
# second = int(input('second value:'))

# print('Result is in boolean value:',first >= second)


# if first > second:
#     print('Best')
# else:
#     print('good')


# print('Best' if first > second else 'food')




#exercise again
#1
# math = int(input('you scored in maths: '))
# science = int(input('you scored in science: '))

# print('total score: ', math+science)

#2
# area = int(input('your one side of area is: '))

# print('total area: ', area*area)

#3
# value1 = float(input('enter your first value: '))
# value2 = float(input('enter your second value: '))

# print('Your average result: ', (value1 + value2)/2)

#4
# a = int(input('first value: '))
# b = int(input('secont value: '))

# print('a is grater the b:' , a >= b)


######################################## Lecture 1

# a = float(input())
# b = float(input())
# print(int(a+b))


# a = 4
# side_of_square = a * a 
# print(side_of_square)



# a = int(input())
# b = int(input())

# ave = (a+b)/2
# print(ave)


# a = int(input())
# b = int(input())

# print(True if a >= b else False)



######################################## Lecture 2


# name = input()
# print(len(name))


# name = "naman is going to meet raman"

# count = 0
# find = "g"

# for char in name:
#     if char == find:
#         count += 1


# print(count)


# a = int(input())

# if a%2 == 0:
#     print("Even number")

# else:
#     print("odd number")


# def is_even(number):
#     return number%2 == 0

# number = 4

# if is_even(number):
#     print("even")

# else:
#     print("odd")


# def find_greatest_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3



# greatest = find_greatest_num(2,5,3)

# print(greatest)




# num1 = 2
# num2 = 5
# num3 = 3

# if num1 >= num2 and num1 >= num3:
#     print(num1)

# elif num2 >= num1 and num2 >= num3:
#     print(num2)

# else:
#     print(num3)



# def is_mult_of(number):
#     return number % 7 == 0

# number = 2

# if is_mult_of(number):
#     print("Yes")

# else:
#     print("No")



######################################## Lecture 3



# movie = []
# a = "Khan"
# b = "ram"
# c = "shan"

# movie.append(a)
# movie.append(b)
# movie.append(c)

# print(movie)



# list1 = [1,2,3,4,5,61]


# copy_list1 = list1.copy()
# copy_list1.reverse()

# if copy_list1 == list1:
#     print("Plendropm")

# else:
#     print("nonp")


# print(copy_list1)



# alist =("C","D","A","A","B","B","A")
# find = "B"

# output = alist.count(find)
# print(output)


# listss = [store for store in alist]
# listss.sort()
# print(listss)




######################################## Lecture 4



# dicti = {"car": "a small animal", "Table": ["a piece of furniture","list of facts and figures"]}
# print(dicti)



# lest = {"python", "java","c++","python","javascript","java","python","java","c++","c"}

# print(lest)
# print(len(lest))


# marks = {}
# a = 75
# b = 89
# c = 95


# marks.update({"phy" : a})
# marks.update({"chem" : b})
# marks.update({"math" : c})

# print(marks)

# sets = {(9, 9.0)}

# print(sets)






# for x in range(100):
#     print(x)
#     x += 1

# print(x)




# count = 0
# while count < 100:
#     print(count)
#     count += 1





# count = 100
# while count >= 0:
#     print(count)
#     count -= 1


# multinumer = 7
# counter = 1

# while counter <= 10:
#     check = counter * multinumer
#     print(check)
# #     counter += 1

# bucket = [1,4,9,16,25,36,49,64,81,100]


# for i in bucket:
#     print(i)
   

# idx = 0
# while idx < len(bucket):
#     print(bucket[idx])
#     idx += 1




# find = 16
# idx = 0
# while idx < len(bucket):
#     if bucket[idx] == find:
#         print(idx)
#     idx += 1



# for i in range(100,0,-1):
#     print(i)


# val_INR = 83

# def curr_convet(val_USD):
#     converter = val_INR * val_USD
#     print(f"USD: {val_USD} = INR: {converter}")


# curr_convet(4)


# def natural_number(n):
#     if n == 0:
#         return 0
    
#     else:
#         return n + natural_number(n-1)



# result = natural_number(4)

# print(result)



# import 

# fact = 1
# for i in range(1, n+1):
#     fact *= i

# print(fact)




# numb = 5
# fact = 1

# i = 1

# while i <= numb:
#     fact *= i
#     i += 1

# print(fact)

# numb = 5
# fact = 1

# for i in range(1, numb+1):
#     fact *= i

# print(fact)


######################################## Lecture 6







# def prt_len(x):
#     print(x)



# prt_len([1,4,9,16,25,36,49,64,81,100])

# x= [1,4,9,16,25,36,49,64,81,100]
# def print_list(lists):
#     for item in lists:
#         print(item, end="")


# print_list(x)





