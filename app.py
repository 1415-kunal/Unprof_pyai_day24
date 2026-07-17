from fastapi import FastAPI, UploadFile, File, HTTPException
import os
import shutil

app = FastAPI(
    title="PDF RAG API",
    version="1.0.0"
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Welcome to the PDF RAG API"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Validate PDF
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "PDF uploaded successfully",
        "filename": file.filename
    }