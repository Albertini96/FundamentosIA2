# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# import some data to play with
iris = datasets.load_iris()
features = iris.feature_names
names = iris.target_names
x = iris.data
y = iris.target


x = x[y != 0]
y = y[y != 0]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=True)

# Perceptron
perc = Perceptron(tol=1e-3, random_state=0, max_iter=1000)
perc.fit(x_train, y_train)
y_p = perc.predict(x_test)


plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], names):
    plt.scatter(x_test[y_p == i, 0], x_test[y_p == i, 1], color=color, alpha=.8, lw=lw,
                label=target_name)
    
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('Perceptron')
plt.show()

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.33, random_state=True)

# Multi Layer Perceptron
mlp = MLPClassifier(max_iter=1000)
mlp.fit(x_train, y_train)
mlp_score = mlp.score(x_test, y_test)
y_m = mlp.predict(x_test)

plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], names):
    plt.scatter(x_test[y_m == i, 0], x_test[y_m == i, 1], color=color, alpha=.8, lw=lw,
                label=target_name)
    
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('MLP')
plt.show()
