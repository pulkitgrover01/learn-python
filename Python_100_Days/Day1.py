
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

# class person():
#     def __init__(self, name, age, work, job):
#         self.name = name
#         self.age = age
#         self.work = work
#         self.job = job
    # name = "Pulkit Grover"
    # age = 27
    # work = "Zynga"
    # job = "Animator"

#     def info(self):
#         print(f"{self.name} is {self.age} year old. He work as {self.work} in {self.job} company.")

# s1 = person("Lakshya Grover",54,"Engineer","Minda")
# s1.name = "Lakshya Grover"
# s1.work = "Engineer"
# s1.job = "Minda"

# s2 = person()
# s2.name = "Raj Kuamr"
# s2.age = 54

# s3 = person()


# s1.info()
# s2.info()
# s3.info()


# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good morning")
#         fx(*args, **kwargs)
#         print("Thank you for visiting")
#     return mfx() 


# @greet
# def hello():
#     print("Hello World")

# @greet  
# def add(a, b):
#     print(a+b) 

# hello()
# greet(add)(5,5)



# class MyClass():
#     def __init__(self, value):
#         self.value = value

#     def show(self):
#         print(f"Your show value is {self.value}")


#     def ten_value(self):
#         return 10 * self.value
    

#     def ten_value(self, new_value):
#         self.new_value = new_value / 10



# a = MyClass(10)
# a.new_value = 67
# a.show()
# a.ten_value(96)



# class employee:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#         self.__work = "Animator"

#     def father(self):
#         print(f"The student ID {self.id} is {self.name}.")
#         # print(self.__work)


# class animator(employee):
#     def son(self):
#         print("The son is happy")

# class business(animator):
#     def mummy(self):
#         print("I work at home")




# a = employee(4, "car")
# print(a._employee__work)
# # print(a.__dir__())

# a.father()


# 
# b = animator(40, "Shyam")
# b.father()
# b.son()
# c = business(10, "Sita")
# c.father()
# c.mummy()

# class library:
#     car = 6
#     def __init__(self):
#         self.books = []
#         self.noBooks = 0

#     def addBooks(self, books):
#         self.books.append(books)
#         self.noBooks = len(self.books)
        
#     def getInfo(self):
#         print(f"You have {self.noBooks} in your library. Here are the names: ")
#         for book in self.books:
#             print(book)
            
#     @staticmethod
#     def check():
#         library.car +=1
#         print(f"Its working now. We have {library.car} cars.")

# a = library()
# a.addBooks("Lembo legends")
# a.addBooks("Lembo legends2")
# a.addBooks("Lembo legends3")
# a.getInfo()
# a.check()
# b = library()
# b.check()
# c = library()   
# c.check()

# class math:
#     def __init__(self, c, d, e ,f):
#         self.c = c
#         self.d = d
#         self.e = e
#         self.f = f


#     def addition(self):
#         print(self.c + self.d)

#     @staticmethod
#     def add(a, b):
#         print(a + b)


# a = math(3,4,5,6)
# a.addition()

# math.add(5,4)




# class employee:
#     company_name = "Zynga"
#     company_size = 0
#     def __init__(self, name, age = 48):
#         self.name = name
#         self.age = age
#         self.slary_hike = 15
#         employee.company_size +=1

#     # @staticmethod   
#     def student(self):
#         print(f"Hi {self.name}.You age is {self.age}. You work in a company {self.company_name}.Your company size is {self.company_size}. Your raise amount is {self.slary_hike}.")



# employee.company_name = "Fila-tch"


# a = employee("Pulkit",45)
# a.slary_hike = 23
# a.company_name = "Minda"
# a.student()


# b = employee("Grover",23)
# b.company_name = "Netle"
# b.student()

# c = employee("Laksya")
# c.student()



# class employee:
#     company = "Apple"

#     def show(self):
#         print(f"Your name is {self.name} and your work in {self.company} Company.")

