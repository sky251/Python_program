# 21). By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.import pprint

import pprint

def ThreeD(a, b, c):
    lst = [[['#' for col in range(a)] for col in range(b)] for row in range(c)]
    return lst
      

col1 = 3
col2 = 5
row = 8
pprint.pprint(ThreeD(col1, col2, row))