from enum import Enum

class ChangeType(Enum):
    FLIP = 1
    PHONEME = 2
    ADD = 3
    SWAP = 4
    DROP = 5
    NONE = 6