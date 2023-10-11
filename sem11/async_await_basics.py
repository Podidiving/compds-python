import asyncio
import time


async def print_something_bad(something):
    time.sleep(2)
    print(something)


async def main_bad():
    start = time.time()
    await print_something_bad("blabla")
    await print_something_bad("blabla2")
    await print_something_bad("blabla3")
    end = time.time()
    print(end - start)


async def print_something(something):
    await asyncio.sleep(2)
    print(something)


async def main_bad2():
    start = time.time()
    await print_something("blabla")
    await print_something("blabla2")
    await print_something("blabla3")
    end = time.time()
    print(end - start)


async def main1():
    start = time.time()
    tasks = []
    tasks.append(print_something("blabla"))
    tasks.append(print_something("blabla2"))
    tasks.append(print_something("blabla3"))
    for task in asyncio.as_completed(tasks):
        await task

    end = time.time()
    print(end - start)


async def main2():
    start = time.time()
    tasks = []
    # https://docs.python.org/3/library/asyncio-task.html#asyncio.Task
    tasks.append(asyncio.create_task(print_something("blabla")))
    tasks.append(asyncio.create_task(print_something("blabla2")))
    tasks.append(asyncio.create_task(print_something("blabla3")))
    for task in asyncio.as_completed(tasks):
        await task

    end = time.time()
    print(end - start)


async def main():
    start = time.time()
    tasks = []

    # https://docs.python.org/3/library/asyncio-task.html#asyncio.Task
    tasks.append(print_something("blabla"))
    tasks.append(print_something("blabla2"))
    tasks.append(print_something("blabla3"))

    await asyncio.gather(*tasks)

    end = time.time()
    print(end - start)


if __name__ == "__main__":
    asyncio.run(main())
