# INF601 - Advanced Programming in Python
# Melissa Huff
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt

churn_analysis = pd.read_csv("Telco-Customer-Churn.csv")

tech_support_churn = churn_analysis.groupby('TechSupport')['Churn'].value_counts(normalize=True).unstack() * 100

tech_support_churn.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Churn Rate by Tech Support')
plt.xlabel('Tech Support')
plt.ylabel('Churn Rate (%)')
plt.xticks(rotation=0)
plt.legend(title='Churn', loc='upper right')
plt.show()

