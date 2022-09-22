#Start date 22/9/2022

from sklearn import datasets

name = datasets.load_digits()

print(name.keys())

print(name.images[0:2])

print(name.images[0].shape) #.shape แสดงขนาด
