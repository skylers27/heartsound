#fuzzy clustering

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']

# Define three cluster centers
centers = [[4, 2],
           [1, 7],
           [5, 6]]

# Define three cluster sigmas in x and y, respectively
sigmas = [[0.8, 0.3],
          [0.3, 0.5],
          [1.1, 0.7]]

# Insert his test data instead !!!!
# Then our data 

# Collect Test Data 
with open("testFun.dat") as textFile:
    y = [line.split() for line in textFile]

y = np.array(y)
X = np.zeros(shape=(200,2))

# stores test data as number in array X (converts from strings)
for i in range(0,len(y)): # num rows 
  for j in range(0,len(y[0])): # num columns 
    X[i,j] = float(y[i,j])
   
xpts = np.zeros(len(y)) 
ypts = np.zeros(len(y)) 
labels = np.zeros(len(y)) # no labels 


# xpts = x[all rows][0]
for i in range (0, len(y)):
  xpts[i] = X[i][0]

# ypts = x[all rows][1]
for i in range (0, len(y)):
  ypts[i] = X[i][1]

# Visualize the test data
fig0, ax0 = plt.subplots()
for label in range(2): # need 2 different kinds of labels, only have 1 cuz theyre not labeled...
    ax0.plot(xpts[labels == label], ypts[labels == label], '.',
             color=colors[label])
ax0.set_title('Test data: 200 points x2 clusters.')
plt.show()

# Set up the loop and plot
fig1, axes1 = plt.subplots(2, 1, figsize=(8, 8)) #number of figures
alldata = np.vstack((xpts, ypts))
fpcs = []

for ncenters, ax in enumerate(axes1.reshape(-1), 2):
    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
        alldata, ncenters, 2, error=0.005, maxiter=1000, init=None)
    print("Centers = ", str(ncenters), "\n") # u0 is the array of the memberiship functions 
    for i in range (len(y)): # columns
      print ("Data point: ",xpts[i], ",", ypts[i]) #data point
      print("Membership: ")
      for j in range(ncenters): #number of clusters
        print("Cluster: ", j, "\n", u0[j][i]) #membership for cluster
      print()

    # Store fpc values for later
    fpcs.append(fpc)

    # Plot assigned clusters, for each data point in training set
    cluster_membership = np.argmax(u, axis=0)
    for j in range(ncenters):
        ax.plot(xpts[cluster_membership == j],
                ypts[cluster_membership == j], '.', color=colors[j])

    # Mark the center of each fuzzy cluster
    for pt in cntr:
        ax.plot(pt[0], pt[1], 'rs')

    ax.set_title('Centers = {0}; FPC = {1:.2f}'.format(ncenters, fpc))
    ax.axis('off')

fig1.tight_layout()
plt.show()
