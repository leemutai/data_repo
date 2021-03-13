import pandas as pd
data = pd.read_csv('AirlinesCluster.csv')
# print(data.head(10))
subset= data[['FlightMiles','FlightTrans' ,'DaysSinceEnroll']]
# print(subset)
array= subset.values
# print(array)
X = array[:,0:3]
# print(X)

#fitting the K-Means model
from sklearn.cluster import KMeans
model = KMeans(n_clusters=5)
model.fit(X)
print(model)
centronoids =model.cluster_centers_
print('Centroids: ',centronoids)
cluster = pd.DataFrame(centronoids,
                       columns=['FlightMiles','FlightTrans' ,
                                            'DaysSinceEnroll'])
print('Printing clusters')
# print(cluster)

#plotting our clusters
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# fig, ax = plt.subplots()
fig=plt.figure()
ax= Axes3D(fig)
ax.scatter(X[:,0],X[:,1],X[:,2],c=model.labels_.astype(float))
ax.scatter(centronoids[:,0],centronoids[:,1],centronoids[:,2],
           marker='.', c='red', s=100)
plt.show()