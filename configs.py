# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "14356452"))
    API_HASH = getenv("API_HASH", "cac21249a0c6373a1b742afb8dbc9cb7")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "PS_BOTz")
    CHID = int(getenv("CHID", "-1001910352559"))
    SUDO = list(map(int, getenv("SUDO", "950958796 5003133371").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
