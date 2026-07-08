# ==========================================
# Creator: MrZyro
# Telegram: @MrZyro_dev
# GitHub: https://github.com/MrZyro
# ==========================================

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
api_id = os.getenv("API_ID", "21418386")
api_hash = os.getenv("API_HASH", "aeac46b1d123e82fe6dcb43b6a26cfae")

# Bot Token
TOKEN = os.getenv("TOKEN", "")

# Logging & Logs Channel
BOT_LOGGING = os.getenv("BOT_LOGGING", "-1004445101312")
DATABASE_ID = os.getenv("DATABASE_ID", "-1003757977776")
FORCE_JOIN = os.getenv("FORCE_JOIN", "-1001484473904")

# Database configuration
mongo_url = os.getenv("MONGO_URL", "")
backup_mongo_url = os.getenv("BACKUP_MONGO_URL", "")
DB_NAME = os.getenv("DB_NAME", "SHANUWAIFUBOT")

# Channels & Chats
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "-1001484473904")
UPDATE_CHAT = os.getenv("UPDATE_CHAT", "-1004364670717")
MUSJ_JOIN = os.getenv("MUSJ_JOIN", "-1001484473904")

# Admin user configurations
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# ImgBB API Key
IMGBB_API_KEY = os.getenv("IMGBB_API_KEY", "")

# Media Configurations
START_MEDIA = [
    os.getenv("START_MEDIA_1", "https://files.catbox.moe/zufhkk.mp4"),
    os.getenv("START_MEDIA_2", "https://files.catbox.moe/zufhkk.mp4")
]

PHOTO_URL = [
    os.getenv("PHOTO_URL_1", "https://files.catbox.moe/7ccoub.jpg"),
    os.getenv("PHOTO_URL_2", "https://files.catbox.moe/7ccoub.jpg")
]

STATS_IMG = [
    os.getenv("STATS_IMG", "https://files.catbox.moe/gknnju.jpg")
]

