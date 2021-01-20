import numpy as np
import random as random


my_range = np.arange(5)
print(my_range)
# [0 1 2 3 4]
my_range2 = np.arange(start = 1, stop = 6, step = 2)
print(my_range2)
# [1 3 5]

my_list = [i for i in range(5)]
print(my_list)
# [0, 1, 2, 3, 4]


my_array = np.random.randint(low = 0, high = 10, size = (3, 4))
print(my_array)


print()
a = np.arange(1, 4)
b = np.arange(4, 7)

c = np.column_stack((a, b))
print(c)

