import matplotlib.pyplot as plt
from temp import * # where the variables are defined


plt.figure()
plt.title('Randomized Hill Climbing: Performance x Number of Random Restarts\n(6000 training iterations)')
plt.plot(numberOfRestarts, test_error, '-', label='test error')
plt.plot(numberOfRestarts, train_error, '-', label='train error')
plt.legend()
plt.xlabel('Number of Restarts')
plt.ylabel('Sum of Squares Error')
plt.show()


plt.figure()
plt.title('Randomized Hill Climbing: Performance x Number of Random Restarts\n(6000 training iterations)')
plt.plot(numberOfRestarts, testing_time, '-', label='test time')
plt.plot(numberOfRestarts, training_time, '-', label='train time')
plt.legend()
plt.xlabel('Bag Size')
plt.ylabel('Train/Test time')
plt.show()
