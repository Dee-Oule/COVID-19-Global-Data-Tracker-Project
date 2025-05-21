#Data Collection, Loading and Exploration
# Step 1: Import necessary libraries
from networkx import project
import pandas as pd

# Step 2: Load the COVID-19 dataset
file_path = "owid-covid-data.csv"  # Ensure the file is saved in your working directory
df = pd.read_csv(file_path)

# Step 3: Explore dataset structure
print("Columns in dataset:\n", df.columns)  # View column names
print("\nFirst few rows:\n", df.head())  # Preview first few rows
print("\nMissing values:\n", df.isnull().sum())  # Check for missing values

#Data Cleaning
import pandas as pd

# Load dataset
file_path = "owid-covid-data.csv"
df = pd.read_csv(file_path)

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter for countries of interest
countries = ["Kenya", "USA", "India"]
df_filtered = df[df['location'].isin(countries)]

# Drop rows where critical values (date, total_cases, total_deaths) are missing
df_filtered = df_filtered.dropna(subset=['date', 'total_cases', 'total_deaths'])

# Fill missing numeric values using interpolation
numeric_cols = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations']
df_filtered[numeric_cols] = df_filtered[numeric_cols].interpolate()

# Display cleaned data summary
print("Cleaned Data Preview:\n", df_filtered.head())
print("\nMissing values after cleaning:\n", df_filtered.isnull().sum())


#Exploratory Data Analysis
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load cleaned dataset
file_path = "owid-covid-data.csv"
df = pd.read_csv(file_path)

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter for selected countries
countries = ["Kenya", "USA", "India"]
df_filtered = df[df['location'].isin(countries)]

# Calculate death rate
df_filtered["death_rate"] = df_filtered["total_deaths"] / df_filtered["total_cases"]

# 📌 Line chart: Total cases over time
plt.figure(figsize=(12, 6))
for country in countries:
    subset = df_filtered[df_filtered["location"] == country]
    plt.plot(subset["date"], subset["total_cases"], label=country)

plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.title("COVID-19 Total Cases Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# 📌 Line chart: Total deaths over time
plt.figure(figsize=(12, 6))
for country in countries:
    subset = df_filtered[df_filtered["location"] == country]
    plt.plot(subset["date"], subset["total_deaths"], label=country)

plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.title("COVID-19 Total Deaths Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# 📌 Bar chart: Comparing daily new cases
plt.figure(figsize=(10, 5))
sns.barplot(data=df_filtered, x="location", y="new_cases", ci=None)
plt.xlabel("Country")
plt.ylabel("Average Daily New Cases")
plt.title("Comparison of Daily New Cases Between Countries")
plt.show()

# 📌 (Optional) Heatmap: Correlation Analysis
plt.figure(figsize=(10, 6))
sns.heatmap(df_filtered[["total_cases", "total_deaths", "death_rate"]].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap for COVID-19 Data")
plt.show()


#Visualizing Vaccination Progress
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
file_path = "owid-covid-data.csv"
df = pd.read_csv(file_path)

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter for selected countries
countries = ["Kenya", "USA", "India"]
df_filtered = df[df['location'].isin(countries)]

# 📌 Line Chart: Cumulative vaccinations over time
plt.figure(figsize=(12, 6))
for country in countries:
    subset = df_filtered[df_filtered["location"] == country]
    plt.plot(subset["date"], subset["total_vaccinations"], label=country)

plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.title("Cumulative COVID-19 Vaccinations Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# 📌 Bar Chart: Percentage of vaccinated population (normalized estimate)
df_filtered["vaccination_rate"] = df_filtered["total_vaccinations"] / df_filtered["population"] * 100

plt.figure(figsize=(10, 5))
sns.barplot(data=df_filtered, x="location", y="vaccination_rate", ci=None)
plt.xlabel("Country")
plt.ylabel("Vaccination Rate (%)")
plt.title("Vaccination Coverage Across Selected Countries")
plt.show()

# 📌 Optional Pie Chart: Vaccinated vs. Unvaccinated Population (for latest date)
latest_data = df_filtered[df_filtered['date'] == df_filtered['date'].max()]
for country in countries:
    country_data = latest_data[latest_data["location"] == country]
    vaccinated = country_data["total_vaccinations"].values[0]
    unvaccinated = country_data["population"].values[0] - vaccinated

    plt.figure(figsize=(6, 6))
    plt.pie([vaccinated, unvaccinated], labels=["Vaccinated", "Unvaccinated"], autopct="%1.1f%%", colors=["green", "red"])
    plt.title(f"Vaccination Distribution in {country}")
    plt.show()


#Generate Choropleth map
import pandas as pd
import plotly.express as px

# Load cleaned dataset
file_path = "owid-covid-data.csv"
df = pd.read_csv(file_path)

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Select the latest data available for each country
latest_df = df[df['date'] == df['date'].max()]  # Filter for the latest date

# Select relevant columns
latest_df = latest_df[['iso_code', 'location', 'total_cases', 'total_vaccinations', 'population']]

# Calculate vaccination rate (% of population vaccinated)
latest_df['vaccination_rate'] = (latest_df['total_vaccinations'] / latest_df['population']) * 100

# 📌 Choropleth Map: Total COVID-19 Cases by Country
fig_cases = px.choropleth(latest_df,
                          locations='iso_code',
                          color='total_cases',
                          hover_name='location',
                          color_continuous_scale='Reds',
                          title="Global COVID-19 Case Density")

fig_cases.show()

# 📌 Choropleth Map: Vaccination Rates by Country
fig_vax = px.choropleth(latest_df,
                        locations='iso_code',
                        color='vaccination_rate',
                        hover_name='location',
                        color_continuous_scale='Blues',
                        title="Global COVID-19 Vaccination Rates")

fig_vax.show()


#Jupyter Notebook Content
# 📌 COVID-19 Data Analysis & Insights Report

## 1️⃣ Project Overview
#This project tracks global COVID-19 trends, focusing on total cases, deaths, and vaccinations across selected countries.

## 2️⃣ Key Insights
-# **Vaccination Trends**: The USA led vaccine rollout, while Kenya progressed steadily.
- #**Case Surges**: India had significant waves impacting healthcare systems.
- #**Death Rates**: Fluctuations in different regions indicate severity patterns.

## 3️⃣ Visualizations
#Below are plots showing COVID-19 cases, deaths, vaccination trends, and global case density.


### 🔹 Embed Code & Visualizations
#python
# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Load cleaned dataset
file_path = "owid-covid-data.csv"
df = pd.read_csv(file_path)

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Example visualization: Total cases over time
plt.figure(figsize=(12, 6))
for country in ["Kenya", "USA", "India"]:
    subset = df[df["location"] == country]
    plt.plot(subset["date"], subset["total_cases"], label=country)

plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.title("COVID-19 Total Cases Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.show()
