import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from  https://api.imgbb.com/
API_KEY = getenv("API_KEY", "3c10eb772fc9e5a9ee66fe03293c3247") 

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "24669465"))
API_HASH = getenv("API_HASH", "ef15199702ea76ebb2ebe4eca477ab60")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7997882781:AAEwzFafUd6jpelIjxIHl60Z4T5aRuW9Rmk")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://cenap526:cenappp526@cluster0.7onsb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002662249469"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6623140842"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/venombolteop/VenomMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+WWX0t-5B509iMWE0")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Turkiyelinki")


AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "false")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "BAF4bRkAmZqo6k7_HacnAbxm2-wU1_sHt3eSYofTxeo9tHOWq1u55UYhDNwv-0FUp9LJdjFbK0ch7rUVupCa-vbUNIUXfUZLZy6h3y5xJzHrEWe_tF4rxYLo2PXI6MoECbw14_J49pt0djDq3hzqRP4rsFwWBFOK421w0-O9_0Evbs-Gg0Tj6HAC3k-lGFp3d8w8DGmMLmh-vyZZVv2bZSj1EQLPjKD0Pv8PCMKLYMT_-b81IBWNbLzJWuF9Q2JPhgGeuqkRgA6O-AbNVT_oGQBsAe8UxhAVlRz-Rs61inueDuOWmILQddH0snFFGTx53BHT5wiuwaHr38sWCg_uXdo7ER9fhwAAAAG_f8l8AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
