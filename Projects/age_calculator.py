# You can calculate your age by your Age or by your Birth Year.

user_input = input("Enter your age/Year: ")


if user_input > "2024" or user_input <= "0" and len(user_input) == 1:
    print("You are not born yet!!")

elif user_input < "1925" or user_input > "100" and len(user_input) == 3 :
    print("You seems to be the oldest person alive.")
    
 
#Age
elif len(user_input) == 2 or len(user_input) == 1:
    user_input = int(user_input)
    output = (100 - user_input) + 2024
    print(f"You will be 100 year old in {output}")
    
    user_input1 = input("Enter to check your age on perticular year or Q to exit: ")
    if user_input1 == "q" or user_input1 == "Q":
        exit()

    else:
        user_input1 = int(user_input1)
        output1 = user_input1 + user_input - 2024
        print(f"You will be {output1} years old in {user_input1}")

# Years
elif len(user_input) == 4:
    user_input = int(user_input)
    output = (100 + user_input)
    print(f"You will turn 100 in {output}")

    user_input1 = input("Enter to check your age on perticular year or Q to exit: ")
    if user_input1 == "q" or user_input1 == "Q":
        exit()

    else:
        user_input1 = int(user_input1)
        output1 = user_input1 - user_input
        print(f"You will be {output1-1} years old in {user_input1}")

    

 


