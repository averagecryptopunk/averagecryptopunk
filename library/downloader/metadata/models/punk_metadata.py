# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import List

# Local
from .enums import PunkType, Acccessory

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ class: PunkMetadata ----------------------------------------------------- #

class PunkMetadata:

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        id_: int,
        type_: PunkType,
        accessories: List[Acccessory]
    ):
        self.id = id_
        self.type = type_
        self.accessories = accessories

    @staticmethod
    def from_json(
        j: dict
    ):
        try:
            return PunkMetadata(
                id_         = j['id'],
                type_       = PunkType(j['type']),
                accessories = [Acccessory(a) for a in j['accs']],
            )
        except:
            return None


# -------------------------------------------------------------------------------------------------------------------------------- #