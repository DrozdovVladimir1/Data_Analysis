from tensorflow import*
import tensorflow as tf
from keras import*
from numpy import array
import pandas as pd
model = models.Sequential()
dataframe1 = pd.read_excel('D:\Desktop\Code\code lmao\Machine Learning\data_fixed.xlsx')
data_array = array(dataframe1)
# input=data_array[1:418,1:7]
# output=data_array[1:418,7]
model.add(layers.Dense(units=128,input_shape=[6]))
model.add(layers.Dense(units=256))
model.add(layers.Dense(units=256))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=1))
model.compile(loss='mean_squared_error',optimizer='ftrl')
input = tf.convert_to_tensor(data_array[1:418,1:7], dtype =tf.int64)
output = tf.convert_to_tensor(data_array[1:418,7], dtype= tf.float32)

model.fit(x=input,y=output,epochs=300)
tembulat = array([[1,0,10,0,0,26]])  #class 1 = best 3=worst, sex(male=0), age, relatives, children, fare
vova = array([[2, 0, 35, 0, 2, 3]])
woman = array([[1,1,21,0,0,26]])
poor_girl= array([[3,1,21,0,0,26]])
pr1 = model.predict(tembulat)
pr2 = model.predict(vova)
pr3 = model.predict(woman)
pr4 = model.predict(poor_girl)
#print(pr1, pr2)
print("Tembulat survives with {:.2f}".format(pr1[0][0]*100))
print("Vova survives with {:.2f}".format(pr2[0][0]*100))
print("Woman survives with {:.2f}".format(pr3[0][0]*100))
print("Poor girl survives with {:.2f}".format(pr4[0][0]*100))
