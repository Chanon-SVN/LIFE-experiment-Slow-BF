import numpy as np
f = open('hailmary_data_training.csv')
ff = open('x.csv','r+')
count = 0
for line in f:
    data = line.strip().split('\n')[0]
    ff.write(data)
    ff.write(',1')
    ff.write('\n')
f.close()
ff.close()

