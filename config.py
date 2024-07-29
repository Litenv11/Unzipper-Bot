# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("20315396"))
    API_HASH = os.environ.get("52edde742449c75895948e0a25abe7db")
    BOT_TOKEN = os.environ.get("7429678025:AAF1Mh8xgrfOe5YMf4D__igQHsVzMph3__M")
    LOGS_CHANNEL = int(os.environ.get("-1002122659804"))
    BOT_OWNER = int(os.environ.get("5196029054"))
    MONGODB_URL = os.environ.get("mongodb+srv://Liten:OoIj9FZ6J5ca7K31@cluster0.hcxotkc.mongodb.net/?retryWrites=true&w=majority")
    GOFILE_TOKEN = os.environ.get("pSFMwETrfniRc0drvX7AaUxjpWBzeOMO")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
