import matplotlib.pyplot as plt
import seaborn as sns

# Monthly sales trend
df["InvoiceMonth"] = df["InvoiceDate"].dt.to_period("M")
monthly_sales = df.groupby("InvoiceMonth")["TotalPrice"].sum()

monthly_sales.plot(kind="line", title="Monthly Revenue")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# Top countries
top_countries = (
    df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False).head(10)
)
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 10 Countries by Revenue")
plt.show()
