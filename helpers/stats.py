import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from helpers.data_peparation import \
    get_data_for_each_orientation_type, \
    get_data_for_each_sound_type

from helpers.funs import \
    get_average_distance, \
    get_distance_quantiles, \
    get_percentage_of_mistakes_lower_than, \
    print_stats


def save_average_distance_statistics_for_sounds(binaural_df: pd.DataFrame, ambeo_df: pd.DataFrame, zylia_df: pd.DataFrame):
    bin_trumpet, bin_duck, bin_noise, bin_angry, bin_sweet = get_data_for_each_sound_type(binaural_df)
    bin_noise_az, bin_noise_el = get_data_for_each_orientation_type(bin_noise)

    amb_trumpet, amb_duck, amb_noise, amb_angry, amb_sweet = get_data_for_each_sound_type(ambeo_df)
    amb_noise_az, amb_noise_el = get_data_for_each_orientation_type(amb_noise)

    zyl_trumpet, zyl_duck, zyl_noise, zyl_angry, zyl_sweet = get_data_for_each_sound_type(zylia_df)
    zyl_noise_az, zyl_noise_el = get_data_for_each_orientation_type(zyl_noise)

    bin_trumpet_avg, bin_duck_avg, bin_noise_az_avg, bin_noise_el_avg, bin_angry_avg, bin_sweet_avg = get_average_distance([
        bin_trumpet, bin_duck, bin_noise_az, bin_noise_el, bin_angry, bin_sweet
    ])

    amb_trumpet_avg, amb_duck_avg, amb_noise_az_avg, amb_noise_el_avg, amb_angry_avg, amb_sweet_avg = get_average_distance([
        amb_trumpet, amb_duck, amb_noise_az, amb_noise_el, amb_angry, amb_sweet
    ])

    zyl_trumpet_avg, zyl_duck_avg, zyl_noise_az_avg, zyl_noise_el_avg, zyl_angry_avg, zyl_sweet_avg = get_average_distance([
        zyl_trumpet, zyl_duck, zyl_noise_az, zyl_noise_el, zyl_angry, zyl_sweet
    ])

    print_stats(
        "Average distance across sounds [Trumpet, Duck, Noise AZ, Noise EL, Angry, Sweet]",
        [bin_trumpet_avg, bin_duck_avg, bin_noise_az_avg, bin_noise_el_avg, bin_angry_avg, bin_sweet_avg],
        [amb_trumpet_avg, amb_duck_avg, amb_noise_az_avg, amb_noise_el_avg, amb_angry_avg, amb_sweet_avg],
        [zyl_trumpet_avg, zyl_duck_avg, zyl_noise_az_avg, zyl_noise_el_avg, zyl_angry_avg, zyl_sweet_avg]
    )

    plotdata = pd.DataFrame({
            "Trumpet [Azimuth]": [
                bin_trumpet_avg,
                amb_trumpet_avg,
                zyl_trumpet_avg
            ],
            "Duck [Elevation]": [
                bin_duck_avg,
                amb_duck_avg,
                zyl_duck_avg
            ],
            "Noise [Azimuth]": [
                bin_noise_az_avg,
                amb_noise_az_avg,
                zyl_noise_az_avg
            ],
            "Noise [Elevation]": [
                bin_noise_el_avg,
                amb_noise_el_avg,
                zyl_noise_el_avg
            ],
            "Angry [Azimuth]": [
                bin_angry_avg,
                amb_angry_avg,
                zyl_angry_avg
            ],
            "Sweet [Elevation]": [
                bin_sweet_avg,
                amb_sweet_avg,
                zyl_sweet_avg
            ]
        },
        index = ["Binaural", "Ambeo", "Zylia"]
    )
    
    plotdata.plot(kind = "bar")
    plt.legend(bbox_to_anchor = (1.0, 1.0))
    plt.title("Average distance across microphones and sounds")
    plt.xlabel("Microphone Type")
    plt.ylabel("Average distance [degrees]")
    plt.ylim([0, 120])
    plt.savefig("./results/average_distances_sounds.png", bbox_inches="tight")


def save_average_distance_statistics_for_microphones(binaural: pd.DataFrame, ambeo: pd.DataFrame, zylia: pd.DataFrame):
    binaural_azimuth, binaural_elevation = get_data_for_each_orientation_type(binaural)
    ambeo_azimuth, ambeo_elevation = get_data_for_each_orientation_type(ambeo)
    zylia_azimuth, zylia_elevation = get_data_for_each_orientation_type(zylia)

    bin_avg_dist, bin_az_avg_dist, bin_el_avg_dist = get_average_distance([binaural, binaural_azimuth, binaural_elevation])
    amb_avg_dist, amb_az_avg_dist, amb_el_avg_dist = get_average_distance([ambeo, ambeo_azimuth, ambeo_elevation])
    zyl_avg_dist, zyl_az_avg_dist, zyl_el_avg_dist = get_average_distance([zylia, zylia_azimuth, zylia_elevation])

    print_stats(
        "Average distance across microphones and orientations",
        [bin_az_avg_dist, bin_el_avg_dist, bin_avg_dist],
        [amb_az_avg_dist, amb_el_avg_dist, amb_avg_dist],
        [zyl_az_avg_dist, zyl_el_avg_dist, zyl_avg_dist]
    )

    plotdata = pd.DataFrame({
            "Azimuth": [
                bin_az_avg_dist,
                amb_az_avg_dist,
                zyl_az_avg_dist
            ],
            "Elevation": [
                bin_el_avg_dist,
                amb_el_avg_dist,
                zyl_el_avg_dist
            ],
            "Overall": [
                bin_avg_dist,
                amb_avg_dist,
                zyl_avg_dist
            ],
        },
        index = ["Binaural", "Ambeo", "Zylia"]
    )
    
    plotdata.plot(kind = "bar")
    plt.title("Average distance across microphones and orientations")
    plt.xlabel("Microphone Type")
    plt.ylabel("Average distance [degrees]")
    plt.ylim([0, 120])
    plt.savefig("./results/average_distances_microphones.png", bbox_inches="tight")


def save_quantile_statistics(original_df: pd.DataFrame, binaural_df: pd.DataFrame, ambeo_df: pd.DataFrame, zylia_df: pd.DataFrame):
    q1, q2, q3 = get_distance_quantiles(original_df)

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