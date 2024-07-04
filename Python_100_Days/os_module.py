

import os

list = ["Assets","Edits","Render"]
list2 = ["File1","File2","File3"]
list3 = ["Play1","Play2","Play3"]


# if not os.path.exists("SWH_Remake_Start"):
#     os.mkdir("SWH_Remake_Start")



# i = 0
# if not os.path.exists(f"SWH_Remake_Start/{list[i]}/{list2[i]}/{list3[i]}"):
#     os.mkdir(f"SWH_Remake_Start")
#     while i < len(list):
#         os.mkdir(f"SWH_Remake_Start/{list[i]}")
#         os.mkdir(f"SWH_Remake_Start/{list[i]}/{list2[i]}")
#         os.mkdir(f"SWH_Remake_Start/{list[i]}/{list2[i]}/{list3[i]}")
#         i += 1


# print("Hello")

""""""""""""""""""""""""""""""""""""""""""""""""""""""
i = 1
if not os.path.exists("Data_Testing"):
    os.mkdir("Data_Testing")

#To create folder in folder
# if not os.path.exists(f"Data_Testing/Day{i}"):
#     for i in range(1,101):
#         os.mkdir(f"Data_Testing/Day{i}")

#To rename the folder
# for i in range(1,101):
#     os.rename(f"Data_Testing/Classes {i}", f"Data_Testing/Places {i}")
print(os.getcwd())

print("Hello")


