# ---------------------------------- Imports --------------------------------- #

# System
from library.pixelator.image_map import ImageMap
from typing import List, Union

# Local
from ._utils import merge_image_maps, render_image
from .render_options import RenderOptions

# ---------------------------------------------------------------------------- #



# ---------------------------------- Methods --------------------------------- #

def render(
    options: Union[RenderOptions, List[RenderOptions]],
    image_maps: List[ImageMap]
) -> None:
    if not isinstance(options, list):
        options = [options]

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