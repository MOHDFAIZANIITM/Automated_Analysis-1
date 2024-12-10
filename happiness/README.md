# Data Analysis Summary

## Overview

This analysis aims to explore well-being metrics across various countries from 2005 to 2023. The dataset contains several features related to life satisfaction, economic conditions, social support, and perceptions of corruption among others.

## Data Summary

### Columns and Types

The dataset consists of the following columns:
- **Country name**: Country identifier (object)
- **year**: Year of observation (int64)
- **Life Ladder**: Index measuring life satisfaction (float64)
- **Log GDP per capita**: Economic productivity (float64)
- **Social support**: Measure of social connections (float64)
- **Healthy life expectancy at birth**: Average healthy years expected at birth (float64)
- **Freedom to make life choices**: Personal freedom index (float64)
- **Generosity**: Measure of charitable contributions (float64)
- **Perceptions of corruption**: Level of perceived corruption (float64)
- **Positive affect**: Measure of positive emotions (float64)
- **Negative affect**: Measure of negative emotions (float64)

### Missing Values
The dataset has several missing values that need to be addressed:
- Log GDP per capita: 28 missing
- Social support: 13 missing
- Healthy life expectancy at birth: 63 missing
- Freedom to make life choices: 36 missing
- Generosity: 81 missing
- Perceptions of corruption: 125 missing
- Positive affect: 24 missing
- Negative affect: 16 missing

### Summary Statistics
Here are some key statistics from the dataset:

- **Years Covered**: The average year of observation is approximately **2014.76**, with data ranging from **2005 to 2023**.
- **Life Ladder**: The average score is **5.48**, with a minimum of **1.28** and a maximum of **8.02**.
- **Log GDP per capita**: The average is **9.40** (around $12,116), indicating variations in economic conditions.
- **Healthy Life Expectancy**: On average, it stands at **63.40 years**, with a significant standard deviation indicating variability among countries.

## Correlation Insights

### Correlation Matrix
The correlation between features reveals interesting insights:

- **Life Ladder** has a strong positive correlation with:
  - **Log GDP per capita**: **0.78**
  - **Social support**: **0.72**
  - **Healthy life expectancy**: **0.72**
  - **Freedom to make life choices**: **0.54**
  
- **Perceptions of corruption** is negatively correlated with:
  - **Life Ladder**: **-0.43**
  - **Social support**: **-0.22**
  - **Healthy life expectancy**: **-0.30**

- **Positive affect** has moderate positive correlation with:
  - **Life Ladder**: **0.51**
  - **Social support**: **0.42**

- Concerns around **Negative affect** generally correlate with lower life satisfaction (Life Ladder): **-0.35**.

### Key Insights
1. **Economic Factors Matter**: There is a clear linkage between economic metrics (like GDP per capita) and happiness (Life Ladder).
2. **Social Connections**: High levels of social support contribute significantly to perceived well-being.
3. **Corruption's Impact**: Countries with higher perceptions of corruption tend to have lower life satisfaction, highlighting the importance of governance.
4. **Emotional Well-being**: Positive affect correlates positively with life satisfaction, while negative affect detracts from it.

## Visualizations

### 1. Life Ladder vs. Log GDP per Capita
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Sample code, assuming you have the dataset in a variable called df
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Log GDP per capita', y='Life Ladder', hue='Country name', alpha=0.7)
plt.title('Life Ladder vs. Log GDP per Capita')
plt.xlabel('Log GDP per Capita')
plt.ylabel('Life Ladder')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
```

### 2. Correlation Heatmap
```python
plt.figure(figsize=(12, 8))
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Heatmap')
plt.show()
```

### 3. Yearly Trends in Life Ladder Over Time
```python
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='year', y='Life Ladder', ci=None)
plt.title('Yearly Trends in Life Ladder')
plt.xlabel('Year')
plt.ylabel('Life Ladder')
plt.show()
```

## Conclusion
The analysis highlights the significant relationships between various well-being indicators and the factors that influence them. The correlation insights indicate that economic prosperity and social support play pivotal roles in enhancing quality of life across countries. Future efforts should focus on addressing the missing values and potentially leveraging machine learning techniques to predict life satisfaction based on available metrics.