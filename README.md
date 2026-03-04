# AskMyDocs

This project implements a Retrieval-Augmented Generation (RAG) system using FastAPI.

## Directory Structure

The project is structured as follows:

```
askmydocs/
├── backend/
│   ├── config.py
│   └── main.py
├── frontend/
├── docker/
├── data/
├── scripts/
└── tests/
```

## Installation

### Requirements

Make sure to have Python 3.8+ installed. You can install the dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

To run the FastAPI application, execute:

```bash
uvicorn backend.main:app --reload
```

## Tests

To run the tests, use:

```bash
pytest tests/
```
