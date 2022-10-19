"""
    Author: Eder Machado
    Description: Input values in python
    Create Date: 19.10.2022 13:45
"""
# 1. input
"""
name = input("Please enter your name: ")
print("Hello, ", name)
"""

# 2. mean function (calculate the average)

import statistics


exList = [5,3,2,9,7,4,3,1,8,9,9,9]
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

print("The Average 'mean' is", statistics.mean(speed))

# 3. median function (calculate the mid value)
"""
learn more here
https://www.w3schools.com/python/python_ml_mean_median_mode.asp

Median -> First de array ou list is sorted in ascendent way, then
the mid value(s) are determined and divided by the number of mid value(s)
found

"""

print("The Median 'middle point' is", statistics.median(speed))

# 4. mode function
"""
    mode function counts the number that appears more times
"""

print("The Mode is", statistics.mode(exList))

# 5. stdev
"""
    Desvio padrão explicado em detalhes:
    https://pt.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/a/calculating-standard-deviation-step-by-step
"""

print("The Standard Deviation", statistics.stdev(exList))

# 6. variance
"""
    https://www.w3schools.com/python/python_ml_standard_deviation.asp
"""
print("The variance", statistics.variance(exList))
