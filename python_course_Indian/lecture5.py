######################### While and for Loop #######################


# count = 1

# while count <= 6:
#     print(count)
#     count +=1
     

# check = 6

# while check >= 1:
    
#     print(check)
#     check -=1
     






# down = 1

# while down <= 100:
#     print("hello", down)
#     down += 1

# print(down)

#1
#Print number from 1 to 100
# pos_num = 1

# while pos_num <= 100:
#     print(pos_num)
#     pos_num += 1


# print("")

#2
# #Print number from 100 to 1
# neg_num = 100

# while neg_num >= 1:
#     print(neg_num)
#     neg_num -= 1


#3
#Print the multiplication table of a number n.
# number = int(input("Enter your digit: "))

# value = 1
# while value <=10:
#     print(value*number)
#     value +=1


#4
#Print the elements of the following list using Loop:
# nlist = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(nlist):
#     print(nlist[idx])
#     idx += 1


#5
#search for a number x in this tuple using loop:

# listX = (1,4,9,16,25,36,49,64,81,100)
# listy = ("a","r","g","s","j","o","c","k","n")

# serch ="c"

# a = 0
# while a < len(listy):
#     if serch == listy[a]:
#         print("Yes",a)
#     else:
#         print("no", a)

#     a += 1



# a = 0
# while a < 6:
#     print(a)
#     if a ==2:
#         break
#     a += 1




#bucket = [1,5,4,9,6,8,2,1,3]

# a = 0
# while  a < 10:
#     if a == 5:
#         a += 1
#         continue
#     print(a)
#     a += 1




# i = 0
# while i < 20:
#     if i%2 !=0:
#         i += 1
#         continue

#     print(i)
#     i += 1



# nlist = [1,4,9,16,25,36,49,64,16,81,100,16]
# x = 16

# idx = 0
# for check in nlist:
#     if check == x:
#         print("Found     ", idx)
        
#     else:
#         print("not found ", idx)
#     idx += 1
 



# for check in range(1,101):
#     print(check)


# for use in range(100,0,-1):
#     print(use)


# m = 2
# for ans in range(1,11):
#     print(ans * m)


# n = 5

# fact = 1
# for i in range(1, n+1):
#     fact *= i

# print(fact)

# # sum = 1
# i = 1
# while i <= n:
#     sum += i
#     i += 1

# print(sum)



1
# a = 1
# while a < 101:
#     print(a)
#     a += 1

2
# b = 100
# while b > 0:
#     print(b)
#     b -= 1


3
# c = 1
# while c < 11:
#     print(c*5)
#     c += 1


4
# elem = [1,4,9,16,25,36,49,64,81,100]
# d = 0
# while d < len(elem):
#     print(elem[d])
#     d += 1

5
# tup = (1,4,9,16,25,36,49,64,81,100,25)
# find = 25

# e = 0
# while e < len(tup):
#     if find == tup[e]:
#         print("Found it ", e)
#     else:
#         print("not found", e)

#     e += 1


# 6
# sets = (1,4,9,16,25,36,49,64,81,100,25)

# f = 1
# while f < 10:
#     if f == 6:
#         f += 1
#         continue
#     print(f)
#     f += 1


# g = 0
# while g < 20:
#     if g%2 !=0:
#         g += 1
#         continue
#     print(g)
#     g += 1




# h = (1,4,9,16,25,36,49,64,81,100)
# find = 81
# idx = 1
# for h2 in h:
#     if h2 == find:
#         print("found", idx)
        
#     else:
#         print("not found", idx)
    
#     idx += 1

# for i in range(1,101):
#     print(i)


# for j in range(100,0,-1):
#     print(j)


# k1= 2
# for k in range(1,11):
#     print(k*k1)

 



# n=5
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1

# print(sum)

# print("")
# f = int(input("enter value:"))
# fract = 1
# for n in range(1, f+1):
#     fract *= n
# print(fract)
sum = 0
min = 1
while min <= 5:
    sum += min
    min += 1
print(sum)




