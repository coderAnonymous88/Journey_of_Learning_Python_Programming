import time
import asyncio
import requests


async def function1():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('google1.ico', 'wb').write(r.content)
    # time.sleep(3)
    # await asyncio.sleep(1)
    print("This is Function 1")
    return "anonymousCoder"

async def function2():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('google2.ico', 'wb').write(r.content)
    # time.sleep(3)
    # await asyncio.sleep(1)
    print("This is Function 2")

async def function3():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('google3.ico', 'wb').write(r.content)
    # time.sleep(3)
    # await asyncio.sleep(4)
    print("This is Function 3")


async def  main():
    Task = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(Task)
    # task = asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()

asyncio.run(main())