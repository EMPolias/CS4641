import matplotlib.pyplot as plt
from temp import *


problem_name = 'Traveling Salesman'

# MIMIC has interesting results if you plot all iterations
maxIter = len(mimic)
plt.figure()
plt.title(problem_name + ' : Iteration x Fitness')
plt.plot(range(maxIter), map(lambda x: x[1], rhc)[:maxIter], '-', label='RHC')
plt.plot(range(maxIter), map(lambda x: x[1], sima)[:maxIter], '-', label='SimA')
plt.plot(range(maxIter), map(lambda x: x[1], genal)[:maxIter], '-', label='GenAl')
plt.plot(range(maxIter), map(lambda x: x[1], mimic)[:maxIter], '-', label='MIMIC')
plt.legend(loc=4)
plt.xlabel('Iteration (*1000)')
plt.ylabel('Fitness')
plt.show()


maxIter = 50
plt.figure()
plt.title(problem_name + ' : Iteration x Fitness')
plt.plot(range(maxIter), map(lambda x: x[1], rhc)[:maxIter], '-', label='RHC')
plt.plot(range(maxIter), map(lambda x: x[1], sima)[:maxIter], '-', label='SimA')
plt.plot(range(maxIter), map(lambda x: x[1], genal)[:maxIter], '-', label='GenAl')
plt.plot(range(maxIter), map(lambda x: x[1], mimic)[:maxIter], '-', label='MIMIC')
plt.legend(loc=4)
plt.xlabel('Iteration (*1000)')
plt.ylabel('Fitness')
plt.show()

max_time = 100
rhc_times = filter(lambda x: x < max_time, map(lambda x: x[0], rhc))
rhc_fitns = map(lambda x: x[1], rhc)[:len(rhc_times)]
sima_times = filter(lambda x: x < max_time, map(lambda x: x[0], sima))
sima_fitns = map(lambda x: x[1], sima)[:len(sima_times)]
genal_times = filter(lambda x: x < max_time, map(lambda x: x[0], genal))
genal_fitns = map(lambda x: x[1], genal)[:len(genal_times)]
mimic_times = filter(lambda x: x < max_time, map(lambda x: x[0], mimic))
mimic_fitns = map(lambda x: x[1], mimic)[:len(mimic_times)]

plt.figure()
plt.title(problem_name + ' : Time x Fitness')
plt.plot(rhc_times, rhc_fitns, '-', label='RHC')
plt.plot(sima_times, sima_fitns, '-', label='SimA')
plt.plot(genal_times, genal_fitns, '-', label='GenAl')
plt.plot(mimic_times, mimic_fitns, '-', label='MIMIC')
plt.legend(loc=4)
plt.xlabel('Time')
plt.ylabel('Fitness')
plt.show()


plt.figure()
plt.title(problem_name + ' : Time (log) x Fitness')
plt.xscale('log')
plt.plot(rhc_times, rhc_fitns, '-', label='RHC')
plt.plot(sima_times, sima_fitns, '-', label='SimA')
plt.plot(genal_times, genal_fitns, '-', label='GenAl')
plt.plot(mimic_times, mimic_fitns, '-', label='MIMIC')
plt.legend(loc=2)
plt.xlabel('Time')
plt.ylabel('Fitness')
plt.show()
