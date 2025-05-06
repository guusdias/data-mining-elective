import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

file_path = '/Users/gustavodias/dev/n2-camargo/chatice.csv'
data = pd.read_csv(file_path, encoding='latin1')

features = ['NETPRO  ', 'Q20Age', 'Q21Gender', 'Q22Income', 'Q23FLY', 'Q5TIMESFLOWN', 'Q6LONGUSE']
df = data[features].copy()

df = pd.get_dummies(df, columns=['Q21Gender'], drop_first=True)

features.remove('Q21Gender')
features.extend([col for col in df.columns if col.startswith('Q21Gender_')])

df = df.dropna()

scaler = StandardScaler()
scaled_features = scaler.fit_transform(df)

n_clusters = 4
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

df['Cluster'] = clusters

cluster_sizes = df['Cluster'].value_counts(normalize=True) * 100
unusual_cluster = cluster_sizes.idxmin()
unusual_size = cluster_sizes.min()
unusual_group = df[df['Cluster'] == unusual_cluster]

unusual_profile = unusual_group[features].describe()
print(f"Unusual cluster size: {unusual_size:.2f}% of passengers")
print("\nProfile of unusual cluster:")
print(unusual_profile)