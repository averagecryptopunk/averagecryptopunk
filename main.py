# ---------------------------------- Imports --------------------------------- #

# System
import os

# Local
from library import RenderOptions, generate_images

# ---------------------------------------------------------------------------- #



# ----------------------------------- Vars ----------------------------------- #

scale = 100 # 24x24 * scale(100) ==> 2400x2400

cwd = os.path.dirname(__file__)
dist_folder_path = os.path.join(cwd, 'results')


# All pixels averaged
true_average = RenderOptions(
    path=os.path.join(dist_folder_path, 'true_average.png'),
    min_avg_alpha_perc=0,
    color_overflow_by_alpha=False,
    scale=scale
)

# All pixels averaged - everything ignored that doesn't have 255*0.6 alpha
some_transparent_ignored = RenderOptions(
    path=os.path.join(dist_folder_path, 'some_transparent_ignored.png'),
    min_avg_alpha_perc=0.6,
    color_overflow_by_alpha=False,
    scale=scale
)

# All pixels averaged - everything ignored that doesn't have 255 alpha
all_transparent_ignored = RenderOptions(
    path=os.path.join(dist_folder_path, 'all_transparent_ignored.png'),
    min_avg_alpha_perc=1,
    color_overflow_by_alpha=False,
    scale=scale
)

# All pixels averaged - everything ignored that doesn't have 255 alpha.
# Every pixels r,g,b are multiplied by it's alpha and 255 before averaging
all_transparent_ignored_color_overflow = RenderOptions(
    path=os.path.join(dist_folder_path, 'all_transparent_ignored_color_overflow.png'),
    min_avg_alpha_perc=1,
    color_overflow_by_alpha=True,
    scale=scale
)


# ----------------------------------- Flow ----------------------------------- #

generate_images(
    cache_folder_path=os.path.join(cwd, 'cache'),
    options=[
        true_average,
        some_transparent_ignored,
        all_transparent_ignored,
        all_transparent_ignored_color_overflow
    ]
)


# ---------------------------------------------------------------------------- #