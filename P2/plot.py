import matplotlib.pyplot as plt
from temp import * # where the variables are defined


plt.figure()
plt.title('Simulated Annealing: Performance x Training Set Size\n(15000 training iterations)')
plt.plot(datasetPercentage, test_error, '-', label='test error')
plt.plot(datasetPercentage, train_error, '-', label='train error')
plt.legend()
plt.xlabel('Percentage of Training Set')
plt.ylabel('Sum of Squares Error')
plt.show()


plt.figure()
plt.title('Simulated Annealing: Performance x Training Set Size\n(15000 training iterations)')
plt.plot(datasetPercentage, testing_time, '-', label='test time')
plt.plot(datasetPercentage, training_time, '-', label='train time')
plt.legend()
plt.xlabel('Percentage of Training Set')
plt.ylabel('Train/Test time')
plt.show()
