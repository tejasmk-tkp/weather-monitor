''' 
partly-cloudy-day: 0
rain: 1
clear-day: 2
wind: 3
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

features = pd.read_csv('chennai 2023-01-01 to 2024-02-27.csv')

labels = np.array(features['cloudcover'])
features= features.drop(['name', 'datetime', 'preciptype', 'snow', 'snowdepth', 'sunrise', 'sunset', 'conditions', 'description', 'icon', 'stations', 'cloudcover', 'solarenergy', 'tempmax', 'tempmin', 'feelslikemax', 'feelslikemin', 'feelslike', 'dew', 'precip', 'precipprob', 'precipcover', 'preciptype', 'windgust', 'windspeed', 'winddir', 'visibility', 'solarradiation', 'uvindex', 'severerisk', 'moonphase'], axis = 1)
feature_list = list(features.columns)
features = np.array(features)

train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.1, random_state = 80)


rf = DecisionTreeRegressor(random_state = 80)
rf.fit(train_features, train_labels)

predictions = rf.predict(test_features)
errors = abs(predictions - test_labels)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

pre = rf.predict([[79.2, 7.00, 26.66]])
print(pre)

#print(len(errors), len(test_labels))

mape = 0
for i in range(len(errors)):
    mape += abs(predictions[i]-test_labels[i])
    mape /= len(errors)

accuracy = 100 - mape
print('Accuracy:', round(accuracy, 4), '%.')

import matplotlib.pyplot as plt
try:
    x = predictions
    y = test_labels
    plt.plot(x, label = 'Predicted Values')
    plt.plot(y, label = 'Actual Values')
    plt.xlabel('Days')
    plt.ylabel('Cloud Cover')
    plt.legend()
    plt.show()
except KeyboardInterrupt:
    print('Closed by user!')
    plt.close()
