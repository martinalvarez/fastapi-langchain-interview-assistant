.
├── app/
│   ├── api/             # 1. Web/API Layer (FastAPI Routers)
│   │   ├── endpoints/   # Contains the routers (e.g., items.py, lang_router.py)
│   │   ├── __init__.py
│   │   └── main.py      # FastAPI entry point (mounts the routers)
│   │
│   ├── core/            # 2. Central Configurations/Utilities
│   │   ├── config.py    # Loads environment variables (Settings)
│   │   ├── exceptions.py
│   │   └── __init__.py
│   │
│   ├── services/        # 3. Service Layer (Business Logic/LangChain)
│   │   ├── lang_service.py # Interaction with LangChain and LLMs
│   │   └── __init__.py
│   │
│   ├── data/            # 4. Data Layer (Models, DB Connections if applicable)
│   │   ├── schemas/     # Pydantic Schemas (Input/Output Models)
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── tests/               # 5. Unit and Integration Tests
│   ├── conftest.py      # Shared fixtures for tests
│   ├── api/             # Tests for API endpoints
│   ├── services/        # Tests for business logic (LangChain)
│   └── __init__.py
│
├── .env                 # Environment variables
├── requirements.txt     # Project dependencies
└── uvicorn_start.sh     # Script to run the application (optional)