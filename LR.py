# # coding:utf-8
# from numpy import linalg
# import numpy
# import math
# #
# A = [100, 50]
# B = [1000, 500]
# num = float(A[0] * B[0] + A[1] * B[1]) #若为行向量则 A * B.T
# denom = linalg.norm(A) * linalg.norm(B)
# cos = num / denom #余弦值
# sim1 = 0.5 + 0.5 * cos #归一化
# print sim1
# dist = math.sqrt(math.pow(A[1] - B[1], 2) + math.pow(A[0] - B[0], 2))
# sim2 = 1.0 / (1.0 + dist) #归一化
# print sim2

############################

from numpy import *
import matplotlib.pyplot as plt
import time
import xlwt


# calculate the sigmoid function
def sigmoid(X):
    return 1.0 / (1 + exp(-X))


# train a logistic regression model using some optional optimize algorithm
# input: train_x is a mat datatype, each row stands for one sample
# train_y is mat datatype too, each row is the corresponding label
# opts is optimize option include step and maximum number of iterations
def trainLogRegres(train_x, train_y, opts):
    # calculate training time
    startTime = time.time()
    numSamples, numFeatures = shape(train_x)
    alpha = opts['alpha'];
    maxIter = opts['maxIter']
    weights = ones((numFeatures, 1))
    # print weights
    weight = []
    # optimize through gradient descent algorilthm
    for k in range(maxIter):
        if opts['optimizeType'] == 'gradDescent':  # gradient descent algorilthm
            output = sigmoid(train_x * weights)
            error = train_y - output
            weights += alpha * train_x.transpose() * error
        elif opts['optimizeType'] == 'stocGradDescent':  # stochastic gradient descent
            for i in range(numSamples):
                output = sigmoid(train_x[i, :] * weights)
                error = train_y[i, 0] - output
                weights += alpha * train_x[i, :].transpose() * error
        elif opts['optimizeType'] == 'smoothStocGradDescent':  # smooth stochastic gradient descent
            # randomly select samples to optimize for reducing cycle fluctuations
            dataIndex = range(numSamples)
            for i in range(numSamples):
                alpha = 4.0 / (1.0 + k + i) + 0.01
                randIndex = int(random.uniform(0, len(dataIndex)))
                output = sigmoid(train_x[randIndex, :] * weights)
                error = train_y[randIndex, 0] - output
                weights += alpha * train_x[randIndex, :].transpose() * error
                del (dataIndex[randIndex])  # during one interation, delete the optimized sample
            weight.append([k, float(weights[0]), float(weights[1]), float(weights[2])])
        else:
            raise NameError('Not support optimize method type!')

    print 'Congratulations, training complete! Took %fs!' % (time.time() - startTime)
    return weights, weight


# test your trained Logistic Regression model given test set
def testLogRegres(weights, test_x, test_y):
    numSamples, numFeatures = shape(test_x)
    matchCount = 0
    score = []
    for i in xrange(numSamples):
        score.append([i, float(sigmoid(test_x[i, :] * weights))])
        predict = sigmoid(test_x[i, :] * weights)[0, 0] > 0.5
        if predict == bool(test_y[i, 0]):
            matchCount += 1
    accuracy = float(matchCount) / numSamples
    return accuracy, score

# def getScore(weights, test_x):
#     numSamples, numFeatures = shape(test_x)
#     score = []
#     for i in xrange(numSamples):
#         score.append(float(sigmoid(test_x[i, :] * weights)))
#     return score

# show your trained logistic regression model only available with 2-D data
# def showLogRegres(weights, train_x, train_y):
#     # notice: train_x and train_y is mat datatype
#     numSamples, numFeatures = shape(train_x)
#     if numFeatures != 3:
#         print "Sorry! I can not draw because the dimension of your data is not 2!"
#         return 1
#
#     # draw all samples
#     for i in xrange(numSamples):
#         if int(train_y[i, 0]) == 0:
#             plt.plot(train_x[i, 1], train_x[i, 2], 'or')
#         elif int(train_y[i, 0]) == 1:
#             plt.plot(train_x[i, 1], train_x[i, 2], 'ob')
#
#     # draw the classify line
#     min_x = min(train_x[:, 1])[0, 0]
#     max_x = max(train_x[:, 1])[0, 0]
#     weights = weights.getA()  # convert mat to array
#     y_min_x = float(-weights[0] - weights[1] * min_x) / weights[2]
#     y_max_x = float(-weights[0] - weights[1] * max_x) / weights[2]
#     plt.plot([min_x, max_x], [y_min_x, y_max_x], '-g')
#     plt.xlabel('X1');
#     plt.ylabel('X2')
#     plt.show()


# show your trained logistic regression model Weight Curves
def showWeightCurves(weights, opts):
    ax1 = plt.subplot(3, 1, 1)
    ax2 = plt.subplot(3, 1, 2)
    ax3 = plt.subplot(3, 1, 3)
    for i in range(opts['maxIter']):
        # plt.plot(weights[1][i][0], weights[1][i][1], 'or')
        if i > 0:
            plt.sca(ax1)
            plt.plot([weights[1][i - 1][0], weights[1][i][0]], [weights[1][i - 1][1], weights[1][i][1]], '-g')
            # plt.plot([0, 100], [weights[1][99][1], weights[1][99][1]], '-g')
            plt.sca(ax2)
            plt.plot([weights[1][i - 1][0], weights[1][i][0]], [weights[1][i - 1][2], weights[1][i][2]], '-r')
            # plt.plot([0, 100], [weights[1][99][2], weights[1][99][2]], '-r')
            plt.sca(ax3)
            plt.plot([weights[1][i - 1][0], weights[1][i][0]], [weights[1][i - 1][3], weights[1][i][3]], '-y')
            # plt.plot([0, 100], [weights[1][99][3], weights[1][99][3]], '-y')
    plt.xlabel('iteration times')
    plt.ylabel('history weights')
    plt.show()


# set excel style
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


# write excel
def write_excel(test_x, score):
    numSamples, numFeatures = shape(test_x)
    workbook = xlwt.Workbook(encoding='utf-8')
    data_sheet = workbook.add_sheet('demo')
    data_sheet.write(0, 0, 'ID', set_style('Times New Roman', 220, True))
    # data_sheet.write(0, 1, 'ID')
    for i in xrange(numSamples):
        data_sheet.write(i + 1, 0, score[i][0], set_style('Times New Roman', 220, True))
    workbook.save('demo.xls')
