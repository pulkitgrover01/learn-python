


user_input = int(input("Please enter number of apple you want to divide: "))

min_value = int(input("Please give the min range: "))
max_value = int(input("Please give the max range: "))


for i in range(min_value, max_value+1):

    if user_input % i == 0:
        print(f"{i} is a divisor of {user_input}")

    else:
        print(f"{i} is not a divisor of {user_input}")








