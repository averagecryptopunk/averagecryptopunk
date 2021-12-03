# ---------------------------------- Imports --------------------------------- #

# System
from typing import Optional, Tuple

# ---------------------------------------------------------------------------- #



# ---------------------------------------------------------------------------- #

class RenderOptions:

    # ------------------------------- Init ------------------------------ #

    def __init__(
        self,
        path: str,
        min_avg_alpha_perc: float = 0,
        color_overflow_by_alpha: bool = False,
        size: int = 2**10,
        bg_color: Optional[Tuple[int, int, int]] = None
    ):
        self.path = path
        self.min_avg_alpha_perc = min_avg_alpha_perc
        self.color_overflow_by_alpha = color_overflow_by_alpha
        self.size = size
        self.bg_color = bg_color


# ---------------------------------------------------------------------------- #