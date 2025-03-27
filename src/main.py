from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "platform!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
