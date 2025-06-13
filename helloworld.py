from fastapi import fastapi

app= FastAPI()

@app.get("/helloworld")
async def read_root():
    return{"message":"Hello world Congrats"}
