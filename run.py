import helpers.data_preparation as preparation
import helpers.stats as stats


if __name__ == "__main__":
    data = preparation.load_data("./data/wyniki_analiza2.csv")

    binaural, ambeo, zylia = preparation.get_data_for_each_microphone_type(data)

    stats.save_quantile_statistics(data, binaural, ambeo, zylia)

    stats.save_quantile_statistics_with_orientations(data, binaural, ambeo, zylia)

    stats.save_average_distance_statistics_for_orientations(data)

    stats.save_average_distance_statistics_for_microphones(binaural, ambeo, zylia)

    stats.save_distance_std_dev_statistics_for_microphones(binaural, ambeo, zylia)
    
    stats.save_average_distance_statistics_for_microphones_sounds(binaural, ambeo, zylia)

    stats.save_average_distance_statistics_for_sounds(data)