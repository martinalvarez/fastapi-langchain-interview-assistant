# FastAPI + LangChain: Interview Assistant

**Description:** FastAPI + LangChain: Generate interview questions and evaluate candidate responses using LLMs.

This project serves as a practical demonstration of integrating a high-performance Python API framework (FastAPI) with a sophisticated LLM orchestration library (LangChain) following a clear, scalable architectural pattern.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.10+
* Virtual environment (recommended)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/fastapi-langchain-interview-assistant.git](https://github.com/your-username/fastapi-langchain-interview-assistant.git)
    cd fastapi-langchain-interview-assistant
    ```

2.  **Create and activate the virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate   # Windows CMD
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    Create a file named **`.env`** in the project root and add your LLM API key.

    ```text
    # .env
    OPENAI_API_KEY="sk-************************************"
    ```

### Running the Application

Start the FastAPI server using Uvicorn with auto-reload:

```bash
uvicorn app.api.main:app --reload