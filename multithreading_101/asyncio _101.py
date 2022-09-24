import asyncio
import time


# Section 1
async def sum(x1: int, x2: int) -> None:
    print(f"Sum of {x1} and {x2} is calculating...")
    await asyncio.sleep(1)
    print(f"Sum of {x1} and {x2} is {x1+x2}")


# calling a async function -> running a coroutine way 1
asyncio.run(sum(x1=14, x2=16))


# Section 2
async def say_message_after(delay: int, message: str) -> None:
    await asyncio.sleep(delay)
    print(message)


async def call_say_hello():
    print(f"started at {time.strftime('%X')}")
    # calling a async function -> running a coroutine way 2
    await say_message_after(1, "hello")
    await say_message_after(1, "hola")
    print(f"finished  at {time.strftime('%X')}")


# call call_say_hello
asyncio.run(call_say_hello())


async def call_say_hello():
    t1 = asyncio.create_task(say_message_after(1, "merhaba"))
    t2 = asyncio.create_task(say_message_after(1, "Привет"))
    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await t1
    await t2

    print(f"finished at {time.strftime('%X')}")


# call call_say_hello
asyncio.run(call_say_hello())
