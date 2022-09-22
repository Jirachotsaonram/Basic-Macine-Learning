print('Start date 21/9/2022')

from sklearn import datasets

name  = datasets.load_iris()

print(name.keys())

print(name['DESCR'])
 
