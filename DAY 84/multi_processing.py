import os
# import multiprocessing
import requests
import concurrent.futures

def downloadImages(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    
    
    os.makedirs("files", exist_ok=True)
    
    
    with open(f"files/{name}.jpg", "wb") as f:
        f.write(response.content)
        
    print(f"Finished Downloading {name}")

if __name__ == '__main__':
    url = "https://picsum.photos/200/300"
    pros = []
    
    # for i in range(5):
    #     p = multiprocessing.Process(target=downloadImages, args=(url, i))
    #     p.start()
    #     pros.append(p)

    # for p in pros:
    #     p.join()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(50)]
        l2 = [i for i in range(50)]
        results = executor.map(downloadImages , l1 , l2)
        for r in results:
            print(r)