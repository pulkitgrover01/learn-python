
#file handling create .txt file in the folder 
#Open and close manually

'''
file = open('test_file_handling.txt')
print(list(file))


#open and close it automatically
with open('testing_file.txt') as custom_name:
    #print(custom_name.read())
    for line in custom_name:
        print(line)




#write some file
with open('new_version.txt','a') as new_file:
    new_file.write('\n ########### write somme ###########')
    
'''

#exercuse
# 1
'''
with open('x_tree.txt','w') as new_tree:
    new_tree.write('\n xxxxxxxx Merry Christmas xxxxxxxx\
                    \n                x\
                    \n               xxx\
                    \n              xxxxx\
                    \n             xxxxxxx\
                    \n            xxxxxxxxx\
                    \n           xxxxxxxxxxx\
                    \n                x\
                    \n                x\
                    \n                x\
                    \n                x')


'''
# 2 This is easy and better way for doing it.
with open('tree2.txt','w') as tree2_file:
    xmas = '''
Welcome to chistmas Party
            x
           xxx
          xxxxx
         xxxxxxx
       xxxxxxxxxxx
            x
            x
            x
            x    '''
    tree2_file.write(xmas)
















   