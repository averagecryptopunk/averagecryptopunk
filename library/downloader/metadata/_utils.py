# ---------------------------------- Imports --------------------------------- #

# System
import os
from typing import cast

# Pip
import requests
from bs4 import BeautifulSoup as bs

import json, os, time

# ---------------------------------------------------------------------------- #



# ------------------------------ Public methods ------------------------------ #

def download_metadata(
    punk_id: int
) -> dict:
    try:
        resp = requests.get('https://www.larvalabs.com/cryptopunks/details/{}'.format(punk_id))

        if resp and resp.status_code == 200 and resp.content:
            soup = bs(resp.content, 'lxml')
            details = soup.find(id='punkDetails')
            punk_type = details.find('h4').find('a').text
            accessories = [a.text for a in details.find(class_='detail-row').find_all('a')]

            return {
                'id': punk_id,
                'type': punk_type,
                'accs': accessories
            }
    except:
        return None


# ---------------------------------------------------------------------------- #