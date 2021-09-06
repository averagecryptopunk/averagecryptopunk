# ---------------------------------- Imports --------------------------------- #

# System
from typing import List, Union
import os

# Local
from ._utils import merge_image_maps, get_image_maps, render_image
from .render_options import RenderOptions

# ---------------------------------------------------------------------------- #



# ---------------------------------- Methods --------------------------------- #

def render(
    options: Union[RenderOptions, List[RenderOptions]],
    img_paths: List[str],
    pixel_maps_cache_folder_path: str
) -> None:
    if not isinstance(options, list):
        options = [options]
    
    image_maps = get_image_maps(
        img_paths,
        pixel_maps_cache_folder_path
    )

    for _options in options:
        img_map = merge_image_maps(
            image_maps,
            _options.min_avg_alpha_perc,
            _options.color_overflow_by_alpha
        )

        render_image(
            img_map,
            _options.path,
            _options.scale
        )


# ---------------------------------------------------------------------------- #