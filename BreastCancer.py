import numpy as np
from sklearn import preprocessing, model_selection, neighbors,svm
import pandas as pd
from math import * 
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')
import random
# import data and data cleaning
df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -9999, inplace=True)
df.drop(columns=['id'], inplace=True)
print(df.head())
# decideing x and y values
x = np.array(df.drop(columns=['class'])) 
y = np.array(df['class'])
#train model
x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y,test_size=0.2)
#fit the model into algorithm
clf = neighbors.KNeighborsClassifier()
clf.fit(x_train, y_train)
accuracy = clf.score(x_test, y_test)

print('K-Nearest Neighbors accuaracy', accuracy)

# full_data = df.astype(float).values.tolist()
# random.shuffle(full_data)

# test_size = 0.2
# train_set = {2:[], 4:[]}
# test_set = {2:[], 4:[]}
# train_data = full_data[:-int(test_size*len(full_data))]
# test_data = full_data[-int(test_size*len(full_data)):]
# for i in train_data:
#     train_set[i[-1]].append(i[:-1])

# for i in test_data:
#     test_set[i[-1]].append(i[:-1])




# def k_nearest_neighbors(data, predict, k=3):
#     if len(data) >= k:
#         warnings.warn('K is set to a value less than total voting groups!')
    
#     distances = []
#     for group in data:
#         for features in data[group]:
#             euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
#             distances.append([euclidean_distance, group])
#     votes = [i[1] for i in sorted(distances) [:k]]
#     # print (Counter(votes).most_common(1))
#     vote_result = Counter(votes).most_common(1)[0][0]


#     return vote_result

# correct = 0
# total = 0
# for group in test_set:
#     for data in test_set[group]:
#         vote = k_nearest_neighbors(train_set, data, k=5)
#         if group == vote:
#             correct += 1
#         total += 1
# print('Accuracy', correct/total )