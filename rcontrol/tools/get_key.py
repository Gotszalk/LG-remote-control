import asyncio

from aiowebostv import WebOsClient

# https://github.com/home-assistant-libs/aiowebostv

HOST = "127.0.0.1"
CLIENT_KEY = None

async def main() -> None:
    client = WebOsClient(HOST, CLIENT_KEY)
    await client.connect()

    print(f"Client key: {client.client_key}")

    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())

