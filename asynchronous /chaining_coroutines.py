import asyncio

# ANSI escape codes for different colors
c = (
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def coroutine1():
    print(f"{c[1]}Coroutine 1: Start{c[0]}")
    await asyncio.sleep(2)  # Simulate an asynchronous operation
    print(f"{c[1]}Coroutine 1: End{c[0]}")
    return "Result from Coroutine 1"


async def coroutine2(data):
    print(f"{c[2]}Coroutine 2: Start{c[0]}")
    await asyncio.sleep(1)  # Simulate another asynchronous operation
    print(f"{c[2]}Received data from Coroutine 1: {data}{c[0]}")
    print(f"{c[2]}Coroutine 2: End{c[0]}")
    return "Result from Coroutine 2"


async def main():
    print(f"{c[3]}Main: Start{c[0]}")
    result_from_coroutine1 = await coroutine1()
    result_from_coroutine2 = await coroutine2(result_from_coroutine1)
    print(
        f"{c[3]}Results from coroutines: {result_from_coroutine1}, {result_from_coroutine2}{c[0]}"
    )
    print(f"{c[3]}Main: End{c[0]}")


# Run the event loop with the main coroutine
asyncio.run(main())
