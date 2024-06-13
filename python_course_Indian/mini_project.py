##################################################################################### Guess the number

# import random
# myRandom = random.randint(1, 5)

# def guess_the_number(myRandom):

#     while True:
#         myNumber = input("Enter your number or quit(Q): ")
#         if myNumber == "q" or myNumber == "Q":
#             break

#         myNumber = int(myNumber)
#         if myNumber == myRandom:
#             print("You guessed it right.")
#             break

#         elif myNumber < myRandom:
#             print("Your guessed the smaller number")

#         else:
#             print("You guessed the bigger number")


# guess_the_number(myRandom)

# print("---------Game Over---------")



##################################################################################### Random password generator

# import random
# import string



# def generate_password(length):

#     val = string.ascii_letters + string.punctuation + string.digits

#     pwd = "".join([random.choice(val) for i in range(length)])   

#     return pwd
   


# length= int(input("Enter the desired passwork length: "))

# password = generate_password(length)

# print(f"Here is the {length} lenght of random password: {password}")



#******************************************************************
# pwdGen = "".join([random.choice(val) for i in range(pwd_lan)])                   List compression way

# print(f"Here is the {pwd_lan} lenght of random password: {pwdGen}")
#*******************************************************************
 



##################################################################################### Rock - Paper - Scissor

# import random

# computer_choice = ["Rock", "Paper", "Scissor"] 

# comp_output = random.choice(computer_choice)
# print(f"Computer choose: {comp_output}")


# user_input = input("Enter your choice: 1: Rock 2: Paper 3: Scissor: ")

# if comp_output == user_input:
#         print("Its a tie. Try again")

# elif user_input == "Rock":
        
#     if comp_output == "Paper":
#          print("Computer won, Paper covers Rock!")

#     elif comp_output == "Scissor":
#         print("Your won, Rock smashes Scissor! ")
           

# elif user_input == "Paper":

#     if comp_output == "Scissor":
#         print("Computer won, Scissor cut the Paper!")

#     elif comp_output == "Rock":
#         print("Your won, Paper covers Rock! ")
           

# elif user_input == "Scissor":

#     if comp_output == "Rock":
#         print("Computer won, Rock smashes Scissor!")
        
#     elif comp_output == "Paper":
#         print("Your won, Scissor cut the Paper!")

# else:
#      print("invalid input")

              
# print("---------- Game Over -----------")



##################################################################################### Simple Calcaluter














##################################################################################### text to speech, time and wishes

# import pyttsx3
# engine = pyttsx3.init()
# # engine.say("Hello Pulkit! Welcome to this python world.")
# # engine.runAndWait()


# import time

# timestamp = time.strftime("%H:%M:%S")

# def hourly_time():

#     time_H = int(time.strftime("%H"))
#     return time_H

#     # timeM = int(time.strftime("%M"))

#     # timeS = int(time.strftime("%S"))

# def wish_time(time_H):

#     if 0 <= time_H and 6 > time_H:
#         return "Good Night and Morning Sir"

#     elif 6 <= time_H and 12 > time_H:
#         return "Good morning Sir"

#     elif 12 <= time_H and 16 > time_H:
#         return "Good Afternoon Sir"
    
#     elif 16 <= time_H and 20 > time_H:
#         return "Good Envening Sir"

#     elif 20 <= time_H and 24 > time_H:
#         return "Good Night Sir"

# def play():
#     hour_time = hourly_time()

#     result = wish_time(hour_time)
#     return result


# output = play()
# #Text
# print(f"{output}.\nThe time is {timestamp}")

# #Spech
# engine.say(f"{output}. The time is {timestamp}")
# engine.runAndWait()




#################################################################### Postive or Negaitve number

# def user_input():
#     user_input = int(input("Pleae enter your value: "))
#     return user_input



# def numb_status(num):
#     if num < 0:
#         return "Number is negatve."
    
#     elif num == 0:
#         return "Number is zero"

#     else:
#         return "Number is positive."



# def check_value():
#     usr_iput = user_input()
#     print(usr_iput)
    
#     result = numb_status(usr_iput)
#     return result


# output = check_value()
# print(output)



#################################################################### Check the time and Wishes
# import time

# timestamp = time.strftime("%H:%M:%S")

# def hourly_time():

#     time_H = int(time.strftime("%H"))
#     return time_H

#     # timeM = int(time.strftime("%M"))

#     # timeS = int(time.strftime("%S"))

# def wish_time(time_H):

#     if 0 <= time_H and 6 > time_H:
#         return "Good Night and Morning, Sir"

#     elif 6 <= time_H and 12 > time_H:
#         return "Good morning, Sir"

#     elif 12 <= time_H and 16 > time_H:
#         return "Good Afternoon, Sir"
    
#     elif 16 <= time_H and 19 > time_H:
#         return "Good Evening, Sir"

#     elif 19 <= time_H and 24 > time_H:
#         return "Good Night, Sir"


# def play():
#     hour_time = hourly_time()

#     result = wish_time(hour_time)
#     return result


# output = play()
# print(F"{output}.\nThe time is {timestamp}")




#################################################################### Check the Python version..

# import os

# print("Hello world.....")
# os.system("python --version")





























