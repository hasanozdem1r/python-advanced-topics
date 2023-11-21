import asyncio


class AsyncQueue:

    def __init__(self):
        self.queue = asyncio.Queue()

    async def enqueue(self, item):
        await self.queue.put(item)
        print(f"Enqueued: {item}")

    async def dequeue(self):
        item = await self.queue.get()
        print(f"Dequeued: {item}")
        return item


async def producer(queue):
    for i in range(5):
        await queue.enqueue(i)
        await asyncio.sleep(1)  # Simulate a time-consuming task


async def consumer(queue):
    for _ in range(5):
        item = await queue.dequeue()
        await asyncio.sleep(2)  # Simulate processing of the item


async def main():
    queue = AsyncQueue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(producer_task, consumer_task)


# Run the event loop with the main coroutine
asyncio.run(main())
