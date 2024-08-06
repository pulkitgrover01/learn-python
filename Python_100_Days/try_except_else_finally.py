#this will Run normally.
with open("Projects/Health_Managemant_Project/Pulkit Grover_Food.txt") as a:            
    print(a.read())

#we use try if we are not sure if the code will work or not.
try:
    with open("Pulkit Grover_Food.txt") as b:
        print(b.read())

#if the code does not work given in try then except will throw the error let rest of the code will run.
except Exception as e:
    print(e,"File doesnt exist")

#if the code works given in try then except will not trigger and instead of that else will work and let rest of the code will run.
else:
    print("Exception didn't run")

#It does not matter if the code in try will work or not finally will work and let rest of the code will run.
finally:
    print("Don't know if second file exist.")

print("Am I inproving?")















