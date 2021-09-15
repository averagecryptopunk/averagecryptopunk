# ---------------------------------- Imports --------------------------------- #

# System
from typing import List, Tuple
import os, json

# Pip
from PIL import Image
import numpy as np

# Local
from ..pixelator import ImageMap

# ---------------------------------------------------------------------------- #



# ------------------------------ Public methods ------------------------------ #

def render_image(
    pixels: ImageMap,
    path: str,
    scale: int = 100
) -> bool:
    org_size = len(pixels)
    target_size = org_size * scale
    array = np.array(pixels, dtype=np.uint8)
    img = Image.fromarray(array)
    img = img.resize((target_size, target_size), Image.AFFINE)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)

    return os.path.exists(path)

def merge_image_maps(
    image_maps: List[ImageMap],
    min_avg_alpha_perc: float = 0,
    color_overflow_by_alpha: bool = False
) -> ImageMap:
    size = len(image_maps[0])
    count = len(image_maps)
    final = [[(0, 0, 0, 0) for _ in range(size)] for _ in range(size)]

    for image_map in image_maps:
        for line, line_pixels in enumerate(image_map):
            for row, (r, g, b, a) in enumerate(line_pixels):
                alpha_multi = a * 255 if color_overflow_by_alpha else 1

                final[line][row] = (
                    final[line][row][0] + r * alpha_multi,
                    final[line][row][1] + g * alpha_multi,
                    final[line][row][2] + b * alpha_multi,
                    final[line][row][3] + a
                )

    return [
        [
            (
                int(r/count),
                int(g/count),
                int(b/count),
                int(a/count) if a/count >= 255*min_avg_alpha_perc else 0
            )
            for (r, g, b, a) in line_pixels
        ] for line_pixels in final
    ]


# ---------------------------------------------------------------------------- #