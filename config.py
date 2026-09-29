import os
from pathlib import Path

from dotenv import load_dotenv


# =========================
# .ENV NI YUKLASH
# =========================

load_dotenv()


# =========================
# BOT SOZLAMALARI
# =========================

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

OWNER_ID = int(os.getenv("OWNER_ID", "0"))

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "data/mafia.db"
)

WEB_BASE_URL = os.getenv(
    "WEB_BASE_URL",
    ""
).strip()


# =========================
# DATABASE PAPKASI
# =========================

db_path = Path(DATABASE_PATH)

if db_path.parent != Path("."):
    db_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )


# =========================
# TEKSHIRUV
# =========================

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN topilmadi!\n"
        ".env faylga BOT_TOKEN=... yozing."
    )
