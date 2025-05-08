import datetime as dt

snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)
rfm = df.groupby("CustomerID").agg(
    {
        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
        "InvoiceNo": "nunique",
        "TotalPrice": "sum",
    }
)
rfm.columns = ["Recency", "Frequency", "Monetary"]

# KMeans Clustering
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

kmeans = KMeans(n_clusters=4, random_state=42)
rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

sns.scatterplot(data=rfm, x="Recency", y="Monetary", hue="Cluster")
plt.title("Customer Segments")
plt.show()
