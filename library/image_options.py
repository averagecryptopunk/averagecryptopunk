# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional

# Local
from typing import Optional
from .renderer import RenderOptions
from .downloader import PunkType

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ class: ImageOptions ----------------------------------------------------- #

class ImageOptions(RenderOptions):

    def __init__(
        self,
        path: str,
        min_avg_alpha_perc: float = 0,
        color_overflow_by_alpha: bool = False,
        scale: int = 1,
        punk_type: Optional[PunkType] = None
    ):
        self.punk_type = punk_type

        super().__init__(
            path=path,
            min_avg_alpha_perc=min_avg_alpha_perc,
            color_overflow_by_alpha=color_overflow_by_alpha,
            scale=scale
        )


# -------------------------------------------------------------------------------------------------------------------------------- #