import pandas as pd

df = pd.read_excel("C:\Users\USER\OneDrive\Desktop\program\E-Commerce Sales & Customer Segmentation Analysis\Online Retail.xlsx")
df.dropna(subset=["CustomerID"], inplace=True)
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]  # remove cancelled
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

# Create new column for total sale
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df.to_csv("data/cleaned_data.csv", index=False)
