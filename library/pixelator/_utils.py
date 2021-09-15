# ---------------------------------- Imports --------------------------------- #

# System
import os, json

# Pip
from PIL import Image

# Local
from . import ImageMap

# ---------------------------------------------------------------------------- #



# ------------------------------ Public methods ------------------------------ #

def get_image_map(
    img_path: str,
    cache_path: str
) -> ImageMap:
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'r') as f:
                return json.load(f)
        except:
            pass

    im = Image.open(img_path, 'r')
    pix_val = list(im.getdata())
    size = im.size[0]
    pixels = []

    for i in range(size):
        line = []

        for j in range(size):
            line.append(pix_val[i*size + j])

        pixels.append(line)

    with open(cache_path, 'w') as f:
        json.dump(pixels, f, indent=4)

    return pixels


# ---------------------------------------------------------------------------- #