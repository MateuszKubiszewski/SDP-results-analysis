from enum import Enum

class MicrophoneTypeEnum(str, Enum):
    BINAURAL = "BINAURAL"
    AMBEO = "AMBEO"
    ZYLIA = "ZYLIA"

class OrientationTypeEnum(str, Enum):
    AZIMUTH = "AZIMUTH"
    ELEVATION = "ELEVATION"

class SoundTypeEnum(str, Enum):
    TRUMPET = "TRUMPET"
    DUCK = "DUCK"
    NOISE = "NOISE"
    ANGRY = "ANGRY"
    SWEET = "SWEET"