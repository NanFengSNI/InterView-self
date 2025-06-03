
#  uvicorn main:app --reload --host 0.0.0.0 --port 8000
from fastapi import FastAPI, UploadFile, File, Request, Query, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from typing import List
from pydantic import BaseModel
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

@app.get("/api/user-profile")
def get_user_profile():
    data_file = Path("user_data.json")
    if not data_file.exists():
        return {"error": "user data not found"}
    with open(data_file, "r", encoding="utf-8") as f:
        user_data = json.load(f)
    return user_data

@app.get("/api/job-recommendations")
def get_job_recommendations():
    data_file = Path("job_recommend.json")
    if not data_file.exists():
        return {"error": "job data not found"}
    with open(data_file, "r", encoding="utf-8") as f:
        job_data = json.load(f)
    return job_data

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

@app.get("/question-data/")
async def get_question_data(
    domain: str = Query(..., description="领域名称，例如：AI"),
    position: str = Query(..., description="岗位名称，例如：AIAlgorithmEngineer")
):
    # 构建文件路径
    file_path = os.path.join("QuestionData", domain, f"{position}.json")
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="找不到对应的问题数据文件")
    
    # 读取并返回文件内容
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"读取文件时发生错误: {str(e)}")