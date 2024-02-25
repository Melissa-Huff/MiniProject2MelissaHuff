import pandas as pd

churn_analysis = pd.read_csv("Telco-Customer-Churn.csv", index_col=0, parse_dates=True)

print(churn_analysis.head())