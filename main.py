# ---------------------------------- Imports --------------------------------- #

# System
import os

from PIL.Image import NONE

# Local
from library import ImageOptions, PunkType, generate_images

# ---------------------------------------------------------------------------- #



# ----------------------------------- Vars ----------------------------------- #

BG_COLOR_ALL    = ( 75, 145, 198)
BG_COLOR_APE    = (211, 199,  98)
BG_COLOR_ZOMBIE = (139,  69,  61)
BG_COLOR_ALIEN  = (128, 100, 167)
BG_COLOR_MALE   = ( 98, 110, 225)
BG_COLOR_FEMALE = (255, 112, 150)


# ------------------------------- CHANGE THESE ------------------------------- #


BG_COLOR = BG_COLOR_MALE # or None
SIZE = 2**12 # 12 images so 2^12 => 4096


# ---------------------------------------------------------------------------- #

cwd = os.path.dirname(__file__)

_bg_color = 'transparent' if BG_COLOR is None else f'{BG_COLOR[0]}_{BG_COLOR[1]}_{BG_COLOR[2]}'
dist_folder_path = os.path.join(cwd, f'results{os.sep}{SIZE}-bg-{_bg_color}')
os.makedirs(dist_folder_path, exist_ok=True)
options = []


# ----------------------------------- Flow ----------------------------------- #

for punk_type in [PunkType.Male]:#None, PunkType.Female, PunkType.Male, PunkType.Zombie, PunkType.Ape, PunkType.Alien]:
    pt = punk_type.value.lower() if punk_type else 'all'

    # All pixels averaged
    true_average = ImageOptions(
        path=os.path.join(dist_folder_path, '{}-c0-a00.png'.format(pt)),
        min_avg_alpha_perc=0,
        color_overflow_by_alpha=False,
        size=SIZE,
        bg_color=BG_COLOR,
        punk_type=punk_type
    )

    # All pixels averaged - everything ignored that doesn't have 255*0.6 alpha
    some_transparent_ignored = ImageOptions(
        path=os.path.join(dist_folder_path, '{}-c0-a06.png'.format(pt)),
        min_avg_alpha_perc=0.6,
        color_overflow_by_alpha=False,
        size=SIZE,
        bg_color=BG_COLOR,
        punk_type=punk_type
    )

    # All pixels averaged - everything ignored that doesn't have 255 alpha
    all_transparent_ignored = ImageOptions(
        path=os.path.join(dist_folder_path, '{}-c0-a10.png'.format(pt)),
        min_avg_alpha_perc=1,
        color_overflow_by_alpha=False,
        size=SIZE,
        bg_color=BG_COLOR,
        punk_type=punk_type
    )

    # All pixels averaged - everything ignored that doesn't have 255 alpha.
    # Every pixels r,g,b are multiplied by it's alpha and 255 before averaging
    all_transparent_ignored_color_overflow = ImageOptions(
        path=os.path.join(dist_folder_path, '{}-c1-a10.png'.format(pt)),
        min_avg_alpha_perc=1,
        color_overflow_by_alpha=True,
        size=SIZE,
        bg_color=BG_COLOR,
        punk_type=punk_type
    )

    options.extend([
        true_average,
        some_transparent_ignored,
        all_transparent_ignored,
        all_transparent_ignored_color_overflow
    ])


generate_images(
    cache_folder_path=os.path.join(cwd, 'cache'),
    options=options
)


# ---------------------------------------------------------------------------- #