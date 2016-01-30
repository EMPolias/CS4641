from __future__ import division
from sklearn import tree
from sklearn.metrics import mean_squared_error

import datasets
import numpy as np
import matplotlib.pyplot as plt


# Preparing data
cifar_data = datasets.cifar()

# Training trees of different max_depths
max_depth = range(2, 20)
train_err = [0] * len(max_depth)
test_err = [0] * len(max_depth)

for i, d in enumerate(max_depth):
    print 'learning a decision tree with max_depth=' + str(d)
    clf = tree.DecisionTreeClassifier(max_depth=d)
    clf = clf.fit(cifar_data['train']['data'], cifar_data['train']['labels'])

    train_err[i] = mean_squared_error(cifar_data['train']['labels'],
                                     clf.predict(cifar_data['train']['data']))
    test_err[i] = mean_squared_error(cifar_data['test']['labels'],
                                    clf.predict(cifar_data['test']['data']))
    print 'train_err: ' + str(train_err[i])
    print 'test_err: ' + str(test_err[i])
    print '---'

# Plot results
print 'plotting results'
plt.figure()
plt.title('Decision Trees: Performance x Max Depth')
plt.plot(max_depth, test_err, '-', label='test error')
plt.plot(max_depth, train_err, '-', label='train error')
plt.legend()
plt.xlabel('Max Depth')
plt.ylabel('Mean Square Error')
plt.show()


# Training trees of different training set sizes
train_size = len(cifar_data['train']['data'])
offsets = range(int(0.1 * train_size), train_size, int(0.05 * train_size))
MAX_DEPTH = 8
train_err = [0] * len(offsets)
test_err = [0] * len(offsets)

print 'training_set_max_size:', train_size, '\n'

for i, o in enumerate(offsets):
    print 'learning a decision tree with training_set_size=' + str(o)
    clf = tree.DecisionTreeClassifier(max_depth=MAX_DEPTH)
    clf = clf.fit(cifar_data['train']['data'][:o], cifar_data['train']['labels'][:o])

    train_err[i] = mean_squared_error(cifar_data['train']['labels'][:o],
            clf.predict(cifar_data['train']['data'][:o]))
    test_err[i] = mean_squared_error(cifar_data['test']['labels'][:o],
                                     clf.predict(cifar_data['test']['data'][:o]))
    print 'train_err: ' + str(train_err[i])
    print 'test_err: ' + str(test_err[i])
    print '---'

# Plot results
print 'plotting results'
plt.figure()
plt.title('Decision Trees: Performance x Training Set Size')
plt.plot(offsets, test_err, '-', label='test error')
plt.plot(offsets, train_err, '-', label='train error')
plt.legend()
plt.xlabel('Training Set Size')
plt.ylabel('Mean Square Error')
plt.show()
