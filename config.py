from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("24089031"))
API_HASH = getenv("0615e3afe13ddaaf8e9ddbd3977d35ff")

BOT_TOKEN = getenv("7028288342:AAGO5QHFzY4jG0aRpnq3SF9r4IOpBe76qr0")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 6584789596))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Flex_Support_Chat")
