
#match case is similler to if, elif and else statement

'''
body = 'sleep'
match body:
    case 'tired':
        print('get some sleep')
    case 'sleep':
        print('i have to wake up')
    case 'hungry':
        print('get some food')
    case 'run':
        print('you should run')
    case _:
        print('your choice')

'''

#EXERCISE

# grade = 8
# match grade:
#     case 1:
#         print('Excelent')
#     case 2:
#         print('best')
#     case 3:
#         print('better')
#     case 4:
#         print('good')
#     case 5:
#         print('fine')
#     case _:
#         print('pass')



# def match_case(grade):

#     match grade:
#         case 1:
#             print('Excelent')
#         case 2:
#             print('best')
#         case 3:
#             print('better')
#         case 4:
#             print('good')
#         case 5:
#             print('fine')
#         case _:
#             print('pass')


# match_case(3)



x = 0

match x:

    case 0:
        print("X is zero")

    case 4 if x % 2 == 1:
        print("x % 2 == 0 and case is 4")

    case _ if x < 10:
        print("x is < 10")

    case _:
        print(x)





