import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = {
    'Scenario': ['Corporate Office', 'VPN / Remote', 'Public Wi-Fi', 'BYOD / Guest', 'Untrusted', 'Compromised'],
    'Network Trust': [0.95, 0.85, 0.30, 0.90, 0.30, 0.20],
    'Device Trust': [0.95, 0.90, 0.75, 0.40, 0.30, 0.20],
    'Data Trust (Sens)': [0.90, 0.85, 0.60, 0.50, 0.30, 0.20],
    'App Risk Posture': [0.90, 0.90, 0.70, 0.60, 0.30, 0.20],
    'Decision': ['Full', 'Full', 'Limited', 'Limited', 'No', 'No']
}

df = pd.DataFrame(data)

def save_table_image():
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis('tight')
    ax.axis('off')
    
    # Create table
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
    
    # Style
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    
    # Header styling
    for k, cell in table.get_celld().items():
        if k[0] == 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#40466e')
    
    plt.title("Common Network Access Scenarios", fontsize=16, pad=20)
    plt.savefig('scenarios_table.png', bbox_inches='tight', dpi=300)
    print("Saved scenarios_table.png")

def save_graphs():
    # Setup for grouped bar chart
    x = np.arange(len(df['Scenario']))
    width = 0.2
    
    fig, ax = plt.subplots(figsize=(14, 6))
    
    rects1 = ax.bar(x - 1.5*width, df['Network Trust'], width, label='Network Trust', color='#1f77b4')
    rects2 = ax.bar(x - 0.5*width, df['Device Trust'], width, label='Device Trust', color='#ff7f0e')
    rects3 = ax.bar(x + 0.5*width, df['Data Trust (Sens)'], width, label='Data Sensitivity', color='#2ca02c')
    rects4 = ax.bar(x + 1.5*width, df['App Risk Posture'], width, label='App Risk', color='#d62728')
    
    # Add predicted outcomes as text annotations
    for i, decision in enumerate(df['Decision']):
        ax.text(i, 1.1, decision, ha='center', fontweight='bold', fontsize=9, color='black')

    ax.set_ylabel('Trust Score (0-1)')
    ax.set_title('Trust Scores by Scenario (4 Domains)')
    ax.set_xticks(x)
    ax.set_xticklabels(df['Scenario'], rotation=15)
    ax.set_ylim(0, 1.25)
    ax.legend(loc='upper right', ncol=4)
    
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('scenario_trust_analysis.png', bbox_inches='tight', dpi=300)
    print("Saved scenario_trust_analysis.png")

if __name__ == "__main__":
    save_table_image()
    save_graphs()
