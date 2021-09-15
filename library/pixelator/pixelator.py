# ---------------------------------- Imports --------------------------------- #

# System
from typing import List
import os

# Local
from .image_map import ImageMap
from ._utils import get_image_map

# ---------------------------------------------------------------------------- #



# ------------------------------ Public methods ------------------------------ #

def get_image_maps(
    img_paths: List[str],
    cache_folder_path: str
) -> List[ImageMap]:
    os.makedirs(cache_folder_path, exist_ok=True)
    maps = []

    for img_path in img_paths:
        i_str = img_path.split(os.sep)[-1].split('.')[0]
        cache_path = os.path.join(cache_folder_path, '{}.json'.format(i_str))

        maps.append(get_image_map(img_path, cache_path))

    return maps


# ---------------------------------------------------------------------------- #