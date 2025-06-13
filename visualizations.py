import os

import matplotlib.pyplot as plt
import seaborn as sns

output_dir = "./output"

def create_visualizations(results, stats):
    print("Creating Visualizations\n")

    # https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
    # Match outcomes pie chart (proof of concept)
    plt.figure(figsize=(8, 8))
    outcome_counts = results['result'].value_counts()
    labels = ['Home Win', 'Away Win', 'Draw']
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    plt.pie(outcome_counts.values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Match Outcome Distribution', fontsize=14)
    plt.savefig(os.path.join(output_dir, 'fig1_match_outcomes.png'), dpi=300, bbox_inches='tight')
    plt.close()
