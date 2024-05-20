
test_string = 'i am aman'
test_list = [1,2,3,4]


'''
#turning a string into a list/tuple
print(test_string.split())
print(list(test_string))
print(tuple(test_string))


#turning list/tuple into a string
print(''.join(['i' ,'am', 'aman']))

print(str(test_list))


#indexing on strings
print(test_string[2:4])

'''

#exercise

exercise = [1,2,3,4,5,6,7]

result = str(exercise).strip('[]').replace(',','').replace(' ','')
print(result)







