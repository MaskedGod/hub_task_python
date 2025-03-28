from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from src.api import router


app = FastAPI()

app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "platform!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
