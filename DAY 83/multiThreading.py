import threading
import time 
from concurrent.futures import ThreadPoolExecutor


def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return f"Done with {seconds}s"

def manual_threading_demo():
    print("--- Manual Threading Demo ---")
    time1 = time.perf_counter()

    t1 = threading.Thread(target=func, args=(4,))
    t2 = threading.Thread(target=func, args=(1,))
    t3 = threading.Thread(target=func, args=(3,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    time2 = time.perf_counter()
    print(f"Total time using threads: {time2 - time1:.2f} seconds\n")


def pollingDemo():
    print("--- ThreadPoolExecutor Demo ---")
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 4)
        future3 = executor.submit(func, 1)
        
        print(future1.result())
        print(future2.result())
        print(future3.result())

if __name__ == "__main__":
    manual_threading_demo()
    pollingDemo()