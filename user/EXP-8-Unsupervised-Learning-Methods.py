import matplotlib.pyplot as plt # type: ignore
from sklearn.cluster import KMeans


x = [1,2,2,1,8,9,8,9]
y = [1,2,1,2,8,9,9,8]

plt.scatter(x,y)
plt.show()


data = list(zip(x,y))
inertias = []

for i in range(1,8):
  kmeans = KMeans(n_clusters=i)
  kmeans.fit(data)
  inertias.append(kmeans.inertia_)

plt.plot(range(1,8),inertias,marker="o")
plt.show()


kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
plt.scatter(x,y,c=kmeans.labels_)
plt.show()
