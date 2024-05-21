
#list unpacking
'''
def myside(first, *yourside,): 
    print(first)
   
    for car in yourside:
        print(car)
   

myside(1,2,3,4,'heya',5,23, 42)



def ever_more(*args, **kwargs):
    print(args)
    print(kwargs)

ever_more(1,2,3 ,5,8,'palygame', 78,'hawayii',slow = 5, test = 2, run = 2)


'''


#elxecise
def best_calculator(*args):
    print(sum(args))
    print(min(args))
    print(max(args))
    print(min(args))
    
best_calculator(5,10,20)
















