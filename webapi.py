from fastapi import FastAPI, HTTPException, UploadFile, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
import msgBank 
from pydantic import BaseModel
from myRequestType import MyPutRequestType as putType
from vosk_simple import MyVosk


app = FastAPI()
msgBank = msgBank.MsgBank()

@app.get("/get_message")
async def root():
    return {"message": msgBank.get()}

@app.put("/push_message")
async def puss_message(body: putType):
    msgBank.add(body.message)
    return {"result": "succese"}

@app.post("/convert_text")
async def conver_text(file: UploadFile):
    result = MyVosk.TextConvert(file.file)
    print(file.filename)
    # return {"message": "ok"}
    return {"message": str(result)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
