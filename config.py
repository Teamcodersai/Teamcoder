# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "22875242"))
API_HASH = getenv("API_HASH", "32eddce639c6fd7fe6a40db879dcb91c")
BOT_TOKEN = getenv("BOT_TOKEN", "6153257153:AAGGEFkNGwtHEMKLvj8Dx8EVbRkfPQ7YfPw")
OWNER_USERNAME = getenv("OWNER_USERNAME", "TeamcoderTg")
BOT_USERNAME = getenv("BOT_USERNAME", "Team_Coder_Music_Bot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "TeamcoderTg")
BOT_NAME = getenv("BOT_NAME","🆃ҽαɱ 🅲σԃҽɾ 🅼υʂιƈ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))
SESSION_NAME = getenv("SESSION_NAME", "BQBztOc4zVywDsMvu_z1xmfU82NWfAvorlGuJOcKwahycTvuiS1r5TO8s9D7z8epzWaXrd1n8zKV4hKG6I3lp1KCY08gvXSp3Wc53WZjV81is01EuRZ_9sVQ5DgnNxRwGBhI_EriBH9pbttNEaYiWGKuBMYf8ufygtSSq45GYF5evo8V67DyQ0N38z3yohIxZl9CYU8pUH32lARl3iBlfM_kwVsa1l50pyy_-UHGU3SXnKB_pRalVeN8C0XI1952VKnxNaInoY7J5mEjrKytcoKgfGV1nAQBiDyc6BXHOvNxfWqkIcCJhCWbJhb9Kquu_OBE0goW9RKKyaHMAarWr0-qAAAAAWlv1vQA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "DISABLE")
BOT_IMG = getenv("BOT_IMG", "https://telegra.ph/file/2c3097ae03f950800a66f.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6063904500").split()))
