import random


user_input = input("Enter your choice: 1- Rock 2- Paper 3- Scissor: ")
computer_choice = ["Rock", "Paper", "Scissor"] 


comp_output = random.choice(computer_choice)
print(f"Computer choose: {comp_output}")

if comp_output == user_input:
        print("Its a tie. Try again")

elif user_input == "Rock":
        
    if comp_output == "Paper":
         print("Computer won, Paper covers Rock!")

    elif comp_output == "Scissor":
        print("Your won, Rock smashes Scissor! ")
           

elif user_input == "Paper":

    if comp_output == "Scissor":
        print("Computer won, Scissor cut the Paper!")

    elif comp_output == "Rock":
        print("Your won, Paper covers Rock! ")
           

elif user_input == "Scissor":

    if comp_output == "Rock":
        print("Computer won, Rock smashes Scissor!")
        
    elif comp_output == "Paper":
        print("Your won, Scissor cut the Paper!")
          
    
        
print("---------- User Won -----------")














