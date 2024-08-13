#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 25163484)
    API_HASH = os.environ.get("API_HASH", "145bcbc424d1c1ffe04f3e607ea55c9a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7016509767:AAHGyELmvA9D6uCz2yPsI5sL4gr7pooU1lI") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", 6302921275)
    SESSION = os.environ.get("SESSION")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
