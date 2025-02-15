from fastapi import FastAPI
from lib.lgtv import LgTV

app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "FastAPI microservice - signal sender"}

@app.get("/signal/{signal}")
async def read_signal(signal: str):
    tv = LgTV()
    if signal != '':
        await tv.initiate()
        await tv.send_signal(signal)
        message = f"Received {signal}"
        return message
'''
async def main() -> None:
    tv = LgTV()

    sig_event = asyncio.Event()
    signal.signal(signal.SIGINT, lambda _exit_code, _frame: sig_event.set())

    while not sig_event.is_set():
        await asyncio.sleep(1)

        now = datetime.now(UTC).astimezone().strftime("%H:%M:%S")[:-3]
        is_connected = tv.is_connected()
        is_on = tv.is_on()

        logger.info(f"[{now}] Connected: {is_connected}, Powered on: {is_on}")

        if is_connected:
            continue

        with suppress(*WEBOSTV_EXCEPTIONS):
            await tv.connect

    await tv.close()

if __name__ == "__main__":
    asyncio.run(main())
    '''
