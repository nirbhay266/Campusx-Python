import asyncio
import time

# def main():
#     print("HELLO")
#     time.sleep(4)
#     print("World")

# main()



# Coroutine function
async def main():
    print("HELLO")   # This will print immediately
    await asyncio.sleep(4) # The thread is idle here
    print("World") # This will be excecuted right after the thread is idele

# Run the main coroutine
asyncio.run(main())


