# encoding: utf-8
from LR import *
from operator import itemgetter, attrgetter


def loadData():
    train_x = []
    train_y = []
    fileIn = open('testSet-LR.txt')
    for line in fileIn.readlines():
        lineArr = line.strip().split()
        train_x.append([1.0, float(lineArr[0]), float(lineArr[1])])
        # , float(lineArr[2]), float(lineArr[3])
        train_y.append(float(lineArr[2]))
    return mat(train_x), mat(train_y).transpose()

# step 1: load data
print "step 1: load data..."
train_x, train_y = loadData()
test_x = train_x
test_y = train_y
# [20: 41] train_x = train_x train_y = train_y
numSamples, numFeatures = shape(test_x)

# step 2: training...
print "step 2: training..."
opts = {'alpha': 0.01, 'maxIter': 100, 'optimizeType': 'smoothStocGradDescent'}
opts['maxIter'] = input('please input maximum number of iterations: ')
weights = trainLogRegres(train_x, train_y, opts)
optimalWeights = weights[0]
# print weights[1]
print ('optimal weights: ', optimalWeights)

# step 3: testing
print "step 3: testing..."
testResult = testLogRegres(optimalWeights, test_x, test_y)
accuracy = testResult[0]
# convert to an array of characters
# map(str, sorted(testResult[1], key=itemgetter(1), reverse=True))
score = sorted(testResult[1], key=itemgetter(1), reverse=True)
write_excel(test_x, score)
# for i in xrange(numSamples):
#     print score[i]
# print mat(sorted(score[1], reverse = True)).transpose()

# step 4: show the result
print "step 4: show the result..."
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)
# showLogRegres(optimalWeights, train_x, train_y)

# step 5: show weights curves
print "step 5: show weights curves..."
showWeightCurves(weights, opts)