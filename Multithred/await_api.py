# Normal sync API calls

# import time
# def api_call():
#     time.sleep(4)
#     return "Data Fetch"

# def execute():
#     print("Executing API Call")
#     result= api_call()
#     print("Data Fetched ",result)

# execute()

import asyncio

async def api_call():
    await asyncio.sleep(4)
    return "Order data"

async def execute():
    print("Executing API Call")
    result = await api_call()
    print("Data Fetched : ",result)

asyncio.run(execute())



