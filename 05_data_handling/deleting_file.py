
'''
a = 1
del(a)
print(a)
'''


#remove items by index
b = [4,8,2,6,1,7,3]
del b[3]
print(b)


#remove an item by value
c = [4,8,2,6,1,7,3]
c.remove(8)
print(c)





#pop : pop will remove the index but the difference is you are able to print the deleted value saperately.
d = [4,8,2,6,1,7,3]
deleted = d.pop(5)
print(d)

print(deleted)





