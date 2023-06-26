from fastapi import FastAPI
import yaml

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

TOKEN = config['apitable']['token']

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Apitable! Tis my TOKEN " + TOKEN}
