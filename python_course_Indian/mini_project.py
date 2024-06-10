#Guess the number

# import random

# myRandom = random.randint(1, 5)

# while True:
#     myNumber = input("Enter your number or quit(Q): ")
#     if myNumber == "q" or myNumber == "Q":
#         break

#     myNumber = int(myNumber)
#     if myNumber == myRandom:
#         print("You guessed it right.")
#         break

#     elif myNumber < myRandom:
#         print("Your guessed the smaller number")

#     else:
#         print("You guessed the bigger number")




# print("---------Game Over---------")






# import random
# rndNum = random.randint(1,5)

# idx = 1
# while True:
#     userNum = input("Enter your number or press Q for quit: ")
#     if userNum == "q" or userNum == "Q":
#         break
    
#     userNum = int(userNum)
#     if userNum == rndNum:
#         print("Goo Job. Your number is matched. after", idx, "Try")
#         break

#     elif userNum < rndNum:
#         print("your given number is smaller.")

#     else:
#         print("Your given number is bigger.")

#     idx += 1


# print("----------Game Over----------")





#Random password generator

import random
import string


pwd_lan= 20

val = string.ascii_letters + string.punctuation + string.digits

password = ""

for i in range(pwd_lan):
    password += random.choice(val)


 
print(f"Here is the {pwd_lan} lenght of random password: {password}")
