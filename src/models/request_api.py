from typing import Optional
from pydantic import BaseModel


class DownloadVideoRequest(BaseModel):
    url:str
    onlyAudio:  Optional[bool] = False