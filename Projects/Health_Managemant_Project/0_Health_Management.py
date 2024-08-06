
import datetime

w_or_a = "a" # w to write and a to append
l_foods = []
l_exercises = []
name = ["","Pulkit","Lakshya","Amit"]
name_code = ["pe","pf","le","lf","ae","af"]
# Date and Time
def get_D_and_T():
    return datetime.datetime.now()

print("Press 1 to open ...Pulkit... file\
      \nPress 2 to open ...Lakshya... file\
      \nPress 3 to open ...Amit... file")
user_input = int(input())

print("Would you like to Read or Write\
      \nPress R to read or W to write")
r_or_w = input()

# Write
def Write(r_or_w):
    if r_or_w == "w":

        print("Press E to Enter Exercise details or F for food details.")
        user_input1 = input().lower()
        if user_input1 == "e":
            print(f"Write exercise {name[user_input]} has done.")
            while (u_exercise := input()) != "q":
                l_exercises.append(u_exercise)

        elif user_input1 == "f":
            print(f"Write food names {name[user_input]} had.")
            while (u_food := input()) != "q":
                l_foods.append(u_food)
                

        if user_input == 1: #Pulkit
            if user_input1 == "e":
                with open("Projects/Health_Managemant_Project/Pulkit Grover_Exercise.txt", f"{w_or_a}") as a:
                    a.write(f"\n{l_exercises} ....... {get_D_and_T()}")

            elif user_input1 == "f":
                with open("Projects/Health_Managemant_Project/Pulkit Grover_Food.txt", f"{w_or_a}") as a:
                    a.write(f"\n{l_foods} ....... {get_D_and_T()}")

        elif user_input == 2: #Lakshya
            if user_input1 == "e":
                with open("Projects/Health_Managemant_Project/Lakshya Grover_Exercise.txt", f"{w_or_a}") as a:
                    a.write(f"\n{l_exercises} ....... {get_D_and_T()}")

            elif user_input1 == "f":
                with open("Projects/Health_Managemant_Project/Lakshya Grover_Food.txt", f"{w_or_a}") as a:
                    a.write(f"\n{l_foods} ....... {get_D_and_T()}")

        elif user_input == 3: #Amit
            if user_input1 == "e":
                with open("Projects/Health_Managemant_Project/Amit Kaushik_Exercise.txt", f"{w_or_a}") as a:
                    a.write(f"\n{l_exercises} ....... {get_D_and_T()}")

            elif user_input1 == "f":
                with open("Projects/Health_Managemant_Project/Amit Kaushik_Food.txt", f"{w_or_a}") as a:
                    a.write(f"\n{l_foods} ....... {get_D_and_T()}")
Write(r_or_w)
# Read
def read(r_or_w):
    if r_or_w == "r":

        print("To check the record Press first letter of Person and Activity\
            \nExample: PE or PF ")
        people_list = ["pe","pf","le","lf","ae","af"]

        read_input1 = input()
        while read_input1 not in people_list:
            read_input1 = input()
            
        if read_input1 == "pe": #Pulkit
            with open("Projects/Health_Managemant_Project/Pulkit Grover_Exercise.txt") as a:
                print(a.read())

        elif read_input1 == "pf":
            with open("Projects/Health_Managemant_Project/Pulkit Grover_Food.txt") as a:
                print(a.read())

        elif read_input1 == "le": #Lakshya
            with open("Projects/Health_Managemant_Project/Lakshya Grover_Exercise.txt") as a:
                print(a.read())

        elif read_input1 == "lf":
            with open("Projects/Health_Managemant_Project/Lakshya Grover_Food.txt") as a:
                print(a.read())

        elif read_input1 == "ae": #Amit
            with open("Projects/Health_Managemant_Project/Amit Kaushik_Exercise.txt") as a:
                print(a.read())

        elif read_input1 == "af":
            with open("Projects/Health_Managemant_Project/Amit Kaushik_Food.txt") as a:
                print(a.read())
read(r_or_w)




