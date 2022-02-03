import time
import asyncio

async def printer(arr):
    timer = 1
    for c in arr:
        time.sleep(timer)
        print(c)
        timer *= 2


if __name__ == '__main__':
    arr = input().split()
    asyncio.run(printer(arr))