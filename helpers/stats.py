import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from helpers.data_peparation import get_data_for_each_orientation_type
from helpers.funs import get_percentage_of_mistakes_lower_than, print_stats
from helpers.enums import Column


def save_average_distance_statistics(binaural_df: pd.DataFrame, ambeo_df: pd.DataFrame, zylia_df: pd.DataFrame):
    binaural_azimuth_df, binaural_elevation_df = get_data_for_each_orientation_type(binaural_df)
    ambeo_azimuth_df, ambeo_elevation_df = get_data_for_each_orientation_type(ambeo_df)
    zylia_azimuth_df, zylia_elevation_df = get_data_for_each_orientation_type(zylia_df)

    binaural_average_distance = np.round(np.average(binaural_df[Column.DISTANCE].values), 2)
    binaural_azimuth_average_distance = np.round(np.average(binaural_azimuth_df[Column.DISTANCE].values), 2)
    binaural_elevation_average_distance = np.round(np.average(binaural_elevation_df[Column.DISTANCE].values), 2)

    ambeo_average_distance = np.round(np.average(ambeo_df[Column.DISTANCE].values), 2)
    ambeo_azimuth_average_distance = np.round(np.average(ambeo_azimuth_df[Column.DISTANCE].values), 2)
    ambeo_elevation_average_distance = np.round(np.average(ambeo_elevation_df[Column.DISTANCE].values), 2)

    zylia_average_distance = np.round(np.average(zylia_df[Column.DISTANCE].values), 2)
    zylia_azimuth_average_distance = np.round(np.average(zylia_azimuth_df[Column.DISTANCE].values), 2)
    zylia_elevation_average_distance = np.round(np.average(zylia_elevation_df[Column.DISTANCE].values), 2)

    print_stats(
        "Average distance across microphones and orientations",
        [binaural_azimuth_average_distance, binaural_elevation_average_distance, binaural_average_distance],
        [ambeo_azimuth_average_distance, ambeo_elevation_average_distance, ambeo_average_distance],
        [zylia_azimuth_average_distance, zylia_elevation_average_distance, zylia_average_distance]
    )

    plotdata = pd.DataFrame({
            "Azimuth": [
                binaural_azimuth_average_distance,
                ambeo_azimuth_average_distance,
                zylia_azimuth_average_distance
            ],
            "Elevation": [
                binaural_elevation_average_distance,
                ambeo_elevation_average_distance,
                zylia_elevation_average_distance
            ],
            "Overall": [
                binaural_average_distance,
                ambeo_average_distance,
                zylia_average_distance
            ],
        },
        index = ["Binaural", "Ambeo", "Zylia"]
    )
    
    plotdata.plot(kind = "bar")
    plt.title("Average distance across microphones and orientations")
    plt.xlabel("Microphone Type")
    plt.ylabel("Average distance")
    plt.ylim([0, 120])
    plt.savefig("./results/average_distances.png", bbox_inches="tight")


def save_quantile_statistics(original_df: pd.DataFrame, binaural_df: pd.DataFrame, ambeo_df: pd.DataFrame, zylia_df: pd.DataFrame):
    q1, q2, q3 = original_df[Column.DISTANCE].quantile([0.25, 0.50, 0.75])

    binaural_q1 = get_percentage_of_mistakes_lower_than(binaural_df, q1)
    binaural_q2 = get_percentage_of_mistakes_lower_than(binaural_df, q2)
    binaural_q3 = get_percentage_of_mistakes_lower_than(binaural_df, q3)
    ambeo_q1 = get_percentage_of_mistakes_lower_than(ambeo_df, q1)
    ambeo_q2 = get_percentage_of_mistakes_lower_than(ambeo_df, q2)
    ambeo_q3 = get_percentage_of_mistakes_lower_than(ambeo_df, q3)
    zylia_q1 = get_percentage_of_mistakes_lower_than(zylia_df, q1)
    zylia_q2 = get_percentage_of_mistakes_lower_than(zylia_df, q2)
    zylia_q3 = get_percentage_of_mistakes_lower_than(zylia_df, q3)

    print_stats(
        "Percentage of mistakes lower than quantile",
        [binaural_q1, binaural_q2, binaural_q3],
        [ambeo_q1, ambeo_q2, ambeo_q3],
        [zylia_q1, zylia_q2, zylia_q3]
    )

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