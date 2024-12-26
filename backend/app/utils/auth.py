from telegram_webapps_authentication import Authenticator

from config import BOT_TOKEN
authenticator = Authenticator(BOT_TOKEN)

def validate_tma_header(tma_header: str) -> bool:
    if not tma_header.startswith("tma "):
        return False
    initdata = tma_header[4:].strip()
    if initdata == "":
        return False
    tma_header = tma_header.split(" ")[1]
    print("tma header:",tma_header)
    authenticator.get_telegram_user(tma_header)
    return True
