from fastapi import FastAPI

app = FastAPI(title="raulf.ai Backend")

@app.get("/")
def read_root():
    return {"status": "online", "domain": "raulf.ai", "message": "AI Lab backend running successfully!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
