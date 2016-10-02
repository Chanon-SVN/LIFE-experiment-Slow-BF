import json
import smtplib
import os
import sys
import dateutil.parser
from time import mktime
from time import strptime
from datetime import datetime
import datetime
import csv
from math import ceil
import numpy as np
import scipy as sp
from sklearn import svm
from sklearn.externals import joblib

clf = joblib.load('experiment_model/svm_model-ver4.pkl')
prediction = []

f = open("testing_data.csv")
f.readline()
count = 0
line = 0
for line in f:
   data = line.strip().split('\n')[0]
   datasplit = data.split(',')
   datatest = [datasplit[0],datasplit[1],datasplit[3]]
  # print datatest
   predict = (str(clf.predict(np.asarray(datatest))[0:1]))
   print datatest
   print predict
   check = ['1'] 
   if (str(predict) != str(check)): 
      count = count+1

      print("NOT EQUAL ",count)
#   print("---------------------------------------")
#PREDICT WITH SVM.
print(str(clf.predict([4,0,-1])[0:1]))
