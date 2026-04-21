import matplotlib
matplotlib.use('TkAgg')   # 🔥 Fix for graph display

import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("whitegrid")

# Create plots folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLOTS_DIR = os.path.join(BASE_DIR, "outputs", "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)


def plot_unemployment_trend(df):
    if 'Date' not in df.columns:
        print("No Date column found")
        return

    plt.figure(figsize=(10,5))
    sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)')

    plt.title("Unemployment Trend Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()

    file_path = os.path.join(PLOTS_DIR, "trend.png")
    plt.savefig(file_path)
    plt.show()   # ✅ SHOW GRAPH
    plt.close()

    print("Saved:", file_path)


def plot_by_region(df):
    if 'Region' not in df.columns:
        print("No Region column found")
        return

    plt.figure(figsize=(10,5))
    sns.barplot(data=df, x='Region', y='Estimated Unemployment Rate (%)')

    plt.title("Unemployment by Region")
    plt.xticks(rotation=45)
    plt.tight_layout()

    file_path = os.path.join(PLOTS_DIR, "region.png")
    plt.savefig(file_path)
    plt.show()
    plt.close()

    print("Saved:", file_path)


def plot_distribution(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df['Estimated Unemployment Rate (%)'], bins=20, kde=True)

    plt.title("Distribution of Unemployment Rate")
    plt.tight_layout()

    file_path = os.path.join(PLOTS_DIR, "distribution.png")
    plt.savefig(file_path)
    plt.show()
    plt.close()

    print("Saved:", file_path)