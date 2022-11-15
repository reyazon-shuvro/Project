# -*- coding: utf-8 -*-
"""Copy of 201-15-13717-problem1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16bqi9Q1w9QI-umcbc1MfJ0xQCPpTMSHF

Library and data input
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('/content/insurance.csv')
df

"""Missing value handle"""

df.isnull().sum()

df['bmi'].fillna(df['bmi'].mean(), inplace= True)
df

df['charges'].fillna(df['charges'].mean(), inplace= True)

"""Reg for age"""

X = df.iloc[:, 0:1].values
y = df.iloc[:, -1].values
X

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X[:,:] = sc.fit_transform(X[:,:])
X

"""split the data"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 1)

print(X_test)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
y_pred

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Age vs Charges (Training set)')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.show()

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Age vs Charges (Testing set)')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.show()

y

sum = 0
for i in range(len(y_pred)):
  sum = (y[i]-y_pred[i])*(y[i]-y_pred[i]) + sum
mse1 = sum/(len(y_pred))
mse1

"""Reg for BMI"""

X = df.iloc[:, 2:3].values
y = df.iloc[:, -1].values
X

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X[:,:] = sc.fit_transform(X[:,:])
X

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 1)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
y_pred

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('BMI vs Charges (Training set)')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.show()

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('BMI vs Charges (Testing set)')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.show()

sum = 0
for i in range(len(y_pred)):
  sum = (y[i]-y_pred[i])*(y[i]-y_pred[i]) + sum
mse2 = sum/(len(y_pred))
mse2

"""Reg for Children"""

X = df.iloc[:, 3:4].values
y = df.iloc[:, -1].values
X

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X[:,:] = sc.fit_transform(X[:,:])
X

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 1)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
y_pred

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Children vs Charges (Training set)')
plt.xlabel('Children')
plt.ylabel('Charges')
plt.show()

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Children vs Charges (Testing set)')
plt.xlabel('Children')
plt.ylabel('Charges')
plt.show()

sum = 0
for i in range(len(y_pred)):
  sum = (y[i]-y_pred[i])*(y[i]-y_pred[i]) + sum
mse3 = sum/(len(y_pred))
mse3

print(min(mse1,mse2,mse3))

"""BMI is lowest MSE"""

X = df.iloc[:, [2,-1]].values
y = df.iloc[:, 4].values
X

y

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
y

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X[:,:] = sc.fit_transform(X[:,:])
X

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 1)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.25, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i in np.unique(y_set):
    plt.scatter(X_set[y_set == i, 0], X_set[y_set == i, 1],
                c = ListedColormap(('red', 'green'))(i), label = i)
plt.title('Logistic Regression (Training set)')
plt.xlabel('BMI & Charges')
plt.ylabel('Smoking')
plt.legend()
plt.show()

from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.25, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i in np.unique(y_set):
    plt.scatter(X_set[y_set == i, 0], X_set[y_set == i, 1],
                c = ListedColormap(('red', 'green'))(i), label = i)
plt.title('Logistic Regression (Test set)')
plt.xlabel('BMI & Charges')
plt.ylabel('Smoking')
plt.legend()
plt.show()

