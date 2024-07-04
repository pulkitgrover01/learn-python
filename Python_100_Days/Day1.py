
# def f_for(num):
#     for number in num:
#         print("For",number)


# numbers = [1, 2, 3, 4, 5]
# f_for(numbers)




# def f_for(*num):
#     # print(type(num))
#     for number in num:
#         print("For",number)
        


# # numbers = [1, 2, 3, 4, 5]
# f_for(1, 2, 3, 4, 5)




# numbers = [1, 2, 3, 4, 5]
# index = 0
# while index < len(numbers):
#     print("While",numbers[index])
#     index += 1

# #Function
# def f_while(listes):
#     i = 0
#     while i < len(listes):
#         print(f"while {listes[i]}")
#         i += 1

# f_while([1, 2, 3, 4, 5])


# def hello_loop(num1 = 10, num2 = 20 ):
#     i = 1
#     print("Yes",i)
#     while i < num1:
#         i += 1
#         if i == 4:
#             continue
#         elif i == 5:
#             continue
#         elif i == 6:
#             continue
#         print("Hello",i)


#     else:
#         while i <= num2:
#             i += 1
#             if i == 12:
#                 continue
#             elif i == 16:
#                 break
        
#             print("One more loop",i)


#     print("---------------You are learning---------------")
# hello_loop(num1 = 5, num2 = 30)



# def num_Table(number):
#     for i in range(1,15):
#         print("5*",i,"=",5*i)
#         if i == 5:
#             print("Removed 5")
#             continue
#         elif i == 11:
#             break
#         print(f"{number}* {i} = {number * i}")



# num_Table(5)




# def average(*number):
#     sum = 0
#     for i in number:
#         sum += i
#     return sum / len(number)


# c= average(2,4,6)

# print(c)


# import this




# def find_Factorial(n):
#     if n == 0 or n == 1:
#         return 1
    
#     else:
#         return n * find_Factorial(n-1)


# print(find_Factorial(4))


# def fibonacci_seq(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci_seq(n-1) + fibonacci_seq(n-2)



# print(fibonacci_seq(7))



# test_dictionary = {'a' : 123, 1 : True, "b" : 456, 'AB' : 'lets see'}


# for key, value in test_dictionary.items():
#     print(f"your Key: {key} and values: {value}")

# else:
# #     print("Done")




# for i in range(10):
#     print(f"iteration no {i+1} in for loop")
#     # if i > 5:
#     #     break

# else:
#     print("else block in loop")

# print("Out of loop")






# x = int(input("Enter number: "))
# try:
#     num = [4,6,8]
#     print(num[x])

#     print(x + 5)

# except NameError:
#     print("Name not defined")

# except TypeError:
#     print("Typing error")

# except IndexError:
#     print("There is an index error")

# else:
#     print("something")















# while True:
#     a =  input("Entr the value between 5 and 9: ")

#     if "quit" == a:
#         print("You are out of program now.") 
#         break
        

#     a = int(a)
#     if 5 <= a <= 8:
#         print("Yes! Sir")
#         break


#     else:
#         raise ValueError("Value should be between 5 and 9")
#     # raise Exception ValueError TypeError IndexError NameError 


# a = 6
# b = 5
# print("Yes") if a < b else print("==") if a == b else print("Play")

# print("Hello") if 5 < 6 else print("Bye")


# inventory_names = ['plastic','metal','rubber','sheet','paper','glass']
# inventory_numbers = [52,9,56,60,85,42]


# for index, name in enumerate(inventory_names,start=1):
#     print(f"{index+1} : {name}")
#     if index == len(inventory_names) / 2:
#         print("Half if done")
        








# for index,a in enumerate(range(0,100),start=1):
#     print(f"{index} : Yes")
# else:
#     print("No")




# import pulkit
# import os

# pulkit.namer()
# print(pulkit.name)

# for i in pulkit.inventory_names:
#     print(i)


# print(dir(os))







# import random
# import string

   
# def code(user_choice, cod_str):   
#     usr_ipt = user_choice.split()
#     connect = []   
#     for i in usr_ipt:
#         if len(i) > 2:
#             code = i[1:] + i[0]
#             f_b_code = "".join(random.choice(string.ascii_letters) for i in range(cod_str)) \
#                         + code +  \
#                         "".join(random.choice(string.ascii_letters) for i in range(cod_str))
            
#             connect.append(f_b_code)
                    
#         else:
#             s_word = i[::-1]
#             connect.append(s_word)

#     a =' '.join(connect)
#     return a

    
# def decode(user_choice, cod_str):     
#     usr_ipt = user_choice.split()
#     connect = []
#     for i in usr_ipt:
#         if len(i) > 2:
#             code = i[cod_str:-cod_str]
#             f_b_code = code[-1] + code[:-1]
#             connect.append(f_b_code)

#         else:
#             s_word = i[::-1]
#             connect.append(s_word)
                
