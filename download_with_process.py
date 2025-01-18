import requests
import multiprocessing

def downalder(url, queue, index):
    json_text = requests.get(url).json()
    json_len = len(str(json_text))
    print("Process " + str(index) + " Downloaded " + str(json_len) + " chars from " + str(url))
    queue.put(json_len)
        
def main():
    queue = multiprocessing.Queue()
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
           ]
    processes = []
    for index, url in  enumerate(urls):
        process = multiprocessing.Process(target = downalder, args = (url, queue, index,))
        process.start()
        processes.append(process)
        
        
    
    for process in processes: 
        process.join()
    
    queue_sum = 0
    for process in processes:
        queue_sum +=  queue.get()  
    print("Total numbers of chars dowanloaded is " + str(queue_sum))    
    
if __name__ == "__main__":
     main()    
