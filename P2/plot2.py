import matplotlib.pyplot as plt

bagSize = [0.05, 0.1, 0.3, 0.5, 0.7, 0.9]


train_time_rhc = [36.893, 71.780, 216.214, 367.167, 511.743, 659.633]
test_time_rhc = [0.004, 0.004, 0.004, 0.004, 0.004, 0.004]

train_time_sima = [4.561, 9.031, 27.331, 45.484, 65.983, 84.813]
test_time_sima = [0.005, 0.004, 0.004, 0.004, 0.004, 0.004]

train_time_genal = [13.368, 25.747, 75.368, 124.532, 175.099, 224.364]
test_time_genal = [0.004, 0.006, 0.004, 0.004, 0.004, 0.004]


# plt.figure()
# plt.title('Performance x Training Set Size')
# plt.rc('legend',**{'fontsize':10})
# plt.plot(bagSize, test_error_rhc, '-', label='testErr RHC', c='#c2d4ff')
# plt.plot(bagSize, test_error_sima, '-', label='testErr SimA', c='#899cff')
# plt.plot(bagSize, test_error_genal, '-', label='testErr GenAl', c='#0000ff')
# plt.plot(bagSize, train_error_rhc, '-', label='trainErr RHC', c='#aae7a7')
# plt.plot(bagSize, train_error_sima, '-', label='trainErr SimA', c='#7ad36f')
# plt.plot(bagSize, train_error_genal, '-', label='trainErr GenAl', c='#007f00')
# plt.legend(loc=4)
# plt.xlabel('Percentage of Dataset')
# plt.ylabel('Sum of Squares Error')
# plt.show()


plt.figure()
plt.title('Train/Test time x Training Set Size')
## plt.plot(bagSize, test_time_2800, '-', label='test time (2800 iter)', c='#c2d4ff')
## plt.plot(bagSize, test_time_5500, '-', label='test time (5500 iter)', c='#899cff')
# plt.plot(bagSize, test_time_10000, '-', label='test time (10000 iter)', c='#0000ff')
plt.plot(bagSize, train_time_rhc, '-', label='train time RHC', c='#aae7a7')
plt.plot(bagSize, train_time_sima, '-', label='train time SimA (5500 iter)', c='#7ad36f')
plt.plot(bagSize, train_time_genal, '-', label='train time SimA (15000 iter)', c='#007f00')
plt.legend(loc=1)
plt.xlabel('Percentage of Dataset')
plt.ylabel('Train/Test time')
plt.show()
