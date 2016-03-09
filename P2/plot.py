import matplotlib.pyplot as plt
from temp import * # where the variables are defined

datasetPercentage = [1, 2, 3, 5, 8, 10, 15]

plt.figure()
plt.title('Randomized Hill Climbing: Performance x Number of Restarts\n(5500 training iterations)')
plt.plot(datasetPercentage, test_error, '-', label='test error')
plt.plot(datasetPercentage, train_error, '-', label='train error')
plt.legend()
plt.xlabel('Number of Restarts')
plt.ylabel('Sum of Squares Error')
plt.show()


plt.figure()
plt.title('Randomized Hill Climbing: Train/Test time x Number of Restarts\n(5500 training iterations)')
plt.plot(datasetPercentage, test_time, '-', label='test time')
plt.plot(datasetPercentage, train_time, '-', label='train time')
plt.legend()
plt.xlabel('Number of Restarts')
plt.ylabel('Train/Test time')
plt.show()
