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
        if signal in ["YouTube", "Netflix"]:
            await tv.launch(signal)
        else:
            await tv.send_signal(signal)
            # message = f"Received {signal}"
            # return message
