# ---------------------------------- Imports --------------------------------- #

# System
import os

# Local
from library import ImageOptions, PunkType, generate_images

# ---------------------------------------------------------------------------- #



# ----------------------------------- Vars ----------------------------------- #

scale = 1#00 # 24x24 * scale(100) ==> 2400x2400

cwd = os.path.dirname(__file__)
dist_folder_path = os.path.join(cwd, 'results', 'min')
os.makedirs(dist_folder_path, exist_ok=True)
options = []

# ----------------------------------- Flow ----------------------------------- #

for punk_type in [None, PunkType.Female, PunkType.Male, PunkType.Zombie, PunkType.Ape, PunkType.Alien]:
    pt = punk_type.value.lower() if punk_type else 'all'

    # All pixels averaged
    true_average = ImageOptions(
        path=os.path.join(dist_folder_path, '{}-c0-a00.png'.format(pt)),
        min_avg_alpha_perc=0,
        color_overflow_by_alpha=False,
        scale=scale,
        punk_type=punk_type
    )

    # All pixels averaged - everything ignored that doesn't have 255*0.6 alpha
    some_transparent_ignored = ImageOptions(
        path=os.path.join(dist_folder_path, '{}-c0-a06.png'.format(pt)),
        min_avg_alpha_perc=0.6,
        color_overflow_by_alpha=False,
        scale=scale,
        punk_type=punk_type
    )

    # All pixels averaged - everything ignored that doesn't have 255 alpha
    all_transparent_ignored = ImageOptions(
        path=os.path.join(dist_folder_path, '{}-c0-a10.png'.format(pt)),
        min_avg_alpha_perc=1,
        color_overflow_by_alpha=False,
        scale=scale,
        punk_type=punk_type
    )

    # All pixels averaged - everything ignored that doesn't have 255 alpha.
    # Every pixels r,g,b are multiplied by it's alpha and 255 before averaging
    all_transparent_ignored_color_overflow = ImageOptions(
        path=os.path.join(dist_folder_path, '{}-c1-a10.png'.format(pt)),
        min_avg_alpha_perc=1,
        color_overflow_by_alpha=True,
        scale=scale,
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