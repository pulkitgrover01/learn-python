
'''
list1 = [5,1,3,8,9,4,6]

print(sorted(list1)[::-1])

print(sorted(list1, reverse = True))




############################################ Sorting dectionery #################################

list2 = [('a',3),('b',10),('c',6),('d',5)]
def digits(item):
    return item[1]

print(sorted(list2, key = digits))

print(sorted(list2, key = lambda item: item[1]))


#exercise

inventory_names = ['plastic','metal','rubber','sheet','as','glass']
inventory_numbers = [52,9,56,60,85,42]
combined_list = zip(inventory_names,inventory_numbers)

sorted_by_digit = sorted(combined_list, key = lambda inv: inv[1])
print(sorted_by_digit)


sorted_by_name = sorted(combined_list, key = lambda invr: len(invr[0]))
print(sorted_by_name)


'''
#Revisions

a = [5,2,9,8,4,3,6]
#print(sorted(a))
a.sort()
print(a)

#reverse the order of the list by useig '[::-1]' or using this argument 'reverse = True'
print(a[::-1])


#dictionary list sorted

list2 = [('a',3),('b',10),('c',6),('d',5)]
def sorting_function(items):
    return items[1]
print(sorted(list2, key=sorting_function))

















