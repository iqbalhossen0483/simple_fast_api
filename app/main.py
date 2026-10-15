from fastapi import FastAPI

app = FastAPI(title="FastAPI Server")


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Server"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
