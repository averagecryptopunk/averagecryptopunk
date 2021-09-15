# ---------------------------------- Imports --------------------------------- #

# System
from library.downloader.metadata.models.enums import punk_type
from typing import List, Union
import os, copy

# Local
from .downloader import get_all_metadata, get_punks
from .pixelator import get_image_maps
from .renderer import render
from .image_options import ImageOptions

# ---------------------------------------------------------------------------- #



# ------------------------------ Public methods ------------------------------ #

def generate_images(
    cache_folder_path: str,
    options: Union[ImageOptions, List[ImageOptions]]
) -> None:
    punk_image_paths = get_punks(
        os.path.join(cache_folder_path, 'images')
    )
    punk_metadatas = get_all_metadata(
        os.path.join(cache_folder_path, 'metadatas')
    )
    
    if not isinstance(options, list):
        options = [options]

    image_maps_cache_folder_path = os.path.join(cache_folder_path, 'image_maps')

    for _options in options:
        if _options.punk_type:
            _punk_metadatas   = [pm for pm in punk_metadatas if pm.type == _options.punk_type]
            punk_metadata_ids = [pm.id for pm in _punk_metadatas]
            _punk_image_paths = {punk_id:pip for punk_id, pip in punk_image_paths.items() if punk_id in punk_metadata_ids}
        else:
            _punk_image_paths = copy.deepcopy(punk_image_paths)

        render(
            options=_options,
            image_maps=get_image_maps(
                _punk_image_paths.values(),
                image_maps_cache_folder_path
            )
        )


# ---------------------------------------------------------------------------- #