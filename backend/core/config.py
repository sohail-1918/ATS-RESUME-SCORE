import os
from pathlib import Path
from dotenv import load_dotenv

# --- Load .env ---
# This version checks both project root and backend folder
root_env = Path(__file__).resolve().parents[2] / ".env"
backend_env = Path(__file__).resolve().parents[1] / ".env"

if root_env.exists():
    load_dotenv(dotenv_path=root_env, override=True)
    print("Loaded .env from project root:", root_env)
elif backend_env.exists():
    load_dotenv(dotenv_path=backend_env, override=True)
    print("Loaded .env from backend folder:", backend_env)
else:
    print("No .env file found")

# --- API metadata ---
APP_TITLE = "ATS RESUME ANALYZER API"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Analyse resumes against job description using NLP + ML"

ALLOWED_ORIGINS = [
    "https://ats-resume-score-sohail1918.streamlit.app/"
]

# --- File settings ---
MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

SUPPORTED_MIME_TYPES = {
    "application/pdf": "pdf",
    "application/msword": "doc",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
}
SUPPORTED_EXTENSIONS = {".pdf", ".doc", ".docx"}

# --- NLP models ---
SPACY_MODEL_PRIMARY = "en_core_web_md"  # better accuracy
SPACY_MODEL_SECONDARY = "en_core_web_sm"
SENTENCE_TRANSFORMER_MODEL = os.getenv("SENTENCE_TRANSFORMER_MODEL", "all-MiniLM-L6-v2")

# --- Scoring weights ---
SCORE_WEIGHTS = {
    "formatting": 20,
    "keywords": 25,
    "content": 25,
    "skill_validation": 15,
    "ats_compatibility": 15,
}
JD_KEYWORD_WEIGHT = 0.6
JD_SEMANTIC_WEIGHT = 0.4

# --- Environment variables ---
SUPABASE_URL        = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY        = os.getenv("SUPABASE_KEY", "")          # service_role — DB writes
SUPABASE_ANON_KEY   = os.getenv("SUPABASE_ANON_KEY", "")     # public anon — frontend auth
SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET", "")   # backend token verification
GROQ_API_KEY        = os.getenv("GROQ_API_KEY", "")

