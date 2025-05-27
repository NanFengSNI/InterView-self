
#  uvicorn main:app --reload --host 0.0.0.0 --port 8000
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from uuid import uuid4
import random
import shutil
import json
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
META_FILE = UPLOAD_DIR / "metadata.json"

def load_metadata():
    if META_FILE.exists():
        with open(META_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_metadata(metadata):
    with open(META_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

DOC_TYPES = ["简历", "求职信", "其他"]

@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    ext = Path(file.filename).suffix
    uid = str(uuid4())
    filename = f"{uid}{ext}"
    file_path = UPLOAD_DIR / filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 保存元数据
    metadata = load_metadata()
    metadata[filename] = {
        "original_name": file.filename,
        "type": random.choice(DOC_TYPES),
        "upload_date": datetime.date.today().isoformat()
    }
    save_metadata(metadata)

    return {
        "message": "上传成功",
        "id": uid,
        "filename": file.filename,
        "url": f"/api/file/{filename}"
    }

@app.get("/api/files")
def list_files():
    metadata = load_metadata()
    files = []
    for f in UPLOAD_DIR.iterdir():
        if f.is_file() and f.name != "metadata.json":
            meta = metadata.get(f.name, {})
            files.append({
                "name": meta.get("original_name", f.name),  # ← 使用原始文件名
                "type": meta.get("type", "其他"),
                "uploadDate": meta.get("upload_date", datetime.date.today().isoformat()),
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
        metadata = load_metadata()
        if filename in metadata:
            del metadata[filename]
            save_metadata(metadata)
        return {"message": f"{filename} 已删除"}
    return JSONResponse(status_code=404, content={"message": "文件不存在"})

USER_FILE = Path("users.json")