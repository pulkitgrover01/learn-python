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
#               \nEnglish: {self.marks[3]}\nBiology: {self.marks[4]}\nYour total: {sum}\nAvg score is: {sum/len(self.marks)}")

    
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




# class account:

#     def __init__(self,nam,acc,bal):
#         self.name = nam
#         self.account = acc
#         self.balance = bal

#         print("")

#     def debit(self, amount):
#         self.balance -= amount
#         print(f"Dear {self.name}.\nYour accout no: {self.account}.\nDebited amount: {amount}.\nTotal amount: {self.balance}")

#         print("")

#     def credit(self, amount):
#         self.balance += amount
#         print(f"Dear {self.name}.\nYour accout no: {self.account}.\nCredited amount: {amount}.\nTotal amount: {self.balance}")

#         print("")

#     def total_amt(self):
#         return self.balance


    

# c1 = account("Pulkit", 75420689, 62000)
# c1.debit(500)
# c1.credit(5500)


# c2 = account("Lakshya", 45989515, 75600)
# c2.debit(1200)
# c2.credit(5600)


# class bike:

#     def __init__(self,ownr,nam,colr,numb):
#         self.owner = ownr
#         self.name = nam
#         self.color = colr
#         self.number = numb


    

# b1 = bike("Pulkit Grover","Scrambler","Green",8523)
# print(f"owner name:{b1.owner}\nBike name:{b1.name}\nBike color:{b1.color}\nBike number:{b1.number}")


# b2 = bike("Raj Kumar","splender+","Black",8711)
# print(f"owner name:{b2.owner}\nBike name:{b2.name}\nBike color:{b2.color}\nBike number:{b2.number}")



#Bank calculater

# class bank:

#     def __init__(self,bank,name,balance):
#         self.bank = bank
#         self.name = name
#         self.balance = balance

#     def debit(self, amount):
#         self.balance -= amount
#         print(f"Hey {self.name}. Your bank {self.bank} account Rs.{amount} has been debited. Your remaing amount {self.balance}.")

#     def credit(self, amount):
#         self.balance += amount
#         print(f"Hey {self.name}. Your bank {self.bank} account Rs.{amount} has been credited. Your remaing amount {self.balance}.")

#     def total_amount(self):
#         return self.balance



# c1 = bank("HDFC","Pulkit",7500)
# c1.debit(500)
# c1.credit(1000)






#class result

# class student:
    
#     def __init__(self, nam, rol, rslt):
#         self.name = nam
#         self.roll_no = rol
#         self.result = rslt

#     def t_result(self):
#         sum = 0
#         for val in self.result:
#              sum += val
#              return


#         print(f"Hello {self.name} \nRoll no: {self.roll_no}.\nYou scored:\nMath:{self.result[0]}\nScience:{self.result[1]}\nChemestry:{self.result[2]}\
#               \neconomic:{self.result[3]}\nEnglish:{self.result[4]}\nTotal score: {sum}/500\nAverage_score: {sum/5}")



# s1 = student("Pulkit", 22, [75,84,56,79,94])
# s1.t_result()

























