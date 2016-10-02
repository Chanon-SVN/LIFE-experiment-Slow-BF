import numpy as np
f = open('hailmary_data_training.csv')
ff = open('training_data_detail.csv','r+')
count = 0
for line in f:
    data = line.strip().split('\n')[0]
    datasplit = data.split(',')
    datasplit = [datasplit[0],datasplit[1],datasplit[2],datasplit[3]]
    if(np.array_equal(datasplit,['0','1','-1','1']) or np.array_equal(datasplit,['1','0','-1','1'])):
       count = count+1
       print count
    else:
        ff.write(data)
        ff.write('\n')
f.close()

