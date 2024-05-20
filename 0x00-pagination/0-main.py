#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)
tu = []
i = res[0]
while (i < res[-1]):
    tu.append(i)
    i += 1
print(tu)