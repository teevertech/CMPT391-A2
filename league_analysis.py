#!/usr/bin/env python3

import sys
import pandas
from data_processing import process_data 

results_path = "./input/results.csv"
stats_path = "./input/stats.csv"

# Stub Function for analysis
def analyze_data(results, stats):
    print("Analyzing Data");
    print(f"Results shape: {results.shape}");
    print(f"Stats shape: {stats.shape}");

    return

def main():
    # Load the data
    results = pandas.read_csv(results_path);
    stats = pandas.read_csv(stats_path);

    results_processed, stats_processed = process_data(results, stats);

    analyze_data(results_processed, stats_processed);

if __name__ == "__main__":
    main()