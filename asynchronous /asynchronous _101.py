import asyncio


async def is_dividable_to_3(number: int):
    total = sum([int(i) for i in str(number)])
    if total % 3 == 0 and total >= 3:
        return True
    else:
        return False


if __name__ == '__main__':
    print(asyncio.run(is_dividable_to_3(0)))
