import asyncio
from multiprocessing import Queue
from lib.lgtv import LgTV
from lib.base_logger import logger

def initiate(queue: Queue):
    logger.info("Starting process to send signals")
    asyncio.run(proceed(queue)) # proceed with buttons comm in async loop

async def proceed(queue):
    logger.info("Process started with message queue")
    tv = LgTV()
    while True:
        msg = queue.get() # reads messages from remote
        if msg != '':
            await tv.initiate()
            await tv.send_signal(msg) # just send signal
        '''
        if not tv.is_on: # tv is not on or not connected
            await tv.initiate()
        else: # both on and connected
            if msg == "POWER": # if signal is power off
                await tv.close()
            else:
                await tv.send_signal(msg) # just send signal
        '''
