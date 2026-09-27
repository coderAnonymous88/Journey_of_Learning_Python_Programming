import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n * 5

print(fx(20))
print("This is Done for 20")
print(fx(6))
print("This is Done for 6")
print(fx(100))
print("This is Done for 100")


print(fx(20))
print("This is Done for 20")
print(fx(6))
print("This is Done for 6")
print(fx(100))
print("This is Done for 100")

