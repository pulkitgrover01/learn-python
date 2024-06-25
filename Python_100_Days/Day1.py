
# def f_for(num):
#     for number in num:
#         print("For",number)


# numbers = [1, 2, 3, 4, 5]
# f_for(numbers)




# def f_for(*num):
#     # print(type(num))
#     for number in num:
#         print("For",number)
        


# # numbers = [1, 2, 3, 4, 5]
# f_for(1, 2, 3, 4, 5)




# numbers = [1, 2, 3, 4, 5]
# index = 0
# while index < len(numbers):
#     print("While",numbers[index])
#     index += 1

# #Function
# def f_while(listes):
#     i = 0
#     while i < len(listes):
#         print(f"while {listes[i]}")
#         i += 1

# f_while([1, 2, 3, 4, 5])


# def hello_loop(num1 = 10, num2 = 20 ):
#     i = 1
#     print("Yes",i)
#     while i < num1:
#         i += 1
#         if i == 4:
#             continue
#         elif i == 5:
#             continue
#         elif i == 6:
#             continue
#         print("Hello",i)


#     else:
#         while i <= num2:
#             i += 1
#             if i == 12:
#                 continue
#             elif i == 16:
#                 break
        
#             print("One more loop",i)


#     print("---------------You are learning---------------")
# hello_loop(num1 = 5, num2 = 30)



# def num_Table(number):
#     for i in range(1,15):
#         print("5*",i,"=",5*i)
#         if i == 5:
#             print("Removed 5")
#             continue
#         elif i == 11:
#             break
#         print(f"{number}* {i} = {number * i}")



# num_Table(5)




# def average(*number):
#     sum = 0
#     for i in number:
#         sum += i
#     return sum / len(number)


# c= average(2,4,6)

# print(c)


# import this




# def find_Factorial(n):
#     if n == 0 or n == 1:
#         return 1
    
#     else:
#         return n * find_Factorial(n-1)


# print(find_Factorial(4))


# def fibonacci_seq(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci_seq(n-1) + fibonacci_seq(n-2)



# print(fibonacci_seq(7))



# test_dictionary = {'a' : 123, 1 : True, "b" : 456, 'AB' : 'lets see'}


# for key, value in test_dictionary.items():
#     print(f"your Key: {key} and values: {value}")

# else:
# #     print("Done")




# for i in range(10):
#     print(f"iteration no {i+1} in for loop")
#     # if i > 5:
#     #     break

# else:
#     print("else block in loop")

# print("Out of loop")






# x = int(input("Enter number: "))
# try:
#     num = [4,6,8]
#     print(num[x])

#     print(x + 5)

# except NameError:
#     print("Name not defined")

# except TypeError:
#     print("Typing error")

# except IndexError:
#     print("There is an index error")

# else:
#     print("something")















# while True:
#     a =  input("Entr the value between 5 and 9: ")

#     if "quit" == a:
#         print("You are out of program now.") 
#         break
        

#     a = int(a)
#     if 5 <= a <= 8:
#         print("Yes! Sir")
#         break


#     else:
#         raise ValueError("Value should be between 5 and 9")
#     # raise Exception ValueError TypeError IndexError NameError 






