#Machine Learning Heart Murmur Clustering #Alisa Levin and Skyler Szot # Add user input for amount of features and clusters # Test different features to see which are robust and which are sensitive # Try to do something with his code import numpy as npfrom IPython.display import Imagefrom sklearn.datasets import make_blobsimport matplotlib.pyplot as pltfrom sklearn.cluster import KMeansprint("Enter positive floats: ")std1 = float(input("\nEnter onset time standard deviation modifier: "))std2 = float(input("\nEnter duration standard deviation modifier: "))std3 = float(input("\nEnter heart sound duration standard deviation modifier: "))std4 = float(input("\nEnter pitch standard deviation modifier: "))#early systolicX1_0 = np.random.normal(loc = 0,scale = 0, size = 50) #s=0, d=1X1_1 = np.random.normal(loc = 50,scale = 0 * std1, size = 50) #onset time (ms)X1_2 = np.random.normal(loc = 204,scale = 35 * std2, size = 50) #duration (ms)X1_3 = np.random.normal(loc = 354,scale = 7 * std3, size = 50) #heart sound duration (ms)X1_4 = np.random.normal(loc = 388,scale = 8.5 * std4, size = 50) #pitch (Hz)y1 = [0] * 50#holo systolicX2_0 = np.random.normal(loc = 0,scale = 0, size = 50) #s=0, d=1X2_1 = np.random.normal(loc = 50,scale = 0 * std1, size =  50) #onset time (ms)X2_2 = np.random.normal(loc = 200,scale = 84 * std2, size = 50) #duration (ms)X2_3 = np.random.normal(loc = 326,scale = 36 * std3, size = 50) #heart sound duration (ms)X2_4 = np.random.normal(loc = 331,scale = 76 * std4, size = 50) #pitch (Hz)y2 = [1] * 50#mid systolicX3_0 = np.random.normal(loc = 0,scale = 0, size = 50) #s=0, d=1X3_1 = np.random.normal(loc = 129,scale = 46 * std1, size = 50) #onset time (ms)X3_2 = np.random.normal(loc = 62,scale = 50 * std2, size = 50) #duration (ms)X3_3 = np.random.normal(loc = 360,scale = 28 * std3, size = 50) #heart sound duration (ms)X3_4 = np.random.normal(loc = 131,scale = 32 * std4, size = 50) #pitch (Hz)y3 = [2] * 50#late systolicX4_0 = np.random.normal(loc = 0,scale = 0, size = 50) #s=0, d=1X4_1 = np.random.normal(loc = 183,scale = 28 * std1, size = 50) #onset time (ms)X4_2 = np.random.normal(loc = 60,scale = 38 * std2, size = 50) #duration (ms)X4_3 = np.random.normal(loc = 345,scale = 24 * std3, size = 50) #heart sound duration (ms)X4_4 = np.random.normal(loc = 260,scale = 106 * std4, size = 50) #pitch (Hz)y4 = [3] * 50#early diastolicX5_0 = np.random.normal(loc = 1,scale = 0, size = 50) #s=0, d=1X5_1 = np.random.normal(loc = 50,scale = 0 * std1, size = 50) #onset time (ms)X5_2 = np.random.normal(loc = 386,scale = 5 * std2, size = 50) #duration (ms)X5_3 = np.random.normal(loc = 676,scale = 5 * std3, size = 50) #heart sound duration (ms)X5_4 = np.random.normal(loc = 125,scale = 1 * std4, size = 50) #pitch (Hz)y5 = [4] * 50X = np.zeros((250,6))X_0 = np.append(X1_0, X2_0)X_0 = np.append(X_0, X3_0)X_0 = np.append(X_0, X4_0)X_0 = np.append(X_0, X5_0)X_1 = np.append(X1_1, X2_1)X_1 = np.append(X_1, X3_1)X_1 = np.append(X_1, X4_1)X_1 = np.append(X_1, X5_1)X_2 = np.append(X1_2, X2_2)X_2 = np.append(X_2, X3_2)X_2 = np.append(X_2, X4_2)X_2 = np.append(X_2, X5_2)X_3 = np.append(X1_3, X2_3)X_3 = np.append(X_3, X3_3)X_3 = np.append(X_3, X4_3)X_3 = np.append(X_3, X5_3)X_4 = np.append(X1_4, X2_4)X_4 = np.append(X_4, X3_4)X_4 = np.append(X_4, X4_4)X_4 = np.append(X_4, X5_4)#normalizeX_0 = X_0/max(X_0)X_1 = X_1/max(X_1)X_2 = X_2/max(X_2)X_3 = X_3/max(X_3)X_4 = X_4/max(X_4)X[:, 0] = X_0X[:, 1] = X_1X[:, 2] = X_2X[:, 3] = X_3X[:, 4] = X_4	y = np.append(y1,y2)y = np.append(y,y3)y = np.append(y,y4)y = np.append(y,y5)#randomize dataX[:,5] = ynp.random.shuffle(X[:])original = Xoriginaly = X[:,5]features = []#decision treesyst = int(len(X) - sum(X[:,0]))temp = np.zeros((syst,6))j = 0for i in range(0,len(X)):	if X[i,0] == 0:		temp[j] = X[i]		j+=1X = np.array(temp)y = X[:,5]clusters = int(input("\n\tEnter Number of Clusters to be Created (s/d automatically included): "))#print("\nType 1 for Yes and 0 for No")#a = int(input("\n\tInclude Systole/Diastole feature?: "))#if (a == 1):#	features.append(0)b = int(input("\tInclude Onset Time feature?: "))if (b == 1):	features.append(1)c = int(input("\tInclude Duration feature?: "))if (c == 1):	features.append(2)d = int(input("\tInclude Heart Sound Duration feature?: "))if (d == 1):	features.append(3)e = int(input("\tInclude Pitch feature?: "))if (e == 1):	features.append(4)#k-means clustering with 5 clusters km = KMeans(n_clusters=clusters-1,             init='random',             n_init=10,             max_iter=300,            tol=1e-04,            random_state=0)y_km = km.fit_predict(X[:,features])#plotimport matplotlib.pyplot as pltplt.scatter(X[:, 2], X[:, 1],             c='white', marker='o', edgecolor='black', s=50)plt.xlabel('duration')plt.ylabel('onset')plt.grid()plt.tight_layout()#plt.savefig('images/11_01.png', dpi=300)plt.show()#evaluating the accuracy of clustering HM = np.zeros((5,clusters))for i in range(len(original)):	if original[i,0] == 1 and originaly[i] == 4:		HM[4][clusters-1] += 1for i in range(syst):    HM[int(y[i])][km.labels_[i]] += 1print ("\n                   0   1   2   3   4")print("Early Systolic: ", HM[0])print("Holo Systolic:  ", HM[1])print("Mid Systolic:   ",HM[2])print("Late Systolic:  ",HM[3])print("Early Diastolic:",HM[4])