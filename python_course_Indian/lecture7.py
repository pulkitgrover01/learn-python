# # with open("practice.txt","w") as f:
# #     show =  f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
    
  
# with open("practice.txt","r") as f:
#     show = f.read()

# new_show = show.replace("Java","Python")
# print(new_show)


# with open("practice.txt","w") as f:
#     f.write(new_show)



# #write
# with open("second_try.txt","w") as w:
#     wri = w.write("I am gonna test my knowledge")

# #read
# with open("second_try.txt","r") as w:
#     red = w.read()

# print(red)

# #replace
# with open("second_try.txt","r") as w:
#     rep = w.read()

#     check = rep.replace("knowledge","skills")

# print(check)

# #update in txt
# with open("second_try.txt","w") as w:
#     w.write(check)

#Find the word using function 
# def check_word(i):
#     with open("second_try.txt","r") as w:
#         check = w.read()
#         if check.find(i) != -1:
#             print("Found")

#         else:
#             print("not found")


# check_word("am")


# def CWIL(chk):
    
#     data = True
#     line_no = 1
#     with open("second_try.txt","r") as c:
#         while data:
#             data = c.readline()
#             if chk in data:
#                 print(f"Word '{chk}' exist in '{line_no}' line.")
#                 return
         
#             line_no += 1

#     return "not found"   


# print(CWIL("gonna"))

 


with open("numbers.txt","w") as n:
    num = n.write("1,2,76,84,90,101")

counter = 0
with open("numbers.txt","r") as n:
    spl = n.read()
    print(spl)

    oddeven = spl.split(",")
    print(oddeven)

    for check in oddeven:
        if int(check) %2 == 0:
            counter  += 1
            
print(counter)






