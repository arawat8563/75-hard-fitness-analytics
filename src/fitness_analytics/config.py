import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

print("Looking for .env here:")
print(BASE_DIR / ".env")

load_dotenv(BASE_DIR / ".env")

print("POSTGRES_USER:", os.getenv("POSTGRES_USER"))
print("POSTGRES_PORT:", os.getenv("POSTGRES_PORT"))
print("POSTGRES_DB:", os.getenv("POSTGRES_DB"))

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")