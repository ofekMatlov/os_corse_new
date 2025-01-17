import requests
import threading
COUNTERS = []
def downalder(url, index, mutex):
    json_text = requests.get(url).json()
    with mutex:
        json_len = len(str(json_text))
        print("thread " + str(index) + " Downloaded " + str(json_len) + " chars from " + str(url))
        COUNTERS.append(json_len)
        return COUNTERS
      
     
def main():
    mutex = threading.Lock() 
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
        ]
    thread_list = []
    for index, url in enumerate(urls):
        thread = threading.Thread(target = downalder, args = (url, index, mutex,))
        thread.start()
        thread_list.append(thread)
        
    for thread in thread_list:
        thread.join() 
    
    sum =0 
    for thread_count in COUNTERS:
        sum += thread_count

    print("Total numbers of chars dowanloaded is " + str(sum))
    
if __name__ == "__main__":
     main()    
