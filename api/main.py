import shutil

from . import push2gpt

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from . import wav2txt
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://soonawatchy.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def uploadVideo(video: UploadFile = File(...)):
    path =f"./data/{video.filename}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(video.file, buffer)
    # result = processVideo(video)
    query = wav2txt.speech2text(path)
    print(query + "\n\n\n")
    result = push2gpt.summary(query)
    print(result)
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

# mock function
def processVideo(video) -> str:
    # result = "Video name is " + video.filename
    result = wav2txt.speech2text(video)
    return result
