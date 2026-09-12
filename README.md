# DSC5003 Group Project

## Tech Stack
- Backend: FastAPI (Python 3.12)
- Database: TBD

## Getting Started

### 1. Clone the repository
```bash
git clone <repo-url>
cd <repo-name>
```

### 2. Create a virtual environment
```bash
python -m venv .venv
```

### 3. Activate the virtual environment
- Windows (PowerShell):
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- macOS / Linux:
  ```bash
  source .venv/bin/activate
  ```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the server
```bash
uvicorn main:app --reload
```

### 6. Open in your browser
http://127.0.0.1:8000

## Project Structure
```
.
├── main.py              # FastAPI entry point
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md
```

## Notes
- The virtual environment (`.venv/`) is not tracked by Git.
  Each member should create their own after cloning.