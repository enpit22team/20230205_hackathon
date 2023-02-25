from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()


@app.post("/upload")
async def uploadVideo(video: UploadFile = File(...)):
    result = processVideo(video)
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

# mock function
def processVideo(video) -> str:
    result = "Video name is " + video.filename
    return result
