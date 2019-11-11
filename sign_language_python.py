import pandas
from pandas.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import serial
import numpy as np
from matplotlib import pyplot as plt
from time import time


url = "dataset.csv"
names = ['first-finger', 'second finger', 'third finger', 'fourth finger', 'fifth finger','first Contact sensor','2nd Contact sensor','3rd Contact sensor','4th Contact sensor','5th Contact sensor','6th Contact sensor','name']
dataset = pandas.read_csv(url, names=names)

# Split-out validation dataset
array = dataset.values
X = array[:,0:11]
Y = array[:,11]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))


#predictions for new cases
ser = serial.Serial("COM9", 9600)
while True:
    case = str(ser.readline())
    case = case[2:][:-5]
    case = case.split("|")
    case = list(map(int, case))
    predictions = knn.predict([case])
    print(predictions)
