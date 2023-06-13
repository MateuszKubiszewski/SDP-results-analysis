import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from typing import Tuple

from helpers.enums import MicrophoneTypeEnum, OrientationTypeEnum, SoundTypeEnum

def get_data_for_each_microphone_type(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    return (
        df.loc[df["MICROPHONE"] == MicrophoneTypeEnum.BINAURAL],
        df.loc[df["MICROPHONE"] == MicrophoneTypeEnum.AMBEO],
        df.loc[df["MICROPHONE"] == MicrophoneTypeEnum.ZYLIA]
    )

def add_distance_columns(df: pd.DataFrame):
    df.loc[:, "DISTANCE_A"] = np.abs(df["ANGLE"].values - df["ANSWER"].values)
    df.loc[:, "DISTANCE_B"] = 360 - np.abs(df["ANGLE"].values - df["ANSWER"].values)
    df.loc[:, "DISTANCE"] = np.minimum(df["DISTANCE_A"].values, df["DISTANCE_B"].values)

def get_percentage_of_mistakes_lower_than(df: pd.DataFrame, value):
    return np.round((df["DISTANCE"] < value).sum() * 100 / df.shape[0], 2)

def save_average_distance_statistics(df: pd.DataFrame):
    add_distance_columns(df)
    binaural_df, ambeo_df, zylia_df = get_data_for_each_microphone_type(df)

    binaural_average_distance = np.round(np.average(binaural_df["DISTANCE"].values), 2)
    ambeo_average_distance = np.round(np.average(ambeo_df["DISTANCE"].values), 2)
    zylia_average_distance = np.round(np.average(zylia_df["DISTANCE"].values), 2)

    print(f"\
            BINAURAL: {binaural_average_distance}\n\
            AMBEO: {ambeo_average_distance}\n\
            ZYLIA: {zylia_average_distance}\n")

    plotdata = pd.DataFrame({
            "avg_dist": [binaural_average_distance, ambeo_average_distance, zylia_average_distance]
        },
        index = ["Binaural", "Ambeo", "Zylia"]
    )
    
    plotdata.plot(kind = "bar", legend = False)
    plt.xlabel("Microphone Type")
    plt.ylabel("Average distance")
    plt.savefig("./results/average_distances.png", bbox_inches="tight")

def save_quantile_statistics(df: pd.DataFrame):
    add_distance_columns(df)
    binaural_df, ambeo_df, zylia_df = get_data_for_each_microphone_type(df)
    q1, q2, q3 = df["DISTANCE"].quantile([0.25, 0.50, 0.75])

    binaural_q1 = get_percentage_of_mistakes_lower_than(binaural_df, q1)
    binaural_q2 = get_percentage_of_mistakes_lower_than(binaural_df, q2)
    binaural_q3 = get_percentage_of_mistakes_lower_than(binaural_df, q3)
    ambeo_q1 = get_percentage_of_mistakes_lower_than(ambeo_df, q1)
    ambeo_q2 = get_percentage_of_mistakes_lower_than(ambeo_df, q2)
    ambeo_q3 = get_percentage_of_mistakes_lower_than(ambeo_df, q3)
    zylia_q1 = get_percentage_of_mistakes_lower_than(zylia_df, q1)
    zylia_q2 = get_percentage_of_mistakes_lower_than(zylia_df, q2)
    zylia_q3 = get_percentage_of_mistakes_lower_than(zylia_df, q3)

    print(f"\
            BINAURAL: {binaural_q1}, {binaural_q2}, {binaural_q3}\n\
            AMBEO: {ambeo_q1}, {ambeo_q2}, {ambeo_q3}\n\
            ZYLIA: {zylia_q1}, {zylia_q2}, {zylia_q3}\n")

    plotdata = pd.DataFrame({
            "Q1": [binaural_q1, ambeo_q1, zylia_q1],
            "Q2": [binaural_q2, ambeo_q2, zylia_q2],
            "Q3": [binaural_q3, ambeo_q3, zylia_q3] 
        },
        index = ["Binaural", "Ambeo", "Zylia"]
    )

    plotdata.plot(kind = "bar")
    plt.title("Mistakes lower than quantile")
    plt.xlabel("Microphone Type")
    plt.ylabel("Percentage")
    plt.ylim([0, 100])
    plt.savefig("./results/quantiles_statistics.png", bbox_inches="tight")

if __name__ == "__main__":
    data = pd.read_csv("./data/wyniki_analiza.csv", sep = ",").dropna()
    # top_data = data[:5]
    # print(top_data)
    save_average_distance_statistics(data)
    save_quantile_statistics(data)