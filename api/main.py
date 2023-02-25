from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()


@app.post("/upload")
async def uploadVideo(video: UploadFile = File(...)):

    return {"filename": video.filename}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
