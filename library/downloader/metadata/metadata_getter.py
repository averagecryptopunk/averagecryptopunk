# ---------------------------------- Imports --------------------------------- #

# System
import os
from typing import List, Optional

# Pip
import requests
from bs4 import BeautifulSoup as bs

import json, os, time

# Local
from ._utils import download_metadata
from .models import PunkMetadata

# ---------------------------------------------------------------------------- #



# ------------------------------ Public methods ------------------------------ #

def get_all_metadata(
    cache_folder_path: str
) -> List[PunkMetadata]:
    os.makedirs(cache_folder_path, exist_ok=True)
    metadatas = []

    for i in range(10000):
        metadata = None
        cache_path = os.path.join(cache_folder_path, '{}.json'.format(str(i).zfill(4)))

        while not metadata:
            metadata = get_metadata(i, cache_path)

        metadatas.append(metadata)

    return metadatas

def get_metadata(
    punk_id: int,
    cache_path: str
) -> Optional[PunkMetadata]:
    if os.path.exists(cache_path):
        with open(cache_path, 'r') as f:
            return PunkMetadata.from_json(json.load(f))

    metadata_dict = download_metadata(punk_id)

    if metadata_dict:
        with open(cache_path, 'w') as f:
            json.dump(metadata_dict, f, indent=4)

        return PunkMetadata.from_json(metadata_dict)

    return None


# ---------------------------------------------------------------------------- #