#     @classmethod
#     def change_company(self, new_company):
#         self.company = new_company
    


# a = employee()
# a.name = "Pulkit"
# a.show()

# b = employee()
# b.name = "Lakshya"
# b.company = "Zynga"
# b.show()

# f = employee()
# f.name = "Pawan"
# f.show()


# c = employee()
# c.name = "Raj Kumar"
# c.change_company("business")
# c.show()

# d = employee()
# d.name = "Parveen"
# d.show()



# bucket = " Pulkit, 27, Bhiwani, Haryana,      India, Asia, Earth, Solar system, Milkey way"

# print(bucket)
# val = bucket.replace(" ", "")
# print(val)
# val1 = val.split(",")
# print(val1)
# for index,lst in enumerate(val1, start=1):
#     print(index,lst)
   
    


# class program:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class student(program):
#     def __init__(self, name, age, profession):
#         super().__init__(name, age)
#         self.profession = profession

# class profeser(student):
#     def __init__(self, name, age, profession):
#         super().__init__(name, age, profession)

# a = program("Pulkit",45)
# print(a.name)
# print(a.age)

# b = student("Lakshya",13,"self-employee")
# print(b.name)
# print(b.age)
# print(b.profession)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"Your name is {self.name} and your age is {self.age}"    

# p1 = Person("John", 36)

# print(p1)



# import math

# class shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def area_of_shape(self):
#         return self.x * self.y


# class circle(shape):
#     def __init__(self, radius):
#         super().__init__(radius, radius)
#         self.radius = radius
    
#     def area_of_circle(self):
#         return math.pi * super().area_of_shape()


# s = shape(5,4)
# print(s.area_of_shape())

# c = circle(5)
# print(c.area_of_circle())



#########################################################################################################

# import os

# os.getcwd
# print("current working", os.getcwd())
# os.chdir("C:/Users/pgrover/Desktop/python-games/learn-python/Merge_PDF")
# print("done", os.getcwd())

########################################################### Combined_PDF_File

# from PyPDF2 import PdfWriter

# fileses = PdfWriter()

# input1 = open("Gaurav_Kumar_Chunera__Motion_Graphics_Artist.pdf", "rb")
# input2 = open("Laxminarayan Swain Resume-1.pdf", "rb")
# input3 = open("Palak Goel Resume 2024.pdf", "rb")
# input4 = open("resume-ananya.pdf", "rb")
# input5 = open("Resume-Vishal-Kapoor.pdf", "rb")

# fileses.append(input1)
# fileses.append(input2)
# fileses.append(input3)
# fileses.append(input4)
# fileses.append(input5)

# os.chdir("C:/Users/pgrover/Desktop/python-games/learn-python/Merge_PDF/Edited_files")

# with open("CV_combined.pdf","wb") as output:
#     fileses.write(output)

# fileses.close()
# output.close()



######################################################## Only_Fist_Page_of_PDF
# os.chdir("C:/Users/pgrover/Desktop/python-games/learn-python/Merge_PDF")


# from PyPDF2 import PdfWriter

# fileses = PdfWriter()

# input1 = open("Gaurav_Kumar_Chunera__Motion_Graphics_Artist.pdf", "rb")
# input2 = open("Laxminarayan Swain Resume-1.pdf", "rb")
# input3 = open("Palak Goel Resume 2024.pdf", "rb")
# input4 = open("resume-ananya.pdf", "rb")
# input5 = open("Resume-Vishal-Kapoor.pdf", "rb")

# fileses.merge(position=4, fileobj=input1, pages=(0,1))
# fileses.merge(position=3, fileobj=input2, pages=(0,1))
# fileses.merge(position=0, fileobj=input3, pages=(0,1))
# fileses.merge(position=1, fileobj=input4, pages=(0,1))
# fileses.merge(position=2, fileobj=input5, pages=(0,1))

