# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LinearRegression
from matplotlib.colors import ListedColormap
from sklearn import svm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

iris = load_iris()

labels = iris.target_names
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=True)
#
# Regressao Linear
regr = LinearRegression()
regr.fit(x_train, y_train)
y_pred = regr.predict(x_test)

plt.scatter(y_test, y_pred, marker = 'o', c = y_test, edgecolors = 'black')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], lw=1, c = 'green')
plt.xlabel('got', fontsize = 10)
plt.ylabel('expected', fontsize = 10)
plt.title('MMQ')

# PCA
plt.figure()
pca = PCA(n_components=2)
X_r = pca.fit(x).transform(x)
X_r1 = X_r[:,0]
X_r2 = X_r[:,1]
coeficiente = np.transpose(pca.components_[0:2, :])
n = coeficiente.shape[0]
plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], labels):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=.8, lw=lw,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA')
plt.show()

# LDA
lda = LinearDiscriminantAnalysis(n_components=2)
lda_ = lda.fit(x, y).transform(x)
colors = ['navy', 'turquoise', 'darkorange']
for color, i, target_name in zip(colors, [0, 1, 2], labels):
    plt.scatter(lda_[y == i, 0], lda_[y == i, 1], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA')

plt.show()

# SVM
plt.figure()
x_df = pd.DataFrame(iris.data, columns = iris.feature_names).iloc[:,2:4].values
clf = svm.LinearSVC(C=1).fit(x_df, y)
x_svm_min, x_svm_max = x_df[:, 0].min() - 1, x_df[:, 0].max() + 1
y_svm_min, y_svm_max = x_df[:, 1].min() - 1, x_df[:, 1].max() + 1
xp_svm, yp_svm = np.meshgrid(np.arange(x_svm_min, x_svm_max, .02), np.arange(y_svm_min, y_svm_max, .02))
svm_pred = clf.predict(np.c_[xp_svm.ravel(), yp_svm.ravel()]).reshape(xp_svm.shape)

colors = ('blue', 'green', 'yellow')
cmap = ListedColormap(colors[:len(np.unique(y))])

for color, i, target_name in zip(colors, [0, 1, 2], iris.target_names):
    plt.scatter(x[y == i, 0], x[y == i, 1],  color=color, label=target_name, edgecolors='black')

plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])

plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('SVM')
plt.show()   