import asyncio
from fastapi import FastAPI
from lib.lgtv import LgTV

app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "FastAPI microservice - sender"}

@app.get("/signal/{signal}")
async def read_signal(signal: str):
    tv = LgTV()
    if signal != '':
        await tv.initiate()
        await tv.send_signal(signal)
        message = f"Received {signal}"
        return message
