"""
    Author: Eder Machado
    Description: Import Syntax used in python 3.x
    Created Date: 19.10.2022 06:31 PM
"""
# 1. long form
"""
import statistics

lista = [1,2,5,8,8,78,9]

print(statistics.mean(lista))
"""

#2. Short form
"""
import statistics as s

lista = [1,2,5,8,8,78,9]

print(s.mean(lista))
"""
#3.Other better form of doing this
"""
from statistics import mean

lista = [1,2,5,8,8,78,9]

print(mean(lista))
"""
#4.Other better form of doing this
""""
from statistics import mean as m

lista = [1,2,5,8,8,78,9]

print(m(lista))
"""
#5.Other better form of doing this
""""
from statistics import mean as m, stdev as s

lista = [1,2,5,8,8,78,9]

print(m(lista))

print(s(lista))
"""
#6.Other better form of doing this

from statistics import *

lista = [1,2,5,8,8,78,9]

print(mean(lista))

print(stdev(lista))
