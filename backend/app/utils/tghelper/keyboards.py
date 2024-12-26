from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update, WebAppInfo
from config import URL_MINIAPP
key_web_app = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(text="شروع",
                                         web_app=WebAppInfo(url=URL_MINIAPP),
                                         ),
                ],
            ])