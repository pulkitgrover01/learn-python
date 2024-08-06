
############################################################################# All together Random image download from internet


import multiprocessing
import requests
import time

start = time.time()

def download_file(url, name):
    
    print(f"Started downloading {name}")
    response = requests.get(url)
    open(f"Files2/file{name}.jpg","wb").write(response.content)
    print(f"Finished downloading {name}")
    
    
  
if __name__ == '__main__':
    url = "https://picsum.photos/2000/3000"

    pros = []

    for index,_ in enumerate(range(50), start=1):
        p = multiprocessing.Process(target=download_file, args= [url, index])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

finish = time.time()
t_time = finish - start
print(t_time)


############################################################################# one by one Random image download from internet


# import requests
# import time

# start = time.time()

# def download_file(url, name):
    
#     print(f"Started downloading {name}")
#     response = requests.get(url)
#     open(f"Files2/file{name}.jpg","wb").write(response.content)
#     print(f"Finished downloading {name}")
    

# url = "https://picsum.photos/2000/3000"


# for index,_ in enumerate(range(50), start=1):
#     download_file(url, index)
        

# finish = time.time()
# t_time = finish - start
# print(t_time)
















