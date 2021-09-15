# ---------------------------------- Imports --------------------------------- #

# System
import os

# Pip
import requests

# ---------------------------------------------------------------------------- #



# ------------------------------ Public methods ------------------------------ #

def download(
    url:  str,
    path: str
) -> bool:
    try:
        resp = requests.get(url, stream=True)

        if resp and resp.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in resp.iter_content(1024):
                    f.write(chunk)

                return True
    except:
        pass

    return False


# ---------------------------------------------------------------------------- #