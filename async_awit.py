

# asyncio allows asynchronous programming without blocking, useful for I/O-bound tasks.
# async declares a coroutine, and await pauses the coroutine until the awaited task completes.
# asyncio.create_task() schedules a task to run but doesn't wait for it unless you explicitly await it.
# In your case, the tasks started but weren't awaited, so the program exited before they completed, which is why the latter prints didn't appear.


# 1.0.6 await multiple tasks
import asyncio

async def file_return():
    print("3")
    # await asyncio.sleep(1)
    print("4")
    return (f"File returned")


async def email_reply():
    print("1")
    # await asyncio.sleep(3)
    print("2")
    return (f"How you doing?")


async def task1():
    print("Waiting for reply...")
    x = await email_reply()
    print(f"Email Reply: {x}")


async def task2():
    print("Waiting for file...")
    x = await file_return()
    print(f"File returned: {x}")


async def main():

    # asyncio.create_task(task1())
    # asyncio.create_task(task2())

    # await asyncio.gather(task1(),task2())

    test = asyncio.create_task(task1())
    test2 = asyncio.create_task(task2())

    await test
    await test2

asyncio.run(main())