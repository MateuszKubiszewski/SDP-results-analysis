import helpers.data_preparation as preparation
import helpers.stats as stats


if __name__ == "__main__":
    data = preparation.load_data("./data/wyniki_analiza2.csv")

    binaural_df, ambeo_df, zylia_df = preparation.get_data_for_each_microphone_type(data)

    stats.save_quantile_statistics(data, binaural_df, ambeo_df, zylia_df)

    stats.save_average_distance_statistics_for_microphones(binaural_df, ambeo_df, zylia_df)
    
    stats.save_average_distance_statistics_for_microphones_sounds(binaural_df, ambeo_df, zylia_df)

    stats.save_average_distance_statistics_for_sounds(data)