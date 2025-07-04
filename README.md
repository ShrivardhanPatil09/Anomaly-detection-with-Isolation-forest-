# Anomaly Detection using Isolation Forest and Time Series Analysis

## Overview
This project explains two widely used techniques for detecting anomalies in datasets:

- Isolation Forest: Used for detecting outliers in structured, tabular data.
- Time Series Analysis: Used for identifying pattern breaks in time-based data.

## Isolation Forest

### What is it
Isolation Forest works by isolating data points. It splits features randomly and identifies points that get isolated quickly as potential anomalies.

### Best For
- Fraud detection such as unusual transactions
- Analyzing server logs
- Detecting outliers in tabular datasets

### How It Works
- Randomly selects features and values to split the dataset
- Points that require fewer splits to isolate are likely anomalies

### Example
Among one thousand transactions ranging from 500 to 5000, one transaction of 1000000 will be detected as an anomaly.

## Time Series Analysis

### What is it
Time Series Analysis looks at data that changes over time and identifies any values that deviate from normal patterns or trends.

### Best For
- Monitoring environmental data like temperature
- Website traffic or stock market changes
- Detecting sudden increases or drops over time

### How It Works
- Uses techniques like rolling mean or seasonal decomposition
- Flags data points that do not match expected time-based behavior

### Example
A spike from 500 to 5000 visitors in one day is detected as an anomaly in a website's daily traffic.

## Comparison Table

| Feature               | Isolation Forest         | Time Series Analysis       |
|----------------------|--------------------------|----------------------------|
| Data Type            | Tabular data             | Time-based data            |
| Detects              | Outliers                 | Pattern changes over time  |
| Requires Time Column | No                       | Yes                        |
| Ease of Use          | Simple                   | Requires more processing   |

## Getting Started

### Requirements
- Python 3
- pandas
- scikit-learn
- statsmodels (for time series models)

### Run
To run the examples:

