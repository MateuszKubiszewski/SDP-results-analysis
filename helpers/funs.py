import numpy as np
import pandas as pd

def get_percentage_of_mistakes_lower_than(df: pd.DataFrame, value):
    return np.round((df["DISTANCE"] < value).sum() * 100 / df.shape[0], 2)

def print_stats(title, binaural_stats, ambeo_stats, zylia_stats):
    print(f"\
        {title}\n\
        BINAURAL: {binaural_stats}\n\
        AMBEO: {ambeo_stats}\n\
        ZYLIA: {zylia_stats}\n")