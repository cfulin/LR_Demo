from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from numpy import *

iris = datasets.load_iris()
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
right_num = (iris.target == y_pred).sum()
print("Total testing num :%d , naive bayes accuracy :%f" % (iris.data.shape[0], float(right_num)/iris.data.shape[0]))


def loadData():
    train_x = []
    train_y = []
    fileIn = open('testSet-LR.txt')
    for line in fileIn.readlines():
        lineArr = line.strip().split()
        train_x.append([float(lineArr[0]), float(lineArr[1])])
        # , float(lineArr[2]), float(lineArr[3])
        train_y.append(float(lineArr[2]))
    return mat(train_x), mat(train_y).transpose()


train_x, train_y = loadData()
test_x = train_x
test_y = train_y

lr = LogisticRegression()

right_num1 = 0
l_pred = lr.fit(train_x, train_y).predict(train_x)

print lr.fit(train_x, train_y).predict_proba(train_x)


for i in range(train_x.shape[0]):
    if train_y[i] == l_pred[i]:
        right_num1 += 1
print("Total testing num :%d , LogisticRegression accuracy :%f" % (train_x.shape[0], float(right_num1)/train_x.shape[0]))

from scipy.optimize import fsolve
