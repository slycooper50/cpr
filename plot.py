#!/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.rcParams['pgf.texsystem'] = 'pdflatex'
plt.rcParams['text.usetex'] = True
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['axes.labelsize'] = 18


file_cpr = open('./file_cpr', 'r')
file_ilu = open('./file_ilu', 'r')

time_cpr = np.array([])
its_cpr = np.array([])
matbalerr_cpr = np.array([])
cpu_time_cpr = np.array([])

time_ilu = np.array([])
its_ilu = np.array([])
matbalerr_ilu = np.array([])
cpu_time_ilu = np.array([])

for line in file_cpr:
    time_cpr = np.append(time_cpr, line.split()[1])
    its_cpr = np.append(its_cpr, line.split()[5])
    matbalerr_cpr = np.append(matbalerr_cpr, line.split()[6])
    cpu_time_cpr = np.append(cpu_time_cpr, line.split()[11])

for line in file_ilu:
    time_ilu = np.append(time_ilu, line.split()[1])
    its_ilu = np.append(its_ilu, line.split()[5])
    matbalerr_ilu = np.append(matbalerr_ilu, line.split()[6])
    cpu_time_ilu = np.append(cpu_time_ilu, line.split()[11])

cpu_time_cpr = cpu_time_cpr.astype(np.float64)
time_cpr = time_cpr.astype(np.float64)
matbalerr_cpr = matbalerr_cpr.astype(np.float64)
its_cpr = its_cpr.astype(np.float64)

cpu_time_ilu = cpu_time_ilu.astype(np.float64)
time_ilu = time_ilu.astype(np.float64)
matbalerr_ilu = matbalerr_ilu.astype(np.float64)
its_ilu = its_ilu.astype(np.float64)

## Fig 1 ##
fig, ax = plt.subplots()
ax.set_xlabel('Simulation Time (DAY)')
ax.set_ylabel('Linear Iteration \\#')
ax.set_title('Linear Iteration Number Vs Time')
ax.xaxis.set_major_locator(plt.MaxNLocator(20))
ax.yaxis.set_major_locator(plt.MaxNLocator(20))
ax.plot(time_cpr, its_cpr, label="CPR")
ax.plot(time_ilu, its_ilu, label="ILU(0)")
#ax.set_xticks(time[0::90])
plt.xticks(rotation=90)
plt.margins(0.01)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.gcf().set_size_inches(20, 10)
ax.legend()
plt.legend(loc=2, prop={'size': 20})
plt.savefig('its_time.pdf', dpi=400, backend='pgf')
#plt.show()

## Fig 2 ##
fig, ax = plt.subplots()
ax.set_xlabel('Simulation Time (DAY)')
ax.set_ylabel('CPU Time (Hr)')
ax.set_title('Run Time Vs Simulation Time')
ax.xaxis.set_major_locator(plt.MaxNLocator(20))
ax.yaxis.set_major_locator(plt.MaxNLocator(20))
ax.plot(time_cpr, cpu_time_cpr, label="CPR")
ax.plot(time_ilu, cpu_time_ilu, label="ILU(0)")
#ax.set_xticks(time[0::16])
plt.xticks(rotation=90)
plt.margins(0.01)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.gcf().set_size_inches(20, 10)
ax.legend()
plt.legend(loc=2, prop={'size': 20})
plt.savefig('cpu_time.pdf', dpi=400, backend='pgf')
#plt.show()

### Fig 3 ##
fig, ax = plt.subplots()
ax.set_xlabel('Simulation Time (DAY)')
ax.set_ylabel('MatBal Error (\\%)')
ax.set_title('MatBal Error Vs Simulation Time')
ax.xaxis.set_major_locator(plt.MaxNLocator(20))
ax.yaxis.set_major_locator(plt.MaxNLocator(20))
ax.plot(time_cpr, matbalerr_cpr, label="CPR")
ax.plot(time_ilu, matbalerr_ilu, label="ILU(0)")
#ax.set_xticks(time[0::16])
plt.xticks(rotation=90)
plt.margins(0.01)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.gcf().set_size_inches(20, 10)
ax.legend()
plt.legend(loc=2, prop={'size': 20})
plt.savefig('matbalerr_time.pdf', dpi=400, backend='pgf')
#plt.show()
