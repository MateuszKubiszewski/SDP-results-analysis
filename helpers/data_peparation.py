import numpy as np
import pandas as pd

from typing import Tuple

from helpers.enums import Column, MicrophoneType, OrientationType, SoundType


def get_data_for_each_microphone_type(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    return (
        df.loc[df[Column.MICROPHONE] == MicrophoneType.BINAURAL],
        df.loc[df[Column.MICROPHONE] == MicrophoneType.AMBEO],
        df.loc[df[Column.MICROPHONE] == MicrophoneType.ZYLIA]
    )


def get_data_for_each_orientation_type(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    return (
        df.loc[df[Column.ORIENTATION] == OrientationType.AZIMUTH],
        df.loc[df[Column.ORIENTATION] == OrientationType.ELEVATION]
    )


def get_data_for_each_sound_type(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    return (
        df.loc[df[Column.SOUND] == SoundType.TRUMPET],
        df.loc[df[Column.SOUND] == SoundType.DUCK],
        df.loc[df[Column.SOUND] == SoundType.NOISE],
        df.loc[df[Column.SOUND] == SoundType.ANGRY],
        df.loc[df[Column.SOUND] == SoundType.SWEET],
    )


def add_distance_columns(df: pd.DataFrame):
    df.loc[:, Column.DISTANCE_A] = np.abs(df[Column.ANGLE].values - df[Column.ANSWER].values)
    df.loc[:, Column.DISTANCE_B] = 360 - np.abs(df[Column.ANGLE].values - df[Column.ANSWER].values)
    df.loc[:, Column.DISTANCE] = np.minimum(df[Column.DISTANCE_A].values, df[Column.DISTANCE_B].values)


def load_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path, sep = ",").dropna()
    add_distance_columns(data)
    return data