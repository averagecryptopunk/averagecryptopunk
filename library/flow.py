# ---------------------------------- Imports --------------------------------- #

# System
from typing import List, Union
import os

# Local
from .download import get_punks
from .renderer import RenderOptions, render

# ---------------------------------------------------------------------------- #



# ------------------------------ Public methods ------------------------------ #

def generate_images(
    cache_folder_path: str,
    options: Union[RenderOptions, List[RenderOptions]]
) -> None:
    render(
        options,
        get_punks(os.path.join(cache_folder_path, 'images')),
        os.path.join(cache_folder_path, 'pixel_maps.json')
    )


# ---------------------------------------------------------------------------- #