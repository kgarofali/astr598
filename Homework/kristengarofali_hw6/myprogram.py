from __future__ import print_function
import mergesort_slice, mergesort_hilo
from mergesort_hilo import merge_sort_hilo
from mergesort_slice import merge_sort_slice
import numpy as np
import matplotlib.pyplot as plt
import timeit
from timeit import Timer

test_arr = np.random.randint(1,100,10).tolist()
print("Unsorted test arr: {0}".format(test_arr))
merge_sort_hilo(test_arr)
print("Sorted test arr: {0}".format(test_arr))

N_two = np.random.randint(1,100,10**2).tolist()
N_four = np.random.randint(1,100,size=10**4).tolist()
N_six = np.random.randint(1,100,size=10**6).tolist()
N_eight = np.random.randint(1,100, size=10**8).tolist()
size_list = [N_two, N_four, N_six, N_eight]



times = np.zeros(len(size_list))
for i in range(len(size_list)):
    t = Timer(lambda: merge_sort_hilo(size_list[i]))
    times[i] = t.timeit(number=3)



logs = [10**2*np.log10(10**2), 10**4*np.log10(10**4), 10**6*np.log10(10**6), 10**8*np.log10(10**8)]
plt.loglog(times,logs,'.')
plt.xlabel('Time (s)')
plt.ylabel('Nlog(N)')
plt.savefig('mergesort_times.png', format='png')
 