# os.chdir("C:/Users/pgrover/Desktop/python-games/learn-python/Merge_PDF/Edited_files")

# with open("CV_First_Page_combined.pdf","wb") as output:
#     fileses.write(output)

# fileses.close()
# output.close()



# class vector:
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
    
#     def __add__(self, x):
#         return vector(self.i + x.i, self.j + x.j, self.k + x.k)


# v1 = vector(3,5,7)
# # print(v1)

# v2 = vector(2,5,8)
# # print(v2)

# print(v1+v2)
# print(type(v1+v2))

####################################################################

# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice") 


# name_list = ["Pulkit", "Lakshya", "Raj Kumar", "Parveen"]

# for name in name_list:
#     speak_name = f"Shoutout to {name}"
#     speaker.speak(speak_name)


# import pyttsx3
# engine = pyttsx3.init()

# name_list = ["Pulkit", "Lakshya", "Raj Kumar", "Parveen"]


# for name in name_list:
#     speak_name = f"Shoutout to {name}"
#     engine.say(speak_name)
# engine.runAndWait()





# engine.say(name_list())
# engine.runAndWait()


################################################################ To measure time
# import time

# def while_loop():
#     i = 0
#     while i < 50000:
#         i += 1
#         print(i)


# def for_loop():
#     for i in range(5000):
#         print(i)


# check_time = time.time()
# while_loop()
# while_time = time.time() - check_time

# check_time = time.time()
# for_loop()
# print(f"While time {while_time}")
# print(f"For time {time.time() - check_time}")





# foods = []
# while True:
#     food = input()
#     if food == "quit":
#         break
#     foods.append(food)

# print(foods)
################################################################ Walrus

# foods = []
# while (food := input("enter the food you like: ")) != "quit":
#     foods.append(food)

# print(foods)


# import multiprocessing.process
# import requests
# from bs4 import *


# url = "https://www.google.co.in/"

# rqst = requests.get(url)
# soup = BeautifulSoup(rqst.text, "html.parser")

# print(r.text)
# print(soup.prettify())
# for heading in soup.find_all("style"):
#     print(heading.text)




# def my_generator():
#     for i in range(5):
#         yield i
        

# check = my_generator()

# for j in check:
#     print(j)




# import requests
# import json

# query = input("What type of news are you intriested in? ")
# url = f"https://newsapi.org/v2/everything?q={query}&from=2024-06-12&sortBy=publishedAt&apiKey=b725bb113a9e4984b0dbdf25949d0ce3"
# r = requests.get(url)
# news = json.loads(r.text)


# for article in news["articles"]:
#     print(article["title"])
#     print(article["description"])
#     print("-----------------------------------------------------")




############################################################################# How to download image from internet




############################################################################ Multithreading

# import threading
# import time

# a = time.time()
# def print_numbers():
#     for i in range(10):
#         print(i)

# b = time.time()
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_numbers)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# c = b - a
# print(c)

############################################################################ Multiprocessing
# import time
# from multiprocessing import Process


# a = time.time()
# def print_numbers():
#     for i in range(10):
#         print(i)
        
# b = time.time()
# process1 = Process(target=print_numbers)
# process2 = Process(target=print_numbers)

# if __name__ == '__main__':
#     process1.start()
#     process2.start()

#     process1.join()
#     process2.join()

# c = b - a
# print(c)



# from datetime import datetime
# from pygame import mixer
# from time import time


# def MusicOnLoop(file, stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
   
#     while True:
#         user_input = input()
#         if user_input == stopper:
#             mixer.music.stop()
#             break

# def logFile(record):
#     with open("Python_100_Days/recored.txt","a") as r:
#         r.write(f"{record} ... {datetime.now()}\n")

# if __name__=="__main__":
   
#     init_water = time()
#     init_eyes = time()
#     init_exercise = time()
#     water_break = 5
#     eye_break = 10
#     exercise_break = 20

