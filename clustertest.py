# coding: utf-8

# *Python Machine Learning 2nd Edition* by [Sebastian Raschka](https://sebastianraschka.com), Packt Publishing Ltd. 2017
# 
# Code Repository: https://github.com/rasbt/python-machine-learning-book-2nd-edition
# 
# Code License: [MIT License](https://github.com/rasbt/python-machine-learning-book-2nd-edition/blob/master/LICENSE.txt)

# # Python Machine Learning - Code Examples

# # Chapter 11 - Working with Unlabeled Data – Clustering Analysis

# Note that the optional watermark extension is a small IPython notebook plugin that I developed to make the code reproducible. You can just skip the following line(s).

# In[1]:




# *The use of `watermark` is optional. You can install this IPython extension via "`pip install watermark`". For more information, please see: https://github.com/rasbt/watermark.*


# ### Overview

# - [Grouping objects by similarity using k-means](#Grouping-objects-by-similarity-using-k-means)
#   - [K-means clustering using scikit-learn](#K-means-clustering-using-scikit-learn)
#   - [A smarter way of placing the initial cluster centroids using k-means++](#A-smarter-way-of-placing-the-initial-cluster-centroids-using-k-means++)
#   - [Hard versus soft clustering](#Hard-versus-soft-clustering)
#   - [Using the elbow method to find the optimal number of clusters](#Using-the-elbow-method-to-find-the-optimal-number-of-clusters)
#   - [Quantifying the quality of clustering via silhouette plots](#Quantifying-the-quality-of-clustering-via-silhouette-plots)
# - [Organizing clusters as a hierarchical tree](#Organizing-clusters-as-a-hierarchical-tree)
#   - [Grouping clusters in bottom-up fashion](#Grouping-clusters-in-bottom-up-fashion)
#   - [Performing hierarchical clustering on a distance matrix](#Performing-hierarchical-clustering-on-a-distance-matrix)
#   - [Attaching dendrograms to a heat map](#Attaching-dendrograms-to-a-heat-map)
#   - [Applying agglomerative clustering via scikit-learn](#Applying-agglomerative-clustering-via-scikit-learn)
# - [Locating regions of high density via DBSCAN](#Locating-regions-of-high-density-via-DBSCAN)
# - [Summary](#Summary)


# In[2]:
import numpy as np
from IPython.display import Image

# # Grouping objects by similarity using k-means

# ## K-means clustering using scikit-learn

# In[3]:


from sklearn.datasets import make_blobs
'''
X, y = make_blobs(n_samples=50, 
                  n_features=2, 
                  centers=3, 
                  cluster_std=0.5, 
                  shuffle=True, 
                  random_state=0)
'''

#early systolic
X1_0 = np.random.normal(loc = 204,scale = 35, size = 50) #duration
X1_1 = np.random.normal(loc = 388,scale = 8.5, size = 50) #pitch

y1 = [0] * 50

#mid systolic
X2_0 = np.random.normal(loc = 62,scale = 50, size = 50) #duration
X2_1 = np.random.normal(loc = 130,scale = 32, size = 50) #pitch

y2 = [1] * 50

X = np.zeros((100,2))
X_0 = np.append(X1_0, X2_0)
X_1 = np.append(X1_1, X2_1)

X[:, 0] = X_0
X[:, 1] = X_1

y = np.append(y1,y2)
print(X)
print(y)

#print(X1)
#print(y)


# In[4]:


import matplotlib.pyplot as plt

plt.scatter(X[:, 0], X[:, 1], 
            c='white', marker='o', edgecolor='black', s=50)

plt.xlabel('Duration')
plt.ylabel('Pitch')

plt.grid()
plt.tight_layout()
#plt.savefig('images/11_01.png', dpi=300)
plt.show()


# In[5]:


from sklearn.cluster import KMeans

km = KMeans(n_clusters=2, 
            init='random', 
            n_init=10, 
            max_iter=300,
            tol=1e-04,
            random_state=0)

y_km = km.fit_predict(X)


# In[6]:


plt.scatter(X[y_km == 0, 0],
            X[y_km == 0, 1],
            s=50, c='lightgreen',
            marker='s', edgecolor='black',
            label='cluster 1')
plt.scatter(X[y_km == 1, 0],
            X[y_km == 1, 1],
            s=50, c='orange',
            marker='o', edgecolor='black',
            label='cluster 2')
plt.scatter(X[y_km == 2, 0],
            X[y_km == 2, 1],
            s=50, c='lightblue',
            marker='v', edgecolor='black',
            label='cluster 3')
plt.scatter(km.cluster_centers_[:, 0],
            km.cluster_centers_[:, 1],
            s=250, marker='*',
            c='red', edgecolor='black',
            label='centroids')
plt.legend(scatterpoints=1)

plt.xlabel('Duration')
plt.ylabel('Pitch')

plt.grid()
plt.tight_layout()
#plt.savefig('images/11_02.png', dpi=300)
plt.show()



# ## A smarter way of placing the initial cluster centroids using k-means++

# ...

# ## Hard versus soft clustering

# ...

# ## Using the elbow method to find the optimal number of clusters 

# In[7]:


print('Distortion: %.2f' % km.inertia_)


# In[8]:


distortions = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, 
                init='k-means++', 
                n_init=10, 
                max_iter=300, 
                random_state=0)
    km.fit(X)
    distortions.append(km.inertia_)
plt.plot(range(1, 11), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.tight_layout()
#plt.savefig('images/11_03.png', dpi=300)
plt.show()



# ## Quantifying the quality of clustering  via silhouette plots

# In[9]:


import numpy as np
from matplotlib import cm
from sklearn.metrics import silhouette_samples

km = KMeans(n_clusters=2, 
            init='k-means++', 
            n_init=10, 
            max_iter=300,
            tol=1e-04,
            random_state=0)
y_km = km.fit_predict(X)

cluster_labels = np.unique(y_km)
n_clusters = cluster_labels.shape[0]
silhouette_vals = silhouette_samples(X, y_km, metric='euclidean')
y_ax_lower, y_ax_upper = 0, 0
yticks = []
for i, c in enumerate(cluster_labels):
    c_silhouette_vals = silhouette_vals[y_km == c]
    c_silhouette_vals.sort()
    y_ax_upper += len(c_silhouette_vals)
    color = cm.jet(float(i) / n_clusters)
    plt.barh(range(y_ax_lower, y_ax_upper), c_silhouette_vals, height=1.0, 
             edgecolor='none', color=color)

    yticks.append((y_ax_lower + y_ax_upper) / 2.)
    y_ax_lower += len(c_silhouette_vals)
    
silhouette_avg = np.mean(silhouette_vals)
plt.axvline(silhouette_avg, color="red", linestyle="--") 

plt.yticks(yticks, cluster_labels + 1)
plt.ylabel('Cluster')
plt.xlabel('Silhouette coefficient')

plt.tight_layout()
#plt.savefig('images/11_04.png', dpi=300)
plt.show()









