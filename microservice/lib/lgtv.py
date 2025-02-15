import aiohttp
import asyncio
import json
from contextlib import suppress
from lib.base_logger import logger
from aiowebostv import WebOsClient
from aiowebostv.exceptions import WebOsTvCommandError
from wakeonlan import send_magic_packet

WEBOSTV_EXCEPTIONS = (
    ConnectionResetError,
    WebOsTvCommandError,
    aiohttp.ClientConnectorError,
    aiohttp.ServerDisconnectedError,
    asyncio.CancelledError,
    asyncio.TimeoutError,
)

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,**kwargs)
        return cls._instances[cls]

class LgTV(metaclass=Singleton):
    def __init__(self) -> None:
        with open("./lib/tv_data.json", "r") as file:
            tv_data = json.load(file)

        self.tv_mac_address = tv_data["tv_mac_address"]
        self.tv_ip_address = tv_data["tv_ip_address"]
        self.client_key = tv_data["client_key"]

        self.client = WebOsClient(self.tv_ip_address, self.client_key)
        if self.client.is_registered:
            logger.info("Client is registered")
        else:
            logger.info("Client is not registered")

    async def initiate(self) -> None:
        logger.info("Power on the TV and connecting.")
        if not self.client.is_on:
            logger.info("Client is not on. Switching on")
            await self._power_on()
        # in future check if TV is on and if not then wake_up!
        if not self.client.is_connected():
            logger.info("Client is not connected. Reconnecting")
            with suppress("WEBOSTV_EXCEPTIONS"):
                await self.client.connect()

    def is_on() -> bool:
        return self.client.is_on

    def is_connected() -> bool:
        return self.client.is_connected()

    async def close(self) -> None:
        logger.info("Power off the TV and disconnecting.")
        await self.send_signal("POWER")
        await self.client.disconnect()
    
    async def _power_on(self) -> None:
        """Sends Wake-on-LAN packet to power on LG TV."""
        logger.info("Sending Wake-on-LAN packet...")
        send_magic_packet(self.tv_mac_address)
        await asyncio.sleep(2)  # Wait for TV to boot up before sending further commands
    
    async def send_signal(self, signal: str) -> None:
        logger.info(f"Sending {signal} button pressed.")
        await self.client.button(signal)
        # await asyncio.sleep(2)
    
'''
async def main():
    my_tv = LgTV()
    await my_tv.initiate()
    await my_tv.send_signal("MENU")
    await my_tv.send_signal("DOWN")
    await my_tv.send_signal("DOWN")
    await my_tv.send_signal("DOWN")
    await my_tv.send_signal("HOME")
    await my_tv.send_signal("DOWN")
    await my_tv.send_signal("DOWN")
    await my_tv.send_signal("RIGHT")
    await my_tv.send_signal("RIGHT")
    await asyncio.sleep(20)
    await my_tv.close()

if __name__ == "__main__":
    asyncio.run(main())
'''
