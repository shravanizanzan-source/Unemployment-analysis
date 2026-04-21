import pandas as pd
from cleaning import load_and_clean_data
from visualization import (
    plot_unemployment_trend,
    plot_by_region,
    plot_distribution
)

# Load dataset
df = load_and_clean_data("unemployment.csv")

print("\n✅ DATA LOADED SUCCESSFULLY\n")

# Basic info
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())

# Summary stats
print("\n📊 Summary Statistics:\n", df.describe())

# Mean unemployment
mean_rate = df['Estimated Unemployment Rate (%)'].mean()
print("\n📌 Average Unemployment Rate:", round(mean_rate, 2))

# Add Year column if Date exists
if 'Date' in df.columns:
    df['Year'] = df['Date'].dt.year

    # COVID Impact (2020)
    covid_data = df[df['Year'] == 2020]

    if not covid_data.empty:
        covid_avg = covid_data['Estimated Unemployment Rate (%)'].mean()
        print("\n🦠 COVID 2020 Avg Unemployment:", round(covid_avg, 2))

# Seasonal trend (monthly)
if 'Date' in df.columns:
    df['Month'] = df['Date'].dt.month
    monthly_avg = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()
    print("\n📅 Monthly Average:\n", monthly_avg)

# Visualization
plot_unemployment_trend(df)
plot_by_region(df)
plot_distribution(df)

# Save report
with open("../outputs/report.txt", "w") as f:
    f.write("UNEMPLOYMENT ANALYSIS REPORT\n\n")
    f.write(f"Average Unemployment Rate: {mean_rate:.2f}\n")

    if 'Date' in df.columns and not covid_data.empty:
        f.write(f"COVID 2020 Average: {covid_avg:.2f}\n")

print("\n✅ Analysis Complete! Check outputs folder.")

import os

print("Current Working Directory:", os.getcwd())
