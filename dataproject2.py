import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = r"C:\Users\ritik rana\Downloads\Olympic Athletes.xlsx"

try:
    df = pd.read_excel(file_path)
    print("File loaded successfully!")
except Exception as e:
    print(f"Error loading the Excel file: {e}")

# Define regions for grouping
regions = {
    'Asia': ['China', 'Japan', 'India', 'South Korea', 'Indonesia', 'Thailand', 'Malaysia', 'Philippines', 'Vietnam'],
    'Africa': ['Kenya', 'South Africa', 'Ethiopia', 'Nigeria', 'Egypt', 'Ghana', 'Tanzania', 'Morocco'],
    'Europe': ['Germany', 'France', 'Italy', 'United Kingdom', 'Russia', 'Spain', 'Netherlands', 'Sweden'],
    'North America': ['USA', 'Canada', 'Mexico', 'Cuba'],
    'South America': ['Brazil', 'Argentina', 'Chile', 'Colombia'],
    'Oceania': ['Australia', 'New Zealand']
}

# Plot 1: Pie Chart for Total Medals by Region
region_medals = {}
for region, countries in regions.items():
    total_medals = df[df['Country'].isin(countries)]['Total Medals'].sum()
    region_medals[region] = total_medals

plt.figure(figsize=(8, 8))
plt.pie(region_medals.values(), labels=region_medals.keys(), autopct='%1.1f%%', colors=sns.color_palette("Set3"))
plt.title('Percentage of Total Medals by Region')
plt.show()

# Plot 2: Pie Chart for Gold Medals by Region
region_gold_medals = {}
for region, countries in regions.items():
    gold_medals = df[df['Country'].isin(countries)]['Gold Medals'].sum()
    region_gold_medals[region] = gold_medals

plt.figure(figsize=(8, 8))
plt.pie(region_gold_medals.values(), labels=region_gold_medals.keys(), autopct='%1.1f%%', colors=sns.color_palette("Set2"))
plt.title('Percentage of Gold Medals by Region')
plt.show()

# Plot 3: Histogram with Density Plot for Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=15, kde=True, color='coral')
plt.title('Age Distribution of Athletes with Density Plot')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Plot 4: Heatmap of Correlation between Medals and Age
plt.figure(figsize=(8, 6))
corr_matrix = df[['Age', 'Total Medals', 'Gold Medals', 'Silver Medals', 'Bronze Medals']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# Plot 5: Bar Plot for Total Medals by Region
plt.figure(figsize=(10, 6))
sns.barplot(x=list(region_medals.keys()), y=list(region_medals.values()), palette='Blues_d')
plt.title('Total Medals by Region')
plt.xlabel('Region')
plt.ylabel('Total Medals')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 6: Bar Plot for Gold Medals by Region
plt.figure(figsize=(10, 6))
sns.barplot(x=list(region_gold_medals.keys()), y=list(region_gold_medals.values()), palette='Oranges')
plt.title('Gold Medals by Region')
plt.xlabel('Region')
plt.ylabel('Gold Medals')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 7: Scatter Plot for Age vs Total Medals
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Total Medals', data=df, hue='Country', palette='viridis', s=100, alpha=0.6)
plt.title('Scatter Plot of Age vs Total Medals by Country')
plt.xlabel('Age')
plt.ylabel('Total Medals')
plt.tight_layout()
plt.show()

# Plot 8: Bar Plot for Bronze Medals by Region
region_bronze_medals = {}
for region, countries in regions.items():
    bronze_medals = df[df['Country'].isin(countries)]['Bronze Medals'].sum()
    region_bronze_medals[region] = bronze_medals

plt.figure(figsize=(10, 6))
sns.barplot(x=list(region_bronze_medals.keys()), y=list(region_bronze_medals.values()), palette='Purples')
plt.title('Bronze Medals by Region')
plt.xlabel('Region')
plt.ylabel('Bronze Medals')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
