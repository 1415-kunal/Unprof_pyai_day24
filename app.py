from fastapi import FastAPI, UploadFile, File, HTTPException
import os
import shutil
from models import QueryRequest
from rag_chain import get_answer

from create_vector_db import create_vector_db

app = FastAPI(
    title="PDF RAG API",
    description="Upload PDFs and create a FAISS vector database",
    version="1.0.0"
)

# Folder to store uploaded PDFs
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Welcome to the PDF RAG API 🚀",
        "status": "Running"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF, process it, and create a FAISS vector database.
    """

    # Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Save uploaded PDF
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Create vector database
        chunk_count = create_vector_db(file_path)

        return {
            "message": "PDF uploaded and indexed successfully.",
            "filename": file.filename,
            "chunks_created": chunk_count
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing PDF: {str(e)}"
        )
    

@app.post("/ask")
def ask_question(request: QueryRequest):

    answer = get_answer(request.query)

    return {
        "question": request.query,
        "answer": answer
    }

print("\nRegistered Routes:")
for route in app.routes:
    print(route.methods, route.path)