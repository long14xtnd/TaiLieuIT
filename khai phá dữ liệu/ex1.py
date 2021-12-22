import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

wheats = pd.read_csv("Seed_Data.csv")
wheats = wheats.rename(columns={"target":"label"})
wheats.head()

#Data Visualozation - Label vs other continuous variables - box plot
fig, axs = plt.subplots(ncols = 4, nrows = 2, figsize=(15,8),sharex=True)
for axi,col_name in zip(axs.flat,list(wheats.columns)):
    sns.boxplot(x="label",y=col_name,data=wheats,ax=axi)
fig.delaxes(ax = axs[1,3])
fig.tight_layout()
#fig.show()

#KMeans Clustering - Optimal number of clusters
inertia = []
for c in range(1,7):
    model = KMeans(n_clusters=c)
    model.fit(wheats[list(wheats.columns[:-1])])
    inertia.append(model.inertia_)
fig, ax = plt.subplots(figsize = (10 ,4))
ax.plot(np.arange(1 , 7) , inertia , marker="o")
ax.set_xlabel('Number of Clusters')
ax.set_ylabel('Inertia')
#fig.show()

#KMeans Clustering - Validation
model = KMeans(n_clusters = 3)
model.fit(wheats[list(wheats.columns[:-1])])
label_pred = model.predict(wheats[list(wheats.columns[:-1])])
wheat_preds = pd.DataFrame({"label_act":list(wheats["label"]),"label_kmeans":list(label_pred)})
ok = pd.crosstab(wheat_preds.label_act,wheat_preds.label_kmeans)
ok

#k-Means Clustering - Standardisation
scaler = StandardScaler()
kmeans = KMeans(n_clusters=3)
pipeline = make_pipeline(scaler,kmeans)
pipeline.fit(wheats[list(wheats.columns[:-1])])
labels_pred_std = pipeline.predict(wheats[list(wheats.columns[:-1])])
wheat_preds["labels_kmeans_std"] = labels_pred_std
ok3 = pd.crosstab(wheat_preds.label_act,wheat_preds.labels_kmeans_std)
ok3
