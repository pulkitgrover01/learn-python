
# 1. Create a Simple Calculator (5 Marks)

# while True:
#     a = int(input("Enter first value: "))
#     b = int(input("Enter first value: "))
#     calc_sign = input("Enter Arithmetic Operators: ")

#     if calc_sign == "+":
#         output = a + b
#         print(f"Total of {a} and {b} is: {output}")

#     elif calc_sign == "-":
#         output = a - b
#         print(f"Subtract of {a} and {b} is: {output}")

#     elif calc_sign == "*":
#         output = a * b
#         print(f"Multiplication of {a} and {b} is: {output}")

#     elif calc_sign == "/":
#         output = a / b
#         print(f"Division of {a} and {b} is: {int(output)}")

#     elif calc_sign == "%":
#         output = a % b
#         print(f"Division of {a} and {b} is: {int(output)}")

#     elif calc_sign == "**":
#         output = a ** b
#         print(f"Division of {a} and {b} is: {int(output)}")




# 2. Temperature Converter (5 Marks)

# def C_to_F():
#     c = int(input("Enter Cencius number: "))
#     f = c * 9/5 + 32
#     return f
    

# output = C_to_F()
# print(output)



# 3. Grade Calculator (5 Marks)


def subject_score():
    math = int(input("Math Marks : "))
    physics = int(input("Physics Marks : "))
    chem = int(input("Chem Marks : "))
    english = int(input("English Marks : "))
    hindi = int(input("Hindi Marks : "))

    sum = (math + physics + chem + english + hindi ) / 5
    return sum
    

def grade_Calculator(score):
    if score >= 90:
        return "Grade A"

    elif score >= 80 and score < 90:
        return "Grade B"

    elif score >= 70 and score < 80:
        return "Grade C"

    else:
        return "Grade D"


def output_Calculator():

    avg_score = subject_score()
    print(f"Total avg score: {avg_score}")
    
    result = grade_Calculator(avg_score)
    print(f"you got: {result}")


output_Calculator()
















