# ---------------------------------------------------------------------------- #

class RenderOptions:

    def __init__(
        self,
        path: str,
        min_avg_alpha_perc: float = 0,
        color_overflow_by_alpha: bool = False,
        scale: int = 1
    ):
        self.path = path
        self.min_avg_alpha_perc = min_avg_alpha_perc
        self.color_overflow_by_alpha = color_overflow_by_alpha
        self.scale = scale


# ---------------------------------------------------------------------------- #