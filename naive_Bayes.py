from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression


iris = datasets.load_iris()
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
right_num = (iris.target == y_pred).sum()
print("Total testing num :%d , naive bayes accuracy :%f" % (iris.data.shape[0], float(right_num)/iris.data.shape[0]))

lr = LogisticRegression()
l_pred = lr.fit(iris.data, iris.target).predict(iris.data)
right_num1 = (iris.target == l_pred).sum()
print("Total testing num :%d , naive bayes accuracy :%f" % (iris.data.shape[0], float(right_num1)/iris.data.shape[0]))
