from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

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
    result = processVideo(video)
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

# mock function
def processVideo(video) -> str:
    result = "Video name is " + video.filename
    return result
