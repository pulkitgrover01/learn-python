#Project 1

check = float(input("Roadmap Provider Project: Cloose 1: Fesher, Choose 2: Experienced:"))


if check == 1:
    
    choose = int(input("Enter 1: Web Dev\nEnter 2: App Dev\nEnter 3: DS,ML,AI\n"))

    if choose == 1:
        print("For Web Dev: Learn HTML, CSS, JS, Python, Django")

    elif choose == 2:
        print("For App Dev: Lean Jave + DSA + Build Projects")

    elif choose == 3:
        print("For DS,ML,AI: Learn ython, Maths, R")

    else:
        print("Please Enter between the given numbers")

elif check == 2:
    
    choose = int(input("Enter 1: Data Analytics\nEnter 2: Cloud Computing\nEnter 3: Front-end\n"))

    if choose == 1:
        print("For Data Analytics: Learn Python, Excel, PowerBI")

    elif choose == 2:
        print("For Cloud Computing: Learn DevOps and Python for Automation")

    elif choose == 3:
        print("For Fort-end: Learn Python and Django for Backend")

    else:
        print("Please Enter between the given numbers")

else:
    print("Please Enter between the given numbers")



#Project 2

check2 = float(input("Please enter the days you attended the class for Certificate Eligibility:"))

if check2 == 5:

    assin = input("Did you submit assignment? Yes or No:")
    liv_cls = input("Did you attend live class? Yes or No:")
    cam_on = input("Was you camera on? Yes or No:")

    if assin.title() == "Yes" and liv_cls.title() == "Yes" or cam_on.title() == "Yes":

        check4 = float(input("Did  you submit assignment every day. Enter the days out of 5?"))

        if check4 == 5:
            print("You are eligible for certificate.")

        elif check4 < 5:
            print("You are not eligible for certificate.")

        else:
            print("Please Enter number between 1 to 5.")


  
    else:
        print("You are not eligible for certificate")


elif check2 < 5:
    print("You are not eligible for certificate.")


else:
    print("Please Enter between the given numbers.")











# choose2 = input("Did  you submit assignment every day. Enter the days out of 5?")

#         if choose2 == 5:
#             print("You are eligible for certificate.")

#         else:
#             print("You are not eligible for certificate.")





