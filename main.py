from fastapi import FastAPI

app = FastAPI(title="TATA Power Api Docs")

@app.get("/test")
def read_root():
    return {"message": "Welcome to TATA Power API"}