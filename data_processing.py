# Remove unecessary columns and add information where needed
def clean_data(results, stats):

    # Example cleaning section
    drop_cols = ['big_chance_missed', 'backward_pass']
    stats_cleaned = stats.drop(columns=drop_cols)

    results_cleaned = results; # just a stub for the return function

    return results_cleaned, stats_cleaned;

def process_data(results, stats):
    results_cleaned, stats_cleaned = clean_data(results, stats)

    results_cleaned["season_start"] = results_cleaned["season"].str[:4].astype(int)
    results_cleaned = results_cleaned.drop(columns=["season"])
    results_processed = results_cleaned

    stats_cleaned["season_start"] = stats_cleaned["season"].str[:4].astype(int)
    stats_cleaned = stats_cleaned.drop(columns=["season"])
    stats_processed = stats_cleaned

    return results_processed, stats_processed
