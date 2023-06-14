import numpy as np
import pandas as pd

from typing import List, Tuple

from helpers.enums import Column


def get_average_distance(dfs: List[pd.DataFrame]) -> List[float]:
    distances_data = [df[Column.DISTANCE].values for df in dfs]
    return [np.round(np.mean(distance_data), 2) for distance_data in distances_data]


def get_distance_quantiles(df: pd.DataFrame) -> Tuple[float, float, float]:
    return df[Column.DISTANCE].quantile([0.25, 0.50, 0.75])


def get_percentage_of_mistakes_lower_than(df: pd.DataFrame, value) -> float:
    return np.round((df["DISTANCE"] < value).sum() * 100 / df.shape[0], 2)


def print_stats(title, binaural_stats, ambeo_stats, zylia_stats) -> None:
    print(f"\
        {title}\n\
        BINAURAL: {binaural_stats}\n\
        AMBEO: {ambeo_stats}\n\
        ZYLIA: {zylia_stats}\n")