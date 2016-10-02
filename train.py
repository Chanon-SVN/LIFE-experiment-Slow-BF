from sklearn import svm
from sklearn.externals import joblib
import numpy as num
clf = svm.SVC()
f = open('x.csv')
setx = []
sety = []
for line in f:
    data = line.split('\n')[0]
    data = data.split(',')
    y = data[-1]
    X = data[0:3]
    setx.append(X)
    sety.append(y)
print(setx)
print(sety)
clf.fit(setx, sety) 
joblib.dump(clf, 'svm_model-ver4.pkl')
