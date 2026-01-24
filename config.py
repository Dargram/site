import os, sys
from dotenv import load_dotenv

load_dotenv()
secret = os.getenv("SECRET_KEY")
if not secret:
    sys.exit("NO SECRET IN .env!")