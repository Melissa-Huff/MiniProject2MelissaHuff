# INF601 - Advanced Programming in Python
# Melissa Huff
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists('charts'):
    os.makedirs('charts')

churn_analysis = pd.read_csv("Telco-Customer-Churn.csv")

tech_support_churn = churn_analysis.groupby('TechSupport')['Churn'].value_counts(normalize=True).unstack() * 100

tech_support_churn.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Churn Rate by Tech Support')
plt.xlabel('Tech Support')
plt.ylabel('Churn Rate (%)')
plt.xticks(rotation=0)
plt.legend(title='Churn', loc='upper right')
plt.savefig('charts/churn_rate_by_tech_support.png')
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
plt.savefig('charts/churn_count_by_gender.png')
plt.show()



churned_customers = churn_analysis[churn_analysis['Churn'] == 'Yes']


plt.scatter(churned_customers['MonthlyCharges'], churned_customers['TotalCharges'])
plt.xlabel('Monthly Charges')
plt.ylabel('Total Charges')
plt.title('Monthly Charges vs Total Charges of Churned Customers')
plt.savefig('charts/monthly_vs_total_charges.png')
plt.show()




specified_payment_methods = ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
filtered_data = churn_analysis[churn_analysis['PaymentMethod'].isin(specified_payment_methods)]


payment_method_counts = filtered_data['PaymentMethod'].value_counts()

colors = ['skyblue', 'orange', 'green', 'red']


plt.bar(payment_method_counts.index, payment_method_counts.values, color=colors)
plt.xlabel('Payment Method')
plt.ylabel('Number of Customers')
plt.title('Number of Customers by Payment Method')
plt.xticks(rotation=45, ha='right')
plt.savefig('charts/num_customers_by_payment_method.png')
plt.show()



billing_counts = churn_analysis.groupby('PaperlessBilling')['customerID'].nunique()


plt.figure(figsize=(6, 6))
plt.pie(billing_counts, labels=billing_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen'])
plt.title('CustomerID Distribution by PaperlessBilling')
plt.axis('equal')
plt.savefig('charts/customerid_distribution_by_paperlessbilling.png')
plt.show()