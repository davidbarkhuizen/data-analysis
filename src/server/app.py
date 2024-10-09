from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_index():
    return "yo"

@app.on_event("startup")
async def startup_event():
    print("uvicorn/fastapi server started")