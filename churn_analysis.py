import pandas as pd

# Load dataset
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())

# Check missing values
print(df.isnull().sum())

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(
    df['TotalCharges'],
    errors='coerce'
)

# Fill missing values
df['TotalCharges'].fillna(
    df['TotalCharges'].median(),
    inplace=True
)

# Create Customer Lifetime Value
df['CLV'] = df['MonthlyCharges'] * df['tenure']

# Save cleaned file
df.to_csv(
    "outputs/clean_telco_churn.csv",
    index=False
)

print("Data cleaned successfully!")

import matplotlib.pyplot as plt

df['Churn'].value_counts().plot(kind='bar')

plt.title("Customer Churn Distribution")

plt.savefig("visuals/test_chart.png")

print("Chart Saved Successfully")

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x='Contract',
    hue='Churn'
)

plt.title("Contract vs Churn")

plt.savefig("visuals/contract_vs_churn.png")

plt.show()

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x='InternetService',
    hue='Churn'
)

plt.title("Internet Service vs Churn")

plt.savefig("visuals/internet_service_vs_churn.png")

plt.show()

plt.figure(figsize=(10,5))

sns.countplot(
    data=df,
    y='PaymentMethod',
    hue='Churn'
)

plt.title("Payment Method vs Churn")

plt.savefig("visuals/payment_method_vs_churn.png")

plt.show()

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x='Churn',
    y='MonthlyCharges'
)

plt.title("Monthly Charges vs Churn")

plt.savefig("visuals/monthly_charges_vs_churn.png")

plt.show()

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x='Churn',
    y='tenure'
)

plt.title("Tenure vs Churn")

plt.savefig("visuals/tenure_vs_churn.png")

plt.show()