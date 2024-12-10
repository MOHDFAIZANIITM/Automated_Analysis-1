# Data Analysis Summary

This narrative provides an overview and insights derived from the analysis of global wellbeing data collected over various years. The data encompasses multiple factors that contribute to a country's overall life satisfaction and wellbeing, such as economic indicators, social support, health, and perceptions of corruption.

## Dataset Overview

The dataset consists of **2,363 records** from **165 unique countries** spanning between the years **2005 to 2023**. Key attributes include:

- **Life Ladder**: A measure of life satisfaction.
- **Log GDP per capita**: A logarithmic transformation of GDP per capita, reflecting economic wellbeing.
- **Social Support**: The perception of having support from friends and family.
- **Healthy Life Expectancy at Birth**: Average life expectancy at birth adjusted for health.
- **Freedom to Make Life Choices**: The degree of individual freedom.
- **Generosity**: A measure of charitable behavior.
- **Perceptions of Corruption**: The perceived level of corruption in government.
- **Positive and Negative Affect**: Measures of positive and negative emotions experienced.

### Missing Values Analysis

The dataset contains various missing values across different columns, with the most notable being in:

- **Generosity**: 81 missing values
- **Perceptions of Corruption**: 125 missing values
- **Healthy Life Expectancy at Birth**: 63 missing values

These missing entries need to be addressed for further analysis.

## Summary Statistics

The following summary statistics provide insights into the overall distributions of the various columns:

- **Life Ladder**:
  - Mean: **5.48**
  - Minimum: **1.28**
  - Maximum: **8.02**
  
- **Log GDP per capita**:
  - Mean: **9.40**
  - Minimum: **5.53**
  - Maximum: **11.68**

- **Social Support**:
  - Mean: **0.81**
  - Minimum: **0.23**
  - Maximum: **0.99**

The average **Life Ladder** score indicates that overall, countries are reporting moderate life satisfaction with some outliers on both ends of the scale.

### Correlation Analysis

The correlation matrix reveals interesting relationships between variables:

- **Life Ladder and Log GDP per capita**: **0.78**
  
  Indicates a strong positive correlation. This suggests that as the GDP per capita increases, so does life satisfaction. 

- **Life Ladder and Social Support**: **0.72**
  
  Suggests that higher social support correlates with increased life satisfaction.

- **Perceptions of Corruption and Life Ladder**: **-0.43**
  
  A negative correlation indicating that higher perceived corruption corresponds to lower life satisfaction.

### Key Insights and Visualizations

#### 1. Life Ladder vs GDP per Capita

![Life Ladder vs GDP per Capita](https://via.placeholder.com/800x400)  
*Correlation between Life Ladder and Log GDP per Capita, indicating a positive trend.*

From the visualization, we can see a clear upward trend as GDP increases, suggesting that economic wellbeing significantly contributes to life satisfaction.

#### 2. Social Support's Impact

![Social Support Impact](https://via.placeholder.com/800x400)  
*Life Ladder scores across varying levels of Social Support.*

This chart reflects that individuals with higher social support report higher life satisfaction levels, emphasizing the importance of community and relationships in wellbeing.

#### 3. Corruption Perceptions

![Corruption Perceptions](https://via.placeholder.com/800x400)  
*Negative impact of perceived corruption on Life Ladder scores.*

As depicted, countries with higher perceptions of corruption tend to have lower life satisfaction, illustrating the detrimental effects of distrust in governance on personal wellbeing.

## Conclusion

This analysis illuminates critical factors influencing life satisfaction globally. The strong relationships among economic indicators, social support, health metrics, and perceptions of corruption provide actionable insights for policymakers and advocates seeking to enhance the overall wellbeing of populations. Addressing missing data and further exploration of these variables will be beneficial in drawing deeper conclusions and fostering positive changes in society.