from pydantic import BaseModel
import wave

class MyPutRequestType(BaseModel):
    message: str

