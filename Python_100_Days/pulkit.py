# name = "Hi! My name is Pulkit Grover"



# def namer():
#     print("Welcome my friend")


# if __name__ == "__Day1__":
#     namer()
    




# inventory_names = ['plastic','metal','rubber','sheet','paper','glass']
# inventory_numbers = [52,9,56,60,85,42]
###############################################


import random
import string

########### Code
def code(user_input, enc_str):
    store = []
    usr_ipt = user_input.split()
    for a in usr_ipt:

        code1 = ''.join(random.choice(string.ascii_letters) for enc1 in range(enc_str))
        code2 = ''.join(random.choice(string.ascii_letters) for enc1 in range(enc_str))
        
        code = a[-1] + code1 + a[1:-1] + code2 + a[0] 
        store.append(code)
    result = ' '.join(store)
    return result

########### Decode
def decode(user_input1, enc_str):

    store1 = [] 
    usr_ipt1 = user_input1.split()
    for b in usr_ipt1:

        code1 = b[-1] + b[enc_str+1:len(b)-(enc_str+1)] + b[0]
        
        store1.append(code1)
    result = ' '.join(store1)
    return result
    
########### Converter
def converter():
    while True:
        user_code = input("Enter Code or Decode or Quit: ").lower()
        while user_code not in ["code", "decode", "quit"]:
            user_code = input("Please choose correct option- Code or Decode or Quit: ").lower()

        if user_code == "code":
            user_input = input("Please enter your message to code: ")
            cod_str = int(input("Enter the encrytion number: "))
            result = code(user_input, cod_str)
            print(result)

        elif user_code == "decode":
            user_input = input("Please enter your message to decode: ")
            cod_str = int(input("Enter the encryption number: "))
            result = decode(user_input, cod_str)
            print(result)

        elif user_code == "quit":
            break
 
converter()    



