import requests
import threading

counters = []  

def downalder(url, index, urls):
    json_text = requests.get(url).json()
    json_len = len(str(json_text))
    counters.append(json_len)
    print("Threads " + str(index) + " Downloaded " + str(json_len) + " chars from " + str(urls[index]))
    return counters
            
     
def main(): 
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
        ]
    threads_list = []
    for index, url in enumerate(urls):
        threads = threading.Thread(target = downalder, args = (url, index, urls,))
        threads.start()
        threads_list.append(threads)
        

    sum = 0
    for threads in threads_list:
        threads.join() 
    for i in counters:
        sum = sum + i  

    print("Total numbers of chars dowanloaded is " + str(sum))    
    
if __name__ == "__main__":
     main()    
