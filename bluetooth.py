import asyncio
from bleak import BleakClient, BleakScanner

# async def main():
#     devices = await BleakScanner.discover()
#     for device in devices:
#         print(device)

async def main():
    address = "B90A1F64-B658-2AF1-E638-E2EB9F99875B" # Xsens DOT UUID

    async with BleakClient(address) as client:
        print(client.is_connected) # prints True or False

asyncio.run(main())