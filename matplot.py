import matplotlib.pyplot as plt
import pandas as pd
from numpy import array
dataframe1 = pd.read_excel('D:\Desktop\Code\code lmao\Machine Learning\data_fixed.xlsx')
data_array = array(dataframe1)
gender = data_array[1:418, 2]
survived = data_array[1:418, 7]
ages = data_array[1:418, 3]
men = 0
menSurvived = 0
women = 0
womenSurvived = 0

for index, sex in enumerate(gender):
    if str(sex) == '0':
        if survived[index] == 1:
            menSurvived+=1
        men+=1
    else:
        if survived[index] == 1:
            womenSurvived +=1
        women+=1
dict1 = {}
for age in ages:
    dict1[age] = dict1.get(age, 0) + 1
# print(men)
# print(women)
# print(dict1)






labels = ['Men', 'Women']
share = [men, women] 
# plt.pie(x=share, labels=labels, autopct='%.2f%%')

# explode = (0.1, 0, 0, 0, 0)  # only "explode" the 1st slice 
plt.style.use('ggplot')
plt.title('Gender distribution on Titanic')
plt.pie(x=share, labels=labels, autopct='%.2f%%',
         startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.legend(loc='upper left')

# donut
circle = plt.Circle(xy=(0,0), radius=.75, facecolor='white')
plt.gca().add_artist(circle)
plt.show()


fig = plt.figure(figsize=(0, 90))
ax = fig.add_subplot()

tmp = dict1.items()
x = []
y = []
for xVal, yVal in tmp:
    x.append(xVal)
    y.append(yVal)
ax.bar(y,x)
ax.grid()
plt.show()