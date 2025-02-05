from fastapi import FastAPI
from app.routes import router
import uvicorn

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "DJ Streaming Backend Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="135.148.32.133", port=8000)
