# 📄 PDF RAG API with FastAPI & Gemini

A production-ready Retrieval-Augmented Generation (RAG) API built with **FastAPI**, **LangChain**, **FAISS**, **Hugging Face Embeddings**, and **Google Gemini**.

This API allows users to upload PDF documents, automatically create a vector database, and ask questions about the uploaded content using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- Upload PDF documents
- Automatic text extraction
- Smart document chunking
- Sentence Transformer embeddings
- FAISS vector database
- Semantic similarity search
- Google Gemini-powered answer generation
- FastAPI REST API
- Interactive Swagger documentation

---

## 🛠️ Tech Stack

- Python
- FastAPI
- LangChain
- Google Gemini
- Hugging Face Embeddings
- Sentence Transformers
- FAISS
- PyPDF
- Uvicorn

---

## 📁 Project Structure

```
day24-rag-api/
│
├── uploads/
│
├── vector_store/
│   ├── index.faiss
│   └── index.pkl
│
├── app.py
├── config.py
├── create_vector_db.py
├── models.py
├── rag_chain.py
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd day24-rag-api
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the API

```bash
uvicorn app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 📤 API Endpoints

## Home

```
GET /
```

Returns a welcome message.

---

## Upload PDF

```
POST /upload
```

Uploads a PDF and creates a FAISS vector database.

### Response

```json
{
  "message": "PDF uploaded and indexed successfully.",
  "filename": "sample.pdf",
  "chunks_created": 52
}
```

---

## Ask Question

```
POST /ask
```

### Request

```json
{
  "query": "What is machine learning?"
}
```

### Response

```json
{
  "question": "What is machine learning?",
  "answer": "Machine Learning (ML) is a field of Artificial Intelligence..."
}
```

---

## 🔄 Workflow

```
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in FAISS
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Gemini LLM
      │
      ▼
Generate Answer
```

---

## 📦 Dependencies

- FastAPI
- Uvicorn
- LangChain
- LangChain Community
- LangChain HuggingFace
- LangChain Google GenAI
- HuggingFace Sentence Transformers
- FAISS
- PyPDF
- python-dotenv

---

## 📸 Screenshots

Add screenshots of:

- Swagger UI
- Upload Endpoint
- Ask Endpoint
- Successful API Response

---

## 👨‍💻 Author

**Kunal Walunj**

Artificial Intelligence & Data Science Engineering Student

---

## ⭐ Future Improvements

- Multiple PDF support
- Persistent vector database
- Chat history
- Streaming responses
- Docker support
- Authentication
- Cloud deployment