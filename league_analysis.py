#!/usr/bin/env python3
import os
import sys
import pandas

from data_processing import process_data
from visualizations import create_visualizations

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

results_path = "./input/results.csv"
stats_path = "./input/stats.csv"
output_dir = "./output"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Tee Logger - writes to both console and file
class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

    def close(self):
        self.log.close()

# Set up logging
logger = Logger(os.path.join(output_dir, "analysis.txt"))
sys.stdout = logger

def plot_rules(rules, title, output_filename):
    """
    Generate a bar chart for the top 10 association rules based on confidence.
    
    Parameters:
    - rules: DataFrame containing the association rules.
    - title: Title for the plot.
    - output_filename: Path to save the resulting plot.
    """
    # Sort rules by confidence and pick the top 10
    rules_sorted = rules.sort_values(by="confidence", ascending=False).head(10)
    
    # Create labels from the antecedents
    labels = [", ".join(list(antecedent)) for antecedent in rules_sorted["antecedents"]]
    
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(rules_sorted)), rules_sorted["confidence"], tick_label=labels)
    plt.title(title)
    plt.xlabel("Rule (Antecedents)")
    plt.ylabel("Confidence")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    
    # Save the plot to a file
    plt.savefig(output_filename)
    plt.show()

def get_home_goals_win_rule(results):
    # Returns association rules for home_goals,year->home_win

    # Create feature home_score_season
    results['home_score_season'] = results['home_goals'].astype(int).astype(str) + "_home_goals_" + results['season_start'].astype(str)

    # Set HomeWin as target
    results['HomeWin'] = results['result'] == 'H'

    # Convert to one-hot encoded dataframe
    results_rules = pandas.get_dummies(results['home_score_season'])
    results_rules['HomeWin'] = results['HomeWin']

    # Apply Apriori algorithm
    frequent_itemsets = apriori(results_rules, min_support=0.01, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.5)

    # Filter for consequent HomeWin
    home_win_rules = rules[rules['consequents'] == {'HomeWin'}]
    home_win_rules = home_win_rules.sort_values(by='confidence', ascending=False)

    # Getting the count
    num_matches = len(results_rules)
    home_win_rules['count'] = (home_win_rules['support'] * num_matches).round().astype(int)

    return home_win_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift', 'count']]

def get_away_goals_win_rule(results):
    # Returns association rules for away_goals,year->away_win

    # Create feature home_score_season
    results['away_score_season'] = results['away_goals'].astype(int).astype(str) + "_away_goals_" + results['season_start'].astype(str)

    # Set AwayWin as target
    results['AwayWin'] = results['result'] == 'A'

    # Convert to one-hot encoded dataframe
    results_rules = pandas.get_dummies(results['away_score_season'])
    results_rules['AwayWin'] = results['AwayWin']

    # Apply Apriori algorithm
    frequent_itemsets = apriori(results_rules, min_support=0.005, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.5)

    # Filter for consequent AwayWin
    away_win_rules = rules[rules['consequents'] == {'AwayWin'}]
    away_win_rules = away_win_rules.sort_values(by='confidence', ascending=False)

    # Getting the count
    num_matches = len(results_rules)
    away_win_rules['count'] = (away_win_rules['support'] * num_matches).round().astype(int)

    return away_win_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift', 'count']]


def get_team_goals_win_rule(results):
    # Returns association rules for team_goals,year->team_win

    rows = []
    for _, row in results.iterrows():
        # Home team record
        if row['result'] == 'H':
            home_result = 'win'
            away_result = 'lose'
        elif row['result'] == 'A':
            home_result = 'lose'
            away_result = 'win'
        else:
            home_result = 'draw'
            away_result = 'draw'

        rows.append([
            f"team:{row['home_team']}",
            'role:home',
            f"goals:{int(row['home_goals'])}",
            f"season:{row['season_start']}",
            f"result:{home_result}"
        ])

        # Away team record
        rows.append([
            f"team:{row['away_team']}",
            'role:away',
            f"goals:{int(row['away_goals'])}",
            f"season:{row['season_start']}",
            f"result:{away_result}"
        ])

    # Transaction encoding
    te = TransactionEncoder()
    te_ary = te.fit(rows).transform(rows)
    df_trans = pandas.DataFrame(te_ary, columns=te.columns_)

    # Find frequent itemsets with minimum support threshold
    frequent_itemsets = apriori(df_trans, min_support=0.01, use_colnames=True)

    # Generate association rules from frequent itemsets with confidence threshold
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

    # Filter rules where consequent is win
    win_rules = rules[rules['consequents'].apply(lambda x: 'result:win' in x)]

    # Filter rules where antecedents include a team
    win_rules_with_team = win_rules[win_rules['antecedents'].apply(lambda x: any(item.startswith('team:') for item in x))]

    # Return relevant columns
    return win_rules_with_team[['antecedents', 'consequents', 'support', 'confidence', 'lift']]

# Stub Function for analysis
def analyze_data(results, stats):
    print("Analyzing Data")
    print(f"Results shape: {results.shape}")
    print(f"Stats shape: {stats.shape}")

    home_rules = get_home_goals_win_rule(results)
    away_rules = get_away_goals_win_rule(results)
    team_rules = get_team_goals_win_rule(results)

    # Print the rules for text-based output
    print(home_rules)
    print(away_rules)
    print(team_rules)
    
    # Now, plot the top rules and save the visuals in the 'output' folder
    plot_rules(home_rules, "Top Home Win Rules", "output/home_win_rules.png")
    plot_rules(away_rules, "Top Away Win Rules", "output/away_win_rules.png")
    plot_rules(team_rules, "Top Team Win Rules", "output/team_win_rules.png")

def main():
    # Load the data

    if not os.path.exists("output"):
        os.makedirs("output")

    results = pandas.read_csv(results_path);
    stats = pandas.read_csv(stats_path);

    results_processed, stats_processed = process_data(results, stats);

    analyze_data(results_processed, stats_processed);

    create_visualizations(results_processed, stats_processed);

if __name__ == "__main__":
    main()
