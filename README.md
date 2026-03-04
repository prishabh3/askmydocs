# AskMyDocs RAG System

This repository contains the AskMyDocs RAG (Retrieve-and-Generate) system, which consists of a backend, frontend, Docker configurations, and necessary project files.

## Project Structure

```plaintext
askmydocs/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes.py
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── document_service.py
│   │       └── generation_service.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── components/
│   │       ├── DocumentViewer.js
│   │       └── Navbar.js
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Instructions to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/prishabh3/askmydocs.git
   cd askmydocs
   ```

2. **Run with Docker**:
   ```bash
   docker-compose up --build
   ```

3. **Access the application**:
   Open your browser and go to `http://localhost:3000/` for the frontend and `http://localhost:8000/` for the backend.
