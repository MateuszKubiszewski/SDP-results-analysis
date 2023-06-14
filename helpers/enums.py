from enum import Enum

class Column(str, Enum):
    MICROPHONE = "MICROPHONE"
    ORIENTATION = "ORIENTATION"
    SOUND = "SOUND"
    ANGLE = "ANGLE"
    ANSWER = "ANSWER"
    PERSON = "PERSON"
    DISTANCE = "DISTANCE"
    DISTANCE_A = "DISTANCE_A"
    DISTANCE_B = "DISTANCE_B"

class MicrophoneType(str, Enum):
    BINAURAL = "BINAURAL"
    AMBEO = "AMBEO"
    ZYLIA = "ZYLIA"

class OrientationType(str, Enum):
    AZIMUTH = "AZIMUTH"
    ELEVATION = "ELEVATION"

class SoundType(str, Enum):
    TRUMPET = "TRUMPET"
    DUCK = "DUCK"
    NOISE = "NOISE"
    ANGRY = "ANGRY"
    SWEET = "SWEET"