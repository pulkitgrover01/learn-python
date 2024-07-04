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
# pwd = ''
# for i in length:
#     pwd += length[i]


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

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" For reference
import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()
    print(f"Computer chose: {comp_choice}")
    result = determine_winner(user_choice, comp_choice)
    print(result)

# Play the game
play_game()



##################################################################################### Simple Calcaluter

# Arithmetic_Operators = ["+", "-", "*", "/", "%", "**","//"]

# while True:

#     user_input_1 = int(input("\nEnter First value: "))
#     user_input_2 = int(input("Enter First value: "))
    

#     Arithmetic_opt = input("Enter Arithmetic Operators: ")
#     while Arithmetic_opt not in Arithmetic_Operators:
#         Arithmetic_opt = input("Enter Correct Arithmetic Operators(+,-,*,/,%,**,//): ")


#     if Arithmetic_opt == "+":
#         print(f"\nThe Addition of {user_input_1} and {user_input_2} is {user_input_1 + user_input_2}")

#     elif Arithmetic_opt == "-":
#         print(f"\nThe Subtraction of {user_input_1} and {user_input_2} is {user_input_1 - user_input_2}")

#     elif Arithmetic_opt == "*":
#         print(f"\nThe Multiplication of {user_input_1} and {user_input_2} is {user_input_1 * user_input_2}")

#     elif Arithmetic_opt == "/":
#         print(f"\nThe Division of {user_input_1} and {user_input_2} is {user_input_1 / user_input_2}")

#     elif Arithmetic_opt == "%":
#         print(f"\nThe Modulus of {user_input_1} and {user_input_2} is {user_input_1 % user_input_2}")

#     elif Arithmetic_opt == "**":
#         print(f"\nThe Exponentiation of {user_input_1} and {user_input_2} is {user_input_1 ** user_input_2}")

#     elif Arithmetic_opt == "//":
#         print(f"\nThe Floor division of {user_input_1} and {user_input_2} is {user_input_1 // user_input_2}")



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

#     timeM = int(time.strftime("%M"))

#     timeS = int(time.strftime("%S"))

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




#################################################################### Check the Python version..

# import os

# print("Hello world.....")
# os.system("python --version")


######################################################################### Kon Bnega Crorepati!

# print("")
# print("Welcome to Kon bnega Crorepati!".title())
# print("")

# def get_userInput():
#     user_input = int(input("Press one for first Question: ".title()))
#     while 1 != user_input and user_input != "1":
#         print("Invalid choice. Please try again.")
#         user_input = int(input("Press one for first Question: ".title()))
#     return user_input


# def get_QusList(userInput):

#     if 1 == userInput or userInput == "1":
#         print('''Who are you?
#             1. God
#             2. Object
#             3. Atom
#             4. Human''')
#         userInput = input("Ans 1: ")

#         if 4 == userInput or userInput == "4":
#             print('''
#                 You win 1 Crore
#                 Your next question is........
#                 How many eyes human has?
#                 1. Two eyes
#                 2. Three eyes
#                 3. Four eyes
#                 4. One eye  ''')
#             userInput = int(input("Ans 2: "))

#             if 1 == userInput or userInput == 1:
#                 print('''
#                     You win 2 Crore
#                     Which gas a human lungs absorb to survive?
#                         1. Carbon-dioxide
#                         2. carbon-monoxide
#                         3. Oxygen
#                         4. Ozon  ''')
#                 userInput = int(input("Ans 3: "))

#                 if 3 == userInput or userInput == 3:
#                     print('''You win 3 Crore!
#                             Congurlation on your victory''')


#             else:
#                 print("You loose. You are out of the game now.")
#         else:
#             print("You loose. You are out of the game now.")
#     else:
#         print("You loose. You are out of the game now.")
        

# def startGame():
#     userInput = get_userInput()
#     QusList = get_QusList(userInput)
#     return QusList


# result = startGame()
# print(result)


#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Questions = [
#     ["Which language was used to create Fb?","Python","French","Javascript","C++",4],
#     ["What is your name?","Pulkit","Ramesh","Robin","Amit",1],
#     ["Where are you working?","Orris","DLF","ZYNGA","AIPL",3],
#     ["What is your job profile?","SDE","Animator","Analist","Manager",2],
#     ["What is your office timing?","08:00","09:00","10:00","11:00",3],
#     ["Who is your Manager?","Dipto","Navneet","Dasang","Ravi",1],
#     ["Where is your office?","Delhi","Chandigarh","Hissar","Bangalore",4],
#     ["How do you go to office?","Bus","Car","Bike","Plane",3],
#     ["Where are you From?","Delhi","Haryana","Mumbai","Karnataka",2],
#     ["In which currency do you earn?","Rupees","Doller","Rubel","Euro",1],
#     ["Which language do you speak?","English","Marathi","Bangali","Tamil",1],
#     ["What is your birth Year?","1997","2000","1996","1990",3],
#     ["Did you get promotion last year?","No","Yes","I dont know","Dont what to say",2],
#     ["At what age you started earning?","21","18","25","22",1],
# ]


# levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
# money = 1
# multi_choice= [0,1,2,3,4]

# print(f"\nWelcome to KBC created by Pulkit Grover.\nYou have to give {len(Questions)} correct answers to Win Rs: {levels[-1]}")

# start = int(input("Press Zero to start the game: "))
# while start is not 0:
#     start = int(input("You have entered the Wrong number. Press Zero to start the game: "))


# for i in range(0, len(Questions)):
#     ques = Questions[i]

#     print(f"\nHere is your {i+1} question for {levels[i]} Rupees.")

#     print(f"\n{ques[0]}\n A: {ques[1]}\n B: {ques[2]}\n C: {ques[3]}\n D: {ques[4]}")
        
#     ans = int(input("Press between 0-4 to answer or 0 to quit the game: "))
#     while ans not in multi_choice:
#         ans = int(input("Press between 0-4 to answer or 0 to quit the game: "))

#     if 0 == ans:
#         money = levels[i-1]
#         break
#     if ans == ques[5]:
#         print(f"You Won {levels[i]} Rupees.")
#         if i == 4:
#             money = 10000
#         elif i == 9:
#             money = 640000
#         elif i == 14:
#             money = 10000000
        
#     else:
#         print("\nWrong Answer. You are out of the game now.")
#         break
   

# print(f"Congrats...You are take home money is {money} Rupees Only.")



######################################################################### Encription or Decription

# import random
# import string


# while True:
#     user_code = input("Enter Code or Decode or Quit: ").lower()
#     while user_code not in ["code", "decode", "quit"]:
#         user_code = input("Please choose correct option- Code or Decode or Quit: ").lower()

#     if user_code == "code":
#         user_input = input("Please ender your message: ")
#         usr_ipt = user_input.split()
#         connect = []   
#         for i in usr_ipt:
#             if len(i) > 2:
#                 # pass
#                 code = i[1:] + i[0]
#                 f_b_code = "".join(random.choice(string.ascii_letters) for i in range(3)) \
#                             + code +  \
#                             "".join(random.choice(string.ascii_letters) for i in range(3))

#                 connect.append(f_b_code)
                    
#             else:
#                 # pass
#                 s_word = i[::-1]
#                 connect.append(s_word)

#         print(' '.join(connect))


#     elif user_code == "decode":
#         user_input = input("Please ender your message: ")
#         usr_ipt = user_input.split()
#         # pass
#         connect = []
#         for i in usr_ipt:
#             if len(i) > 2:

#                 code = i[3:-3]

#                 f_b_code = code[-1] + code[:-1]

#                 connect.append(f_b_code)

#             else:
#                 # pass
#                 s_word = i[::-1]
#                 connect.append(s_word)
                
#         print(' '.join(connect))


#     elif user_code == "quit":
#         break

######################################################################### Encription or Decription using Function Method

# import random
# import string

# ########### Code
# def code(user_input, enc_str):
#     store = []
#     usr_ipt = user_input.split()
#     for a in usr_ipt:

#         code1 = ''.join(random.choice(string.ascii_letters) for enc1 in range(enc_str))
#         code2 = ''.join(random.choice(string.ascii_letters) for enc1 in range(enc_str))
        
#         code = a[-1] + code1 + a[1:-1] + code2 + a[0] 
#         store.append(code)
#     result = ' '.join(store)
#     return result

# ########### Decode
# def decode(user_input1, enc_str):

#     store1 = [] 
#     usr_ipt1 = user_input1.split()
#     for b in usr_ipt1:

#         code1 = b[-1] + b[enc_str+1:len(b)-(enc_str+1)] + b[0]
        
#         store1.append(code1)
#     result = ' '.join(store1)
#     return result
    
# ########### Converter
# def converter():
#     while True:
#         user_code = input("Enter Code or Decode or Quit: ").lower()
#         while user_code not in ["code", "decode", "quit"]:
#             user_code = input("Please choose correct option- Code or Decode or Quit: ").lower()

#         if user_code == "code":
#             user_input = input("Please enter your message to code: ")
#             cod_str = int(input("Enter the encrytion number: "))
#             result = code(user_input, cod_str)
#             print(result)

#         elif user_code == "decode":
#             user_input = input("Please enter your message to decode: ")
#             cod_str = int(input("Enter the encryption number: "))
#             result = decode(user_input, cod_str)
#             print(result)

#         elif user_code == "quit":
#             break
 
# converter()    