#     a =' '.join(connect)
#     return a

    
# def converter():
#     while True:
#         user_code = input("Enter Code or Decode or Quit: ").lower()
#         while user_code not in ["code", "decode", "quit"]:
#             user_code = input("Please choose correct option- Code or Decode or Quit: ").lower()

#         if user_code == "code":
#             user_choice = input("Please enter your message to code: ")
#             cod_str = int(input("Enter the encrytion number: "))
#             result = code(user_choice, cod_str)
#             return result

#         elif user_code == "decode":
#             user_choice = input("Please enter your message to decode: ")
#             cod_str = int(input("Enter the encryption number: "))
#             result = decode(user_choice, cod_str)
#             return result

#         elif user_code == "quit":
#             break

# output = converter()    
# print(output)

#########################################################################




# x = 400

# def myfunc():
#   global x
#   x = 300

#   print(x)

# myfunc()

# print(x)



# import os


# if os.path.exists("numbers.txt"):
#     print("Yes file Exist")
#     os.remove("numbers.txt")

# else:
#     print("file does not exist")


# stuent_name = ["Pulkit", "Lakshya", "Robin", "Amit"]

# i = 0


# # with open("marks.txt") as marks:
# marks =  open("marks.txt")

# while True:
#     i += 1
#     a = marks.readline()
#     if not a:
#         break
#     s1 = int(a.split(",")[0])
#     s2 = int(a.split(",")[1])
#     s3 = int(a.split(",")[2])
#     s4 = int(a.split(",")[3])

#     print(f"Marks of student {stuent_name[i-1]} in English: {s1}")
#     print(f"Marks of student {stuent_name[i-1]} in Math   : {s2}")
#     print(f"Marks of student {stuent_name[i-1]} in Science: {s3}")
#     print(f"Marks of student {stuent_name[i-1]} in Hindi  : {s4}\n")




# name = "list1", "list2", "list3", "Ram"
# with open("text-file.txt","w") as f:

#     for nam in name:
#         f.writelines(nam + "\n")
#         f.close 
#     f.truncate(2)


# with open("text-file.txt","r") as f:
#         print(f.read())



# dubble = lambda x: x*2


# play = dubble(8)

# print(play)





# cube = lambda x: x*x*x


# n_list = [10,1,3,25,6,8,2,9]
# new_list = []

# for val in n_list:
#     new_list.append(cube(val))
# new_list = tuple(map(cube, n_list))
# print(new_list)

# new_map = list(map(lambda x: x*x*x, n_list))
# new_map.sort()
# print(new_map)


# def filter_function(a):
#     return a > 5

# new_filter = list(filter(filter_function, n_list))
# print(f" new_check: {new_filter}")


# new_filter1 = list(filter(lambda x: x > 5, n_list))
# print(f" new_check1: {new_filter1}")


# numbers = [1,2,3,4,5]

# store = 0
# for i in numbers:
#     store += i

# print(f"For loop method: {store}")


# from functools import *

# new_reduce = reduce(lambda a,b:a+b, numbers)
# print(f"Reduce method: {new_reduce}")


# numbers = [1,2,3,4,5]
# val1 = 0
# store = []
# for i in numbers:
#     if i >= 3:
#         store.append(i)
        
# for st in store:
#     val1 += st

# print(store)
# print(val1)



############################################ Snake - Water - Gun

# import random

# # Computer input
# def get_computer_choice():
#     global compuer_list
#     compuer_list = ["snake","water","gun"]
#     return random.choice(compuer_list)
# get_computer_choice()

# # User imput
# def get_user_choice():
#     user_choice = input("Please enter your choice (Snake - Water - Gun): ").lower()
#     while user_choice not in compuer_list:
#         print("Please enter correct choice.")
#         user_choice = input("Please enter your choice (Snake - Water - Gun): ").lower()
#     return user_choice

# # generator
# def get_winner(user_choice, compuer_choice):
#     if user_choice == compuer_choice:
#         return "Game is Draw"
        
#     elif (compuer_choice == "snake" and user_choice == "water") or \
#         (compuer_choice == "water" and user_choice == "gun") or \
#         (compuer_choice == "gun" and user_choice == "snake"):
#         return "Computer Win and You lose"

#     else:
#         return "You Win and Computer lose"


# def lets_play():
#     user_choice = get_user_choice()
#     computer_choice = get_computer_choice()
#     print(f"Computer chose: {computer_choice}")
#     result = get_winner(user_choice,computer_choice)
#     print(result)

# lets_play()



##################

class person():
    def __init__(self, name, age, work, job):
        self.name = name
        self.age = age
        self.work = work
        self.job = job
    # name = "Pulkit Grover"
    # age = 27
    # work = "Zynga"
    # job = "Animator"

    def info(self):
        print(f"{self.name} is {self.age} year old. He work as {self.work} in {self.job} company.")

s1 = person("Lakshya Grover",54,"Engineer","Minda")
# s1.name = "Lakshya Grover"
# s1.work = "Engineer"
# s1.job = "Minda"

# s2 = person()
# s2.name = "Raj Kuamr"
# s2.age = 54

# s3 = person()


s1.info()
# s2.info()
# s3.info()







