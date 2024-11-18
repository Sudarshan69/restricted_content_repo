# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28240021"))
API_HASH = getenv("API_HASH", "5cbd934836be2c35fd9bbb2606e4e98e")
BOT_TOKEN = getenv("BOT_TOKEN", "7816281704:AAHd7id_V7ACtAIIdHnYyDA7X_UxjtBAh6Y")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7798957366").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://savebot:RxxBfvkv1xnGsbPL@cluster0.9zpw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002346487469"))
