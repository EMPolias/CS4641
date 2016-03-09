import matplotlib.pyplot as plt

bagSize = [5, 10, 20, 40, 80, 120, 160, 200, 300, 500, 700, 850, 1000, 1200]
train_error_2800 = [46.190, 41.762, 38.714, 36.571, 33.333, 33.000, 33.762, 35.333, 36.429, 38.238, 38.476, 42.333, 42.857, 41.714]
test_error_2800 = [47.778, 40.889, 43.667, 41.000, 37.222, 42.778, 41.222, 41.889, 44.778, 44.667, 46.111, 50.444, 44.444, 45.667]
train_time_2800 = [29.550, 28.877, 31.131, 36.917, 47.675, 58.454, 67.842, 84.049, 127.969, 227.227, 311.459, 422.773, 456.978, 561.697]
test_time_2800 = [0.003, 0.003, 0.003, 0.003, 0.004, 0.005, 0.006, 0.007, 0.011, 0.018, 0.024, 0.033, 0.035, 0.041]
train_error_5500 = [46.143, 40.619, 35.476, 34.000, 30.714, 29.905, 30.381, 27.238, 30.524, 28.762, 31.143, 33.714, 35.952, 36.286]
test_error_5500 = [47.444, 40.444, 42.000, 40.778, 33.889, 39.556, 38.556, 38.667, 39.111, 41.444, 42.222, 40.667, 45.111, 42.333]
train_time_5500 = [55.611, 56.503, 60.486, 74.745, 93.501, 115.855, 136.825, 163.190, 282.877, 455.305, 680.109, 733.730, 863.918, 1055.968]
test_time_5500 = [0.003, 0.003, 0.003, 0.004, 0.004, 0.005, 0.006, 0.007, 0.012, 0.021, 0.025, 0.029, 0.034, 0.042]
train_error_10000  = [46.143, 40.429, 34.810, 29.143, 25.238, 24.571, 24.619, 23.476, 21.143, 23.714, 25.048, 25.714, 29.286, 28.333]
test_error_10000  = [47.444, 40.889, 44.333, 42.222, 32.111, 41.000, 39.111, 38.333, 39.889, 38.444, 41.667, 39.889, 42.222, 39.333]
train_time_10000  = [101.740, 105.216, 112.282, 131.805, 165.862, 207.350, 242.085, 304.929, 482.206, 827.403, 1161.870, 1412.485, 1582.958, 2068.308]
test_time_10000  = [0.003, 0.003, 0.003, 0.003, 0.004, 0.005, 0.006, 0.007, 0.011, 0.018, 0.028, 0.030, 0.036, 0.042]



plt.figure()
plt.title('Randomized Hill Climbing: Performance x Bag Size')
plt.rc('legend',**{'fontsize':10})
plt.plot(bagSize, test_error_2800, '-', label='testErr 2800iter', c='#c2d4ff')
plt.plot(bagSize, test_error_5500, '-', label='testErr 5500iter', c='#899cff')
plt.plot(bagSize, test_error_10000, '-', label='testErr 10000iter', c='#0000ff')
plt.plot(bagSize, train_error_2800, '-', label='trainErr 2800iter', c='#aae7a7')
plt.plot(bagSize, train_error_5500, '-', label='trainErr 5500iter', c='#7ad36f')
plt.plot(bagSize, train_error_10000, '-', label='trainErr 10000iter', c='#007f00')
plt.legend()
plt.xlabel('Bag Size')
plt.ylabel('Sum of Squares Error')
plt.show()


plt.figure()
plt.title('Randomized Hill Climbing: Train/Test time x Bag Size')
## plt.plot(bagSize, test_time_2800, '-', label='test time (2800 iter)', c='#c2d4ff')
## plt.plot(bagSize, test_time_5500, '-', label='test time (5500 iter)', c='#899cff')
# plt.plot(bagSize, test_time_10000, '-', label='test time (10000 iter)', c='#0000ff')
plt.plot(bagSize, train_time_2800, '-', label='train time (2800 iter)', c='#aae7a7')
plt.plot(bagSize, train_time_5500, '-', label='train time (5500 iter)', c='#7ad36f')
plt.plot(bagSize, train_time_10000, '-', label='train time (10000 iter)', c='#007f00')
plt.legend()
plt.xlabel('Bag Size')
plt.ylabel('Train/Test time')
plt.show()
