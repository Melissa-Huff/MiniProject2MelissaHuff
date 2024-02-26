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


gender_churn_counts = churn_analysis[churn_analysis['Churn'] == 'Yes']['gender'].value_counts()

categories = ["Male", "Female"]

values = [gender_churn_counts.get("Male", 0), gender_churn_counts.get("Female", 0)]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(categories, values)
plt.xlabel('Gender')
plt.ylabel('Churn Count')
plt.title('Churn Count by Gender')

plt.show()



churned_customers = churn_analysis[churn_analysis['Churn'] == 'Yes']


plt.scatter(churned_customers['MonthlyCharges'], churned_customers['TotalCharges'])
plt.xlabel('Monthly Charges')
plt.ylabel('Total Charges')
plt.title('Monthly Charges vs Total Charges of Churned Customers')
plt.show()