from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
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
    result = '''{
        "topic": ''' + video.filename + ''',
        "writer":"test",
        "subtopics":[
            {
                "title":"title1",
                "content":"content1"
            },
            {
                "title":"title2",
                "content":"content2"
            },
            {
                "title":"title3",
                "content":"content3"
            }
        ],
        "summary":"summary_test"
    }'''
    return JSONResponse(content=result)
