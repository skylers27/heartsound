#fuzzy clustering

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']

# Define five cluster centers
centers = [[4, 2],
           [1, 7],
           [5, 6],
           [3, 4],
           [6, 3]]

# Define five cluster sigmas in x and y, respectively
sigmas = [[0.8, 0.3],
          [0.3, 0.5],
          [1.1, 0.7],
          [0.5, 0.6],
          [0.2, 0.1]]

# Generate test data

#early systolic

X1_0 = np.random.normal(loc = 0,scale = 0, size = 50) #s=0, d=1

X1_1 = np.random.normal(loc = 50,scale = 0, size = 50) #onset time (ms)

X1_2 = np.random.normal(loc = 204,scale = 35, size = 50) #duration (ms)

X1_3 = np.random.normal(loc = 354,scale = 7, size = 50) #heart sound duration (ms)

X1_4 = np.random.normal(loc = 388,scale = 8.5, size = 50) #pitch (Hz)



y1 = [0] * 50



#holo systolic

X2_0 = np.random.normal(loc = 0,scale = 0, size = 50) #s=0, d=1

X2_1 = np.random.normal(loc = 50,scale = 0, size =  50) #onset time (ms)

X2_2 = np.random.normal(loc = 200,scale = 84, size = 50) #duration (ms)

X2_3 = np.random.normal(loc = 326,scale = 36, size = 50) #heart sound duration (ms)

X2_4 = np.random.normal(loc = 331,scale = 76, size = 50) #pitch (Hz)



y2 = [1] * 50



#mid systolic

X3_0 = np.random.normal(loc = 0,scale = 0, size = 50) #s=0, d=1

X3_1 = np.random.normal(loc = 129,scale = 46, size = 50) #onset time (ms)

X3_2 = np.random.normal(loc = 62,scale = 50, size = 50) #duration (ms)

X3_3 = np.random.normal(loc = 360,scale = 28, size = 50) #heart sound duration (ms)

X3_4 = np.random.normal(loc = 131,scale = 32, size = 50) #pitch (Hz)



y3 = [2] * 50



#late systolic

X4_0 = np.random.normal(loc = 0,scale = 0, size = 50) #s=0, d=1

X4_1 = np.random.normal(loc = 183,scale = 28, size = 50) #onset time (ms)

X4_2 = np.random.normal(loc = 60,scale = 38, size = 50) #duration (ms)

X4_3 = np.random.normal(loc = 345,scale = 24, size = 50) #heart sound duration (ms)

X4_4 = np.random.normal(loc = 260,scale = 106, size = 50) #pitch (Hz)



y4 = [3] * 50



#early diastolic

X5_0 = np.random.normal(loc = 1,scale = 0, size = 50) #s=0, d=1

X5_1 = np.random.normal(loc = 50,scale = 0, size = 50) #onset time (ms)

X5_2 = np.random.normal(loc = 386,scale = 5, size = 50) #duration (ms)

X5_3 = np.random.normal(loc = 676,scale = 5, size = 50) #heart sound duration (ms)

X5_4 = np.random.normal(loc = 125,scale = 1, size = 50) #pitch (Hz)



y5 = [4] * 50


X = np.zeros((250,6))



X_0 = np.append(X1_0, X2_0)

X_0 = np.append(X_0, X3_0)

X_0 = np.append(X_0, X4_0)

X_0 = np.append(X_0, X5_0)



X_1 = np.append(X1_1, X2_1)

X_1 = np.append(X_1, X3_1)

X_1 = np.append(X_1, X4_1)

X_1 = np.append(X_1, X5_1)



X_2 = np.append(X1_2, X2_2)

X_2 = np.append(X_2, X3_2)

X_2 = np.append(X_2, X4_2)

X_2 = np.append(X_2, X5_2)



X_3 = np.append(X1_3, X2_3)

X_3 = np.append(X_3, X3_3)

X_3 = np.append(X_3, X4_3)

X_3 = np.append(X_3, X5_3)



X_4 = np.append(X1_4, X2_4)

X_4 = np.append(X_4, X3_4)

X_4 = np.append(X_4, X4_4)

X_4 = np.append(X_4, X5_4)

#normalize
X_0 = X_0/max(X_0)

X_1 = X_1/max(X_1)

X_2 = X_2/max(X_2)

X_3 = X_3/max(X_3)

X_4 = X_4/max(X_4)


X[:, 0] = X_0

X[:, 1] = X_1

X[:, 2] = X_2

X[:, 3] = X_3

X[:, 4] = X_4 



y = np.append(y1,y2)

y = np.append(y,y3)

y = np.append(y,y4)

y = np.append(y,y5)



#randomize data

X[:,5] = y

np.random.shuffle(X[:])

# onset time and duration 
xpts = X[:,1]
ypts = X[:,2]
labels = X[:,5]

# Visualize the test data
fig0, ax0 = plt.subplots()
for label in range(5):
    ax0.plot(xpts[labels == label], ypts[labels == label], '.',
             color=colors[label])
ax0.set_title('Test data: 250 points x5 clusters.')
plt.show()

# Set up the loop and plot
fig1, axes1 = plt.subplots(3, 3, figsize=(8, 8))
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
