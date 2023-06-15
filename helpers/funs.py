import numpy as np
import pandas as pd

from typing import List, Tuple

from helpers.enums import Column


def get_average_distance(dfs: List[pd.DataFrame]) -> List[float]:
    distances_data = [df[Column.DISTANCE].values for df in dfs]
    return [np.round(np.mean(distance_data), 2) for distance_data in distances_data]


def get_distance_std_dev(dfs: List[pd.DataFrame]) -> List[float]:
    distances_data = [df[Column.DISTANCE].values for df in dfs]
    return [np.round(np.std(distance_data), 2) for distance_data in distances_data]


def get_distance_quantiles(dfs: List[pd.DataFrame]) -> List[Tuple[float, float, float]]:
    distances_columns = [df[Column.DISTANCE] for df in dfs]
    return [distances_column.quantile([0.25, 0.50, 0.75]) for distances_column in distances_columns]


def get_percentage_of_mistakes_lower_than(df: pd.DataFrame, values: List[float]) -> List[float]:
    return [np.round((df[Column.DISTANCE] < value).sum() * 100 / df.shape[0], 2) for value in values]


def print_stats(title, binaural_stats, ambeo_stats, zylia_stats) -> None:
    print(f"\n\
        {title}\n\
        BINAURAL: {binaural_stats}\n\
        AMBEO: {ambeo_stats}\n\
        ZYLIA: {zylia_stats}\n")
    

def print_stats_no_microphones(title, stats) -> None:
    print(f"\n\
        {title}\n\
        RESULT: {stats}\n")