
# import asyncio


# async def func1():
#     await asyncio.sleep(9)
#     print("Func1 in running")
#     return "Pulkit"

# async def func2():
#     await asyncio.sleep(6)
#     print("Func2 in running")
#     return "Grover"

# async def func3():
#     await asyncio.sleep(3)
#     print("Func3 in running")
#     return "Raj Kumar"

# # async def main():
# #     task1 = asyncio.create_task(func1())
# #     task2 = asyncio.create_task(func2())
# #     task3 = asyncio.create_task(func3())


# #     await task1
# #     await task2
# #     await task3

# # asyncio.run(main())

# ######################################################### another way to run fuction
# async def main():
#     L = await asyncio.gather(func1(), func2(), func3())
#     print(L)
  
# asyncio.run(main())

#################################################################################################

# import requests
# import asyncio

# url = "https://picsum.photos/4000/5000"

# async def download_file(url, name):
     
#     print(f"Downloading Started")
#     response = requests.get(url)
#     open(f"Files2/file{name}.jpg","wb").write(response.content)
#     print(f"Downloading Finished")
#     return f"Image: File{name} is downloaded"

# async def download_file1(url, name):
     
#     print(f"Downloading Started")
#     response = requests.get(url)
#     open(f"Files2/file{name}.jpg","wb").write(response.content)
#     print(f"Downloading Finished")
#     return f"Image: File{name} is downloaded"

# async def download_file2(url, name):
     
#     print(f"Downloading Started")
#     response = requests.get(url)
#     open(f"Files2/file{name}.jpg","wb").write(response.content)
#     print(f"Downloading Finished")
#     return f"Image: File{name} is downloaded"




# async def main():
#         L = await asyncio.gather(download_file(url, "file"), download_file1(url, "file1"), download_file2(url, "file2"))
#         # print(L)
  
# asyncio.run(main())


import asyncio

async def fetch_data():
    # await asyncio.sleep(2)  # Simulate an I/O-bound task
    print("Data1")

async def fetch_data1():
    # await asyncio.sleep(4)  # Simulate an I/O-bound task
    print("Data2")

async def main():
    tasks1 = [fetch_data() for _ in range(5)]
    tasks2 = [fetch_data1() for _ in range(5)]

    await asyncio.gather(*tasks1, *tasks2)
  

asyncio.run(main())























