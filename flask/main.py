
#  uvicorn main:app --reload --host 0.0.0.0 --port 8000
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from uuid import uuid4
import random
import shutil
import datetime
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue 的开发服务器地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

DOC_TYPES = ["简历", "求职信", "其他"]

@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    # 使用 UUID 防止重复文件名
    ext = Path(file.filename).suffix
    uid = str(uuid4())
    filename = f"{uid}{ext}"
    file_path = UPLOAD_DIR / filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "上传成功",
        "id": uid,
        "filename": file.filename,
        "url": f"/api/file/{filename}"
    }

@app.get("/api/files")
def list_files():
    files = []
    for f in UPLOAD_DIR.iterdir():
        if f.is_file():
            files.append({
                "name": f.name,
                "type": random.choice(DOC_TYPES),
                "uploadDate": datetime.date.today().isoformat(),
                "fileUrl": f"/api/file/{f.name}",
            })
    return files

@app.get("/api/file/{filename}")
def get_file(filename: str):
    file_path = UPLOAD_DIR / filename
    if file_path.exists():
        return FileResponse(path=file_path, filename=filename, media_type='application/pdf')
    return JSONResponse(status_code=404, content={"message": "文件不存在"})


@app.delete("/api/delete/{filename}")
def delete_file(filename: str):
    file_path = UPLOAD_DIR / filename
    if file_path.exists():
        file_path.unlink()
        return {"message": f"{filename} 已删除"}
    return JSONResponse(status_code=404, content={"message": "文件不存在"})
