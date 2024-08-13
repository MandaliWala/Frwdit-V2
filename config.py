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
    SESSION = os.environ.get("SESSION", "BQF-avYAd0_dPxKuLkyIVEBqhFuG3YXNOgTiNaXmPDXPrB_K6sHa3Y2ZMxKEcipBxnwBkXfmLO5uiP2-LNmT5YJ19wLWLtJb8ZCKsFGGWBEKaNwe1BuYme1gIhm0nq9F2mqhjvSsXsWz1nc-YBBamBlbGuiiSVVgp1wLZl69HQDQukJ0_RSpREX4seW4rczvI4V1PG3-jv3i1Zm8J6N6NyjgejyC-Gx_NCH1fiqqhz-1kkWKBzHDhKsFbc90p8BGN9a99ruwYgTbsXeReHtGm9Wi6av5dgsAc40Zw9GzHB4ID6L1DEDefbYJoFymvrUIoJOIAr7HkScLH5TiiCjpuJAtK3C3-AAAAAGIMzILAA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
