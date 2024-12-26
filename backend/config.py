from os import environ
from dotenv import load_dotenv
load_dotenv()

proj_name = str(environ.get("proj_name"))
API_ID = int(environ.get("API_ID"))
API_HASH = str(environ.get("API_HASH"))
BOT_TOKEN = str(environ.get("BOT_TOKEN"))
LOG_TOKEN = str(environ.get("LOG_TOKEN",BOT_TOKEN))
WORKERS = int(environ.get("WORKERS"))
report_channel = str(environ.get("report_channel"))
MYSQL_PASS = str(environ.get("MYSQL_PASS"))
MYSQL_USER = str(environ.get("MYSQL_USER"))
MYSQL_DB = str(environ.get("MYSQL_DB"))
DOMAIN = str(environ.get("DOMAIN"))
DEBUG = True if str(environ.get("DEBUG")) == 'true' else False
config = {
    'user': MYSQL_USER,
    'password': MYSQL_PASS,
    'host': 'localhost',
    'database': MYSQL_DB,
    }
logid = 223356203
admins = str(environ.get("admins")).split(',')
admins = list(map(lambda x:int(x),admins))


