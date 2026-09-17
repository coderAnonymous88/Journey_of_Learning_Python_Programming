import time
# def usingWhileLoop():
#     i = 0
#     while(i<100):
#         i = i + 1
#         print(i)

# def usingForLoop():
#     for i in range(100 + 1):
#         print(i)

# init = time.time()
# usingForLoop()
# t1 = time.time() - init
# init = time.time()
# print(t1)
# usingWhileLoop()
# print(time.time() - init)



# print(3)
# time.sleep(3)
# print("This text is printed in 3 seconds so keep patience")



t = time.localtime()
formatedTime = time.strftime("%Y-%m-%d %H:%M:S", t)
print(formatedTime)