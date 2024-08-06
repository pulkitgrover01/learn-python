# def calculator():
#     value1 = float(input("Enter you first value: "))
#     AO = input("Enter you first value: ")   
#     value2 = float(input("Enter you first value: "))


#     if AO == "+":
#         print(value1 + value2)
#     elif AO == "-":
#         print(value1 - value2)
#     elif AO == "*":
#         print(value1 * value2)
#     elif AO == "/":
#         if value2 != 0:
#             print(value1 / value2)
#         else:
#             print("Error: Division by zero")

#     else:
#         print("Invalid Operater")


# calculator()



def folty_calculator():
    while True:
        ao = input("Choose your operator: ")
        value1 = float(input("Enter first value: "))
        value2 = float(input("Enter second value: "))

        if value1 == 45 and ao == "*" and value2 == 3:
            print(f"{value1} * {value2}: 555") 

        elif value1 == 56 and ao == "+" and value2 ==9:
            print(f"{value1} + {value2}: 77")

        elif value1 == 56 and ao == "/" and value2 == 6:
            print(f"{value1} / {value2}: 4") 
            
        elif "+" == ao:
            print(f"{value1} + {value2}: {value1+value2}")

        elif "-" == ao:
            print(f"{value1} - {value2}: {value1-value2}")

        elif "*" == ao:
            print(f"{value1} * {value2}: {value1*value2}")

        elif "/" == ao:
            if 0 != value2:
                print(f"{value1} / {value2}: {value1/value2}")
            else:
                print("Cant devide with zero")\
                
        else:
            print("Wrong AO")

        print("Do you want to calcualte again? Y for Yes and N for NO")
        user_input = input()
        if user_input == "y":
            continue
        else:
            break


        
folty_calculator()








