

from google.colab import drive
drive.mount('/content/drive')



# Import required libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn

import keras
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf

dataset = pd.read_csv("/content/drive/My Drive/AI_ASSIGNMENT/roo_data (1).csv")

dataset.loc[dataset['Suggested Job Role'].str.contains('Engineer', case=False), 'Suggested Job Role'] = 'Engineer'
dataset.loc[dataset['Suggested Job Role'].str.contains('Analyst', case=False), 'Suggested Job Role'] = 'Analyst'
dataset.loc[dataset['Suggested Job Role'].str.contains('Administrator', case=False), 'Suggested Job Role'] = 'Manager'
dataset.loc[dataset['Suggested Job Role'].str.contains('Manager', case=False), 'Suggested Job Role'] = 'Manager'
dataset.loc[dataset['Suggested Job Role'].str.contains('Designer', case=False), 'Suggested Job Role'] = 'Designer'
dataset.loc[dataset['Suggested Job Role'].str.contains('Developer', case=False), 'Suggested Job Role'] = 'Developer'
dataset.loc[dataset['Suggested Job Role'].str.contains('Quality Assurance', case=False), 'Suggested Job Role'] = 'Technical Support'
dataset.loc[dataset['Suggested Job Role'].str.contains('Support', case=False), 'Suggested Job Role'] = 'Technical Support'
dataset.loc[dataset['Suggested Job Role'].str.contains('Architect', case=False), 'Suggested Job Role'] = 'Designer'
dataset.loc[dataset['Suggested Job Role'].str.contains('Design & UX', case=False), 'Suggested Job Role'] = 'Designer'
dataset.loc[dataset['Suggested Job Role'].str.contains('Information Technology Auditor', case=False), 'Suggested Job Role'] = 'Manager'

print(dataset['Suggested Job Role'].unique())

dataset['Suggested Job Role'].value_counts()

print(dataset.isna().sum())

from sklearn.preprocessing import LabelEncoder

lb_make = LabelEncoder()
for column in dataset.columns[14:]:
    dataset[column] = lb_make.fit_transform(dataset[column])

X= dataset.iloc[:,0:38]
y= dataset.iloc[:,38]

#Label Encoding k lia
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()

y1=encoder.fit_transform(y)
Y=pd.get_dummies(y1).values

from sklearn.preprocessing import StandardScaler
normalized_data = StandardScaler().fit_transform(X)
print(normalized_data.shape)
print(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.1,random_state=10)

X_train

model=Sequential()
model.add(Dense(38,input_shape=(38,),activation='relu'))
model.add(Dense(6,activation='softmax'))
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train,y_train, batch_size=10, epochs=30)

y_pred= model.predict(X_test)
y_test_class=np.argmax(y_test,axis=1)
y_pred_class=np.argmax(y_pred,axis=1)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test_class,y_pred_class))
print(confusion_matrix(y_test_class,y_pred_class))