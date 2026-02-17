# Task-1 Create an Array and Basic Math

import numpy as np

temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = (temps_celsius * 9/5) + 32
print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)
average_temps_fahrenheit = np.mean(temps_fahrenheit)
print("Average Fahrenheit:", average_temps_fahrenheit)

# Task-2 Array Shape and Statistics

array = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print("Shape:", array.shape)
print("Total elements:", array.size)
print("Highest score:", np.max(array))
print("Lowest score:", np.min(array))
print("Range:", np.ptp(array))

# Task 3: Performance Comparison
import time
numpy_array = np.arange(1, 50001)
python_list = list(range(1, 50001))
start_time = time.time()
numpy_sum = np.sum(numpy_array)
numpy_time = time.time() - start_time
start_time = time.time()
python_sum = sum(python_list)
python_time = time.time() - start_time
print("NumPy sum:", numpy_sum)
print("Python sum:", python_sum)
print(f"NumPy time: {numpy_time:.4f} seconds")
print(f"Python time: {python_time:.4f} seconds")

faster_ratio = python_time / numpy_time
print(f"NumPy is {faster_ratio:.1f}x faster")
