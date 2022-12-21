from typing import Union
from fastapi import FastAPI,HTTPException
from download_video import DownloadVideos
from models.request_api import DownloadVideoRequest
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.responses import FileResponse
from tkinter import *
from tkinter import filedialog
import os



app = FastAPI()
dw = DownloadVideos()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def read_root():
    return {"Hello": "World"}


def iter_file(file_path:str): 
       with open(file_path, mode="rb") as file_like:
         yield from file_like  


@app.post("/downloadVideo/")
def downloadVideo(req:DownloadVideoRequest):
    file = dw.dowloadVideo(urlVideo=req.url)
    mediatype = 'video/mp4'
    if(req.onlyAudio == True):
        mediatype = 'audio/mp3'
        file = dw.convert(file)
    return StreamingResponse(iter_file(file),media_type= mediatype)
    
@app.delete("/deleteFiles/{name_file}")
def delete_file(name_file:str):
    # Implemente a lógica de exclusão do arquivo aqui
    file_path = "files/{}".format(name_file)
    if os.path.exists(file_path):
        os.remove(file_path)
        return {"message": "Arquivo excluído com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")


