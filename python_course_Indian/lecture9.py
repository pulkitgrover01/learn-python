# # #Bank calculater

# class bank:

#     def __init__(self,bank,name,balance):
#         self.bank = bank
#         self.name = name
#         self.balance = balance

    
#     def debit(self, amount):\
        
#         self.balance -= amount
        
#         # print(f"Hey {self.name}. Your bank {self.bank} account Rs.{amount} has been debited. Your remaing amount {self.balance}.")
 
#     def credit(self, amount):
        
#         self.balance += amount
        
#         # print(f"Hey {self.name}. Your bank {self.bank} account Rs.{amount} has been credited. Your remaing amount {self.balance}.")
   
#     def total_amount(self):
#         return self.balance


# c1 = bank("HDFC","Pulkit",7500)
# c1.debit(500)
# c1.credit(1000)


# class branch(bank):
#     def __init__(self, bank, name, balance, mobile):
#         super().__init__(bank, name, balance)
#         super().debit(amount)
#         self.mobile = mobile
        

#         print(f"Hey {self.name}. Your mobile_no: {self.mobile} Your bank {self.bank} account Rs.{amount} has been debited. Your remaing amount {self.balance}.")
    
    
# b1 = branch("SBI","Sandeep",2300,7045266)
# b1.debit(3000)






#priviate

# class play:
#     def __init__(self, name, car):
#         self.name = name
#         self.__car = car

#     def __check_Car(self):
#         print(self.__car)

#     def render(self):
#         self.__check_Car()

 


# d1 = play("mazda","sportssssss")
# print(d1.name)
# print(d1.render())

 

#usage of property decorator


# class student:

#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         # self.prsntge = str((self.phy + self.chem + self.math) / 3) + "%"

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"

    

# stu1 = student(78,94,86)
# print(stu1.math)
# # print(stu1.prsntge)
# print(stu1.percentage)
# stu1.math = 11
# print(stu1.math)
# # print(stu1.prsntge)
# print(stu1.percentage)




# class complex:

#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +", self.img,"j")
#         print("")

#     def __add__(self, p2):
#         newReal = self.real + p2.real
#         newImg = self.img + p2.img
#         return  complex(newReal, newImg)
    
#     def __sub__(self,p2):
#         newReal = self.real - p2.real
#         newImg = self.img - p2.img
#         return complex(newReal, newImg)
    
#     def __mul__(self, p2):
#         newReal = self.real * p2.real
#         newImg = self.img * p2.img
#         return complex(newReal, newImg)
    
# p1 = complex(1, 4)
# p1.showNumber()

# p2 = complex(2, 8)
# p2.showNumber()

# p3 = p1 + p2
# p3.showNumber()

# p4 = p1 - p2
# p4.showNumber()

# p5 = p1 * p2
# p5.showNumber()



#area of circle
# class circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius **2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius



# c = circle(11)
# print(c.area())
# print(c.perimeter())



#area of a triangle
# class triangle:
#     def __init__(self,base , height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return .5 * self.base * self.height



# a = triangle(5,6)
# print(a.area())


#Employee

# class employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

    
#     def showEmDetails(self):
#         print(f"Designation= {self.role}\nDepartment= {self.department}\nSalary= {self.salary}")



# class engineer(employee):
#     def __init__(self, name, age, role, department, salary):
#         super().__init__(role, department, salary)
#         self.name = name
#         self.age = age

#     def showEnDetails(self):
#         print("")
#         print(f"Name= {self.name}\nAge= {self.age}\nDesignation= {self.role}\nDepartment= {self.department}\nSalary= {self.salary}")
        

# class business(employee):
#     def __init__(self, name, age):
#         super().__init__("Owner", "Shop", "1,50,000")
#         self.name = name
#         self.age = age

#     def showBuDetails(self):
#         print("")
#         print(f"Name= {self.name}\nAge= {self.age}\nDesignation= {self.role}\nDepartment= {self.department}\nSalary= {self.salary}")

# a1 = employee("Animator", "Creative", "1,00,000") 
# a1.showEmDetails()

# en1 = engineer("Lakshya", 29, "Engineer", "Technical", "1,20,000")
# en1.showEnDetails()

# print("New")
# b1 = business("Raj Kumar", 54)
# b1.showBuDetails()



class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, o2):
        return self.price > o2.price



o1 = order("Bujeya", 60)
o2 = order("Baverage", 20)

print(o1 > o2)

































