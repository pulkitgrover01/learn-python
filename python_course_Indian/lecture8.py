# class Student:
#     name = "Pulkit"

# s1 = Student
# print(s1.name)

# s2 = Student
# print(s2.name)

# class plane:                                 # Class
    
#     collage = "DU"
# #.....................................
#     def __init__(self, name, marks):
#         self.name = name                     # Constructor
#         self.marks = marks
# #.....................................
#     def welcome(self):
#         print("Welcome student:", self.name)  # Methods

#     def get_marks(self):
#         return self.marks
# #...................................      


# #...................................................
# p1 = plane("Pulkit",89,)
# print("Name is:",p1.name,"and marks is:", p1.marks)

# p2 = plane("Raman", 78,)
# print("Name is:",p2.name,"and marks is:", p2.marks)         # Object


# p1.welcome()

# print(p2.get_marks())
# #..........................................................



# class student:
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val

        
            

#         print(f"Hi {self.name}.\nYou scored in:\nMath: {self.marks[0]}\nPhysics: {self.marks[1]}\nChem: {self.marks[2]}\
#               \nEnglish: {self.marks[3]}\nBiology: {self.marks[4]}\nYour total: {sum}\nAvg score is: {sum/5}")

    
# s1 = student("Pulkt",[78,94,86,75,92])
# s1.get_avg()



# class cars:
    
#     def __init__(self,brand,color,numbers):
#         self.brand = brand
#         self.color = color
#         self.numbers = numbers

#     @staticmethod
#     def hello():
#         print("Hello Guys")

        
#     def get_num(self):
#         var = 0
#         for num in self.numbers:
#             var += num
        

#         print(f"Car Brand:{self.brand}\nCar Color:{self.color}\ncarL:{self.numbers[0]}\nTotal:{var}")


# c1 = cars("Ford","Yellow",[46,8,55,72,16])
# c1.get_num()
# c1.hello()






# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.acc = True

#         print("Car is started...")




# Jaguar = car()
# Jaguar.start()




# class Account:
#     def __init__(self,name, bal, Acc):
#         self.name = name
#         self.balance = bal
#         self.account_no = Acc
        
# #debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print(f"Dear {self.name}. \nYour account no: {self.account_no}. \nRs: {amount} was debited. \nRemaining amount is Rs: {self.balance}")
       

# #credited amount
#     def credit(self, amount):
#         self.balance += amount
#         print(f"Dear {self.name}. \nYour account no: {self.account_no}. \nRs: {amount} was credited. \nRemaining amount is Rs: {self.balance}")



# #total balance
#     def total_bal(self):
#         return self.balance

   

# p1 = Account("Pulkit",10000, 12345)
# p1.debit(500)
# p1.credit(1000)
# p1.credit(50000)


# p2 = Account("Ranu", 456, 789456)
# p2.debit(500)




class account:

    def __init__(self,nam,acc,bal):
        self.name = nam
        self.account = acc
        self.balance = bal

        print("")

    def debit(self, amount):
        self.balance -= amount
        print(f"Dear {self.name}.\nYour accout no: {self.account}.\nDebited amount: {amount}.\nTotal amount: {self.balance}")

        print("")

    def credit(self, amount):
        self.balance += amount
        print(f"Dear {self.name}.\nYour accout no: {self.account}.\nCredited amount: {amount}.\nTotal amount: {self.balance}")

        print("")

    def total_amt(self):
        return self.balance


    

c1 = account("Pulkit", 75420689, 62000)
c1.debit(500)
c1.credit(5500)


# c2 = account("Lakshya", 45989515, 75600)
# c2.debit(1200)
# c2.credit(5600)





















