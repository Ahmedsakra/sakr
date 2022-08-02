## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("BABkIQRXBYn1RX8ww6JbtvjZLS7iQVHawt9w9MeYZvAAhNTdcEW5Sb7_-STX2T5qul_Klpm3NZePmvHrxkNQ25MkdDlQYXsOOdgRgxp49ToQ216I40h3fdTI0qtBHR_1iQT2g_4HH6CZmbZVnA8jWdOWePQh7wYBOWUexwobUZ5jrnGYb6n_YZOywbas_95ZzbxLe13JhKVk2cwYhzN4w3hUlvUY0KchSkLKli5FytkJcz_iQdpXlrCDuS_JW82VESkhtT9_BiYQzY8ng7hrYi9G9OGJEwE7zdMqeA3eXm-iDbsFWfNJkMRBEBnW_-fmDaAv_WTC8qzgzh5vao3XVbleAAAAATmZuk8A", "")
BOT_TOKEN = getenv("5411867068:AAGYTNx4gYbdf4X5XUf5bVafoeovU0RN5A8", "")
BOT_NAME = getenv("Elsakrmusic_bot of", "song")
API_ID = int(getenv("API_ID", "5261343311"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("", "Elsakr")
OWNER_USERNAME = getenv("Elsakrmusic")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("", "")
OWNER_ID = getenv("OWNER_ID", "1825105037")
ASSISTANT_NAME = getenv("Elsakrvip1", "")
GROUP_SUPPORT = getenv("ELSAKRViP", "")
UPDATES_CHANNEL = getenv("Elsakrvip2", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("Elsakrvip2", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