#     while True:
#         if time() - init_water > water_break:
#             print("You have to drink water")
#             MusicOnLoop("Python_100_Days/water.mp3","w")
#             init_water == time()
#             logFile("Drank water")

#         if time() - init_eyes > eye_break:
#             print("Rest to your eye")
#             MusicOnLoop("Python_100_Days/water.mp3","w")
#             init_eyes == time()
#             logFile("Rest Eye")

# C:/Users/pgrover/Desktop/sort
# import os  
# url =  input("Please enter the directory: ")
# # file =  input()
# format = input()


# def soldier(url, format):
#     os.chdir(url)
#     print(os.listdir())
#     lists = os.listdir() 
    
#     i = 1
#     for file in lists:
#         if file.endswith(format):
#             os.rename(f"{file}", f".png")
#             i += 1



# soldier(url, format)


# class library:
#     def __init__(self, list, name):
#         self.booklist = list
#         self.name = name
#         self.lendDict = {}


#     def displayBook(self):
#         print(f"\nWe have following books in our library: {self.name}")
#         for index, book in enumerate(self.booklist, start= 1):
#             print(f"{index}: {book}")

#     def lendBook(self, user, book):
#         if book not in self.lendDict.keys():
#             self.lendDict.update({book:user})
#             print("Lender Book database has been updated. You can take the book now")
#         else:
#             print(f"Book has already been used by {self.lendDict[book]}")


#     def addBook(self, book):
#         self.booklist.append(book)
#         print("Book has been added to the book list")

#     def returnBook(self, book):
#         self.lendDict.pop(book)



# if __name__ == "__main__":
#     pulkit = library(["Pthon","C++","C#","JAVA","RUBY","MURN"], "Code With Pulkit")

#     while True:
#         print(f"Welcome to the {pulkit.name} library. Enter your choice to continue")
#         print(f"1. Display Book\
#               \n2. Lend Book\
#               \n3. Add Book\
#               \n4. Return Book\
#               \nq to Quit")
#         vari = ["1","2","3","4","q"]
#         user_input = input("Please enter your option: ")
#         while user_input not in vari:
#             user_input = input("Please enter your option: ")
        
#         if user_input == "q":
#             break
       
#         elif user_input == "1":
#             pulkit.displayBook()

#         elif user_input == "2":
#             book = input("Enter the name of the book you want to lend: ")
#             user = input("Enter you name: ")
#             pulkit.lendBook(user, book)

#         elif user_input == "3":
#             book = input("Enter the name of the book you want to add: ")
#             pulkit.addBook(book)

#         elif user_input == "4":
#             book = input("Enter the name of the book you want to return: ")
#             pulkit.returnBook(book)

#         else:
#             print("Not a valid option")

#         print("Press q to quit and c to continue")
#         user_input1 = input()
#         while user_input1 != "q" and user_input1 != "c":
#             user_input1 = input()

#             if user_input1 == "q":
#                 exit()

#             elif user_input1 == "c":
#                 continue



# a = []

# while (list := input("enter the food you like: ")) != "q":
#     a.append(list)
  

# # reverse method
# rev = a.copy()
# rev.reverse()
# print(f"Reverse method: {rev}")

# # slicing method
# slic = a[::-1]
# print(f"Slicing method: {slic}")

# #indexing
# p_a = [a[3] , a[2] , a[1] , a[0]]
# print(f"indexing method: {p_a}")



a = [1,2,3,4]

# size = int(input("Enter the list lenght: "))
# for list in range(size):
#     a.append(int(input("Enter your numbers: ")))
  

# reverse method
rev = a.copy()
rev.reverse()
print(f"Reverse method: {rev}")

# slicing method
slic = a[::-1]
print(f"Slicing method: {slic}")

#indexing
p_a = [a[3] , a[2] , a[1] , a[0]]
print(f"indexing method: {p_a}")





