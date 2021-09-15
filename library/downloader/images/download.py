# ---------------------------------- Imports --------------------------------- #

# System
from typing import Dict
import os, time

# Local
from ._utils import download

# ---------------------------------------------------------------------------- #



# ---------------------------------- Methods --------------------------------- #

def get_punks(
    folder_path: str
) -> Dict[int, str]:
    os.makedirs(folder_path, exist_ok=True)

    TOTAL_PUNKS = 10000
    PUNK_URL_FORMAT  = 'https://www.larvalabs.com/public/images/cryptopunks/punk{}.png'
    PUNK_PATH_FORMAT = os.path.join(folder_path, '{}.png')
    img_paths = {}

    for i in range(TOTAL_PUNKS):
        punk_path = PUNK_PATH_FORMAT.format(str(i).zfill(4))

        if os.path.exists(punk_path):
            img_paths[i] = punk_path

            continue

        downloaded = False

        while not downloaded:
            downloaded = download(PUNK_URL_FORMAT.format(i), punk_path)

            if not downloaded:
                time.sleep(5)

        img_paths[i] = punk_path

    return img_paths


# ---------------------------------------------------------------------------- #