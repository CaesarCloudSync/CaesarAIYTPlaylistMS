import uvicorn
from fastapi import FastAPI
from typing import Dict,List,Any,Union
from fastapi.middleware.cors import CORSMiddleware
from CaesarAIYoutube import CaesarAIYoutube
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



JSONObject = Dict[Any, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]


@app.get('/')# GET # allow all origins all methods.
async def index():
    return "Welcome to CaesarAI Template. Hello"


@app.get('/v1/getplaylisturls')# GET # allow all origins all methods.
async def getplaylisturls(url:str):
        try:
            video_urls = CaesarAIYoutube.get_playlist_videos(url)
            return {"video_urls":video_urls} 
  
        except Exception as ex:
            return {"error":f"{type(ex)},{ex}"}



if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,log_level="info")
    #uvicorn.run()
    #asyncio.run(main())