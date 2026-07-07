import os

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

BLOB_URL = os.environ["BLOB_URL"]
BLOB_TOKEN = os.environ["BLOB_READ_WRITE_TOKEN"]


@app.get("/api/v1/data")
async def get_data():
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            BLOB_URL, headers={"Authorization": f"Bearer {BLOB_TOKEN}"}
        )
        return resp.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
