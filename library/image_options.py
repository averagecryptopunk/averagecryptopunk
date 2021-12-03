# ---------------------------------- Imports --------------------------------- #

# System
from typing import Optional, Tuple, Union, List

# Local
from .renderer import RenderOptions
from .downloader import PunkType

# ---------------------------------------------------------------------------- #



# ---------------------------- class: ImageOptions --------------------------- #

class ImageOptions(RenderOptions):

    # ------------------------------- Init ------------------------------ #

    def __init__(
        self,
        path: str,
        min_avg_alpha_perc: float = 0,
        color_overflow_by_alpha: bool = False,
        size: int = 2**10,
        bg_color: Optional[Tuple[int, int, int]] = None,
        punk_type: Optional[Union[PunkType, List[PunkType]]] = None
    ):
        self.punk_types = [punk_type] if isinstance(punk_type, PunkType) else punk_type

        super().__init__(
            path=path,
            min_avg_alpha_perc=min_avg_alpha_perc,
            color_overflow_by_alpha=color_overflow_by_alpha,
            size=size,
            bg_color=bg_color
        )


# ---------------------------------------------------------------------------- #