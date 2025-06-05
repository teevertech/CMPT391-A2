#!/usr/bin/env python3

import sys
import pandas

results_path = "./input/results.csv"
stats_path = "./input/stats.csv"


# Remove unecessary columns and add information where needed
def clean_data():

    # Load the data
    results = pandas.read_csv(results_path);
    stats = pandas.read_csv(stats_path);

    # Example cleaning section
    drop_cols = ['big_chance_missed', 'backward_pass']
    stats_cleaned = stats.drop(columns=drop_cols)

    results_cleaned = results; # just a stub for the return function

    return results_cleaned, stats_cleaned;

# Stub Function for analysis
def analyze_data(results, stats):
    print("Analyzing Data");
    print(f"Results shape: {results.shape}");
    print(f"Stats shape: {stats.shape}");

    return

def main():
    results_cleaned, stats_cleaned = clean_data();

    analyze_data(results_cleaned, stats_cleaned);

if __name__ == "__main__":
    main()