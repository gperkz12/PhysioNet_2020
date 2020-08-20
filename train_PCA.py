import numpy as np
import scipy.io as sio
import pickle as pk
from sklearn.decomposition import PCA
from sklearn import decomposition, datasets
from sklearn.preprocessing import StandardScaler


def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)


pca_fit = pk.load(open("pca_fit.pkl", 'rb'))

X_train = pca_fit

sc = StandardScaler()
sc.fit(X_train)
X_std_train = sc.transform(X_train)

pca = PCA(n_components=20)
pca.fit(X_std_train)

# Save sc as a pickle file for use in get_12ECG_features
save_object(sc, 'sc.pkl')
print(sc)
print(sc.mean_.shape)
print(sc.var_.shape)
print(sc.scale_.shape)
print(sc.n_samples_seen_)
# Save pca as a pickle file for use in get_12ECG_features
print(pca)
print(pca.components_.shape)
save_object(pca, 'pca.pkl')


