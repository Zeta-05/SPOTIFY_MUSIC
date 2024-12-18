import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = os.getenv("API_ID", "23568641")
API_HASH = os.getenv("API_HASH", "a39098e8752a45c2d6d1889941547bbc")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7339158179:AAFZRGNI--7xVXUmwQLkIX_fj7yLhp_8wbs")
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "X_STARBOY_KT")
BOT_USERNAME = os.getenv("BOT_USERNAME", "UtopiaMaxBot")
BOT_NAME = os.getenv("BOT_NAME", "Utopia")
ASSUSERNAME = os.getenv("ASSUSERNAME")

API_KEY = "abc921ff654bcf7b3faff8f775d781d27d32bfd02d6692eea30249ba781c8b"  # अपना API key यहाँ डालें
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://GOKU:MISSBHOPALI@goku.pzzsl8d.mongodb.net/?retryWrites=true&w=majority")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = os.getenv("LOGGER_ID", "@ZTX_HEADQUATERS")
OWNER_ID = get_env_int("OWNER_ID", "7318101682")
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# config.py
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/BABY-MUSIC/SPOTIFY_MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/Kayto_Official")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/ZTX_HEADQUATERS")
SOURCE = getenv("SOURCE", "https://t.me/Kayto_Official")
CHAT = getenv("CHAT", "https://t.me/Kayto_Official")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQFfYv8Afrs-bAndXp9OCWJw6G-fimbq9M9pGnpo8Uw9kzZpsE1aAlIZxSJMpggKzwBuxkNJQAMa6Z2dmJfq-15QaxZ0MmmsMpIC2dyaSzbvTL9h2s_UDpcGeZ-FeT_mGPZa-SyB3WY3Au6lKa_97OP8LyinZvgFFnTBsKXOpzw5A-1TY8BTpTvo9HSJROmYJLPqmRG7rWeA8Cg2BLIqQRbAerKzAwn0dzXjh9rWfDvv2ugXIGrokfntxlJ1n6VzG-sumoAWZfrdiADNUyz8wsV-2oIY2JRRsMPvF20PSCRpdPUMDywzxpBhgg9bJN5ZALpoPOSGd8lLi4lKu2AEdh_EV1BsHQAAAAGjgnJNAA")
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = os.getenv(
    "START_IMG_URL", "https://graph.org/file/364a09ddd47378efaecfb-2d3ae182ccf44e9087.jpg"
)
PING_IMG_URL = os.getenv(
    "PING_IMG_URL", "https://graph.org/file/35ef624f376e22a0fa1d7-1ea63e464ea9f36fab.jpg"
)
PLAYLIST_IMG_URL = os.getenv(
    "PLAYLIST_IMG_URL", "https://envs.sh/K-2.jpg"
) 
TELEGRAM_AUDIO_URL = os.getenv(
    "TELEGRAM_AUDIO_URL", "https://envs.sh/K-2.jpg"
) 
TELEGRAM_VIDEO_URL = os.getenv(
    "TELEGRAM_VIDEO_URL", "https://envs.sh/K-2.jpg"
) 
STREAM_IMG_URL = os.getenv(
    "STREAM_IMG_URL", "https://envs.sh/K-2.jpg"
) 
SOUNCLOUD_IMG_URL = os.getenv(
    "SOUNCLOUD_IMG_URL", "https://envs.sh/K-2.jpg"
) 
YOUTUBE_IMG_URL = os.getenv(
    "YOUTUBE_IMG_URL", "https://envs.sh/K-2.jpg"
) 
SPOTIFY_ARTIST_IMG_URL = os.getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://envs.sh/K-2.jpg",
) 
SPOTIFY_ALBUM_IMG_URL = os.getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://envs.sh/K-2.jpg"
) 
SPOTIFY_PLAYLIST_IMG_URL = os.getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://envs.sh/K-2.jpg"
) 

# YouTube thumbnail URL format
YOUTUBE_IMG_URL = "https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
