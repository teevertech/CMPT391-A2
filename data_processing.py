# Remove unnecessary columns and add additional cleaning steps where needed
def clean_data(results, stats):
    # Drop predefined columns from stats, with error handling in case they do not exist.
    drop_cols = ['big_chance_missed', 'backward_pass']
    stats_cleaned = stats.drop(columns=drop_cols, errors='ignore')
    results_cleaned = results.copy()
    
    # Handling missing values:
    # For the results dataset, we use forward fill (adjust method as needed)
    results_cleaned = results_cleaned.fillna(method='ffill')
    # For stats, drop rows with missing values (could also choose to fill these?)
    stats_cleaned = stats_cleaned.dropna()
    
    # Standardize text fields in the results dataset (e.g., team names)
    if 'home_team' in results_cleaned.columns:
        results_cleaned['home_team'] = results_cleaned['home_team'].str.strip().str.lower()
    if 'away_team' in results_cleaned.columns:
        results_cleaned['away_team'] = results_cleaned['away_team'].str.strip().str.lower()
    
    # Remove any duplicate rows to ensure clean data
    results_cleaned = results_cleaned.drop_duplicates()
    stats_cleaned = stats_cleaned.drop_duplicates()
    
    # Return the cleaned datasets
    return results_cleaned, stats_cleaned

def process_data(results, stats):
    # Get cleaned data first
    results_cleaned, stats_cleaned = clean_data(results, stats)
    
    # Process the season information for results:
    results_cleaned["season_start"] = results_cleaned["season"].str[:4].astype(int)
    results_cleaned = results_cleaned.drop(columns=["season"])
    results_processed = results_cleaned
    
    # Process the season information for stats:
    stats_cleaned["season_start"] = stats_cleaned["season"].str[:4].astype(int)
    stats_cleaned = stats_cleaned.drop(columns=["season"])
    stats_processed = stats_cleaned
    
    # Return the processed data
    return results_processed, stats_processed

