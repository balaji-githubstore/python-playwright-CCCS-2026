import asyncio


async def demo_run():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(1)

    return "work done"


async def main():
    # It creates a coroutine object whereas in typescript it will trigger demo_run() methods and moves on
    output = demo_run()
    print("some other task 1")
    print("some other task 2")
    print("some other task 3")
    print("some other task 4")

    result = await output

    print(result)

# Start Python's asyncio event loop and run main() until it finishes.
asyncio.run(main())