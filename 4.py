import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

display(df.head())
df.info()
print(df.isnull().sum())

df_scaled = pd.DataFrame(
    StandardScaler().fit_transform(df), columns=df.columns
)
display(df_scaled.head())

inertia, scores = [], []

for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init='auto').fit(df_scaled)
    inertia.append(km.inertia_)
    if k >= 2:
        scores.append(silhouette_score(df_scaled, km.labels_))

plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.xticks(range(1, 11))
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(range(2, 11), scores, marker='o')
plt.title('Silhouette Score Method')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Silhouette Score')
plt.xticks(range(2, 11))
plt.grid()
plt.show()

km = KMeans(n_clusters=3, random_state=42, n_init='auto').fit(df_scaled)
df['cluster_label'] = km.labels_

display(df.head())
display(df['cluster_label'].value_counts())

print("Mean of each feature for each cluster:")
print(df.groupby('cluster_label').mean())

plt.figure(figsize=(10, 6))
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=df['cluster_label'], cmap='viridis')
plt.title('Cluster Visualization based on Sepal Length and Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.colorbar(label='Cluster Label')
plt.grid()
plt.show()
