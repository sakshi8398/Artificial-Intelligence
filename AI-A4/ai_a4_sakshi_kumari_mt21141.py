
from google.colab import drive
drive.mount('/content/drive')

# Import required libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
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

dataset[dataset.duplicated()]

dataset['Suggested Job Role'].value_counts()

print(dataset.isna().sum())

data = dataset.iloc[:,:-1].values
label = dataset.iloc[:,-1].values
len(data[0])

dataset.iloc[:,14:38]

dataset.iloc[:,:14]

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder = LabelEncoder()

for i in range(14,38):
    data[:,i] = labelencoder.fit_transform(data[:,i])
data[:5]

data[:5,14:]

from sklearn.preprocessing import Normalizer

data1=data[:,:14]

normalized_data = Normalizer().fit_transform(data1)
print(normalized_data.shape)

normalized_data

data2=data[:,14:]
data2.shape

df = np.append(normalized_data,data2,axis=1)

df.shape

X1 = pd.DataFrame(df,columns=['Acedamic percentage in Operating Systems', 'percentage in Algorithms',
       'Percentage in Programming Concepts',
       'Percentage in Software Engineering', 'Percentage in Computer Networks',
       'Percentage in Electronics Subjects',
       'Percentage in Computer Architecture', 'Percentage in Mathematics',
       'Percentage in Communication skills', 'Hours working per day',
       'Logical quotient rating', 'hackathons', 'coding skills rating',
       'public speaking points', 'can work long time before system?',
       'self-learning capability?', 'Extra-courses did', 'certifications',
       'workshops', 'talenttests taken?', 'olympiads',
       'reading and writing skills', 'memory capability score',
       'Interested subjects', 'interested career area ', 'Job/Higher Studies?',
       'Type of company want to settle in?',
       'Taken inputs from seniors or elders', 'interested in games',
       'Interested Type of Books', 'Salary Range Expected',
       'In a Realtionship?', 'Gentle or Tuff behaviour?',
       'Management or Technical', 'Salary/work', 'hard/smart worker',
       'worked in teams ever?', 'Introvert'])

X1.head()

label = labelencoder.fit_transform(label)
print(len(label))

y=pd.DataFrame(label,columns=["Suggested Job Role"])
y.head()

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing 
from sklearn.metrics import accuracy_score

X_train,X_test,y_train,y_test=train_test_split(X1,y,test_size=0.1,random_state=10)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

from sklearn.metrics import confusion_matrix,accuracy_score

y_pred = clf.predict(X_test)

cm = confusion_matrix(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)

print("confusion matrics=")
print(cm)
print("accuracy=",accuracy*100)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))

from sklearn import svm

clf = svm.SVC()
clf.fit(X_train, y_train)

svm_y_pred = clf.predict(X_test)

svm_cm = confusion_matrix(y_test,svm_y_pred)
svm_accuracy = accuracy_score(y_test,svm_y_pred)

print("confusion matrics=",svm_cm)
print("  ")
print("accuracy=",svm_accuracy*100)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,svm_y_pred))
print(confusion_matrix(y_test,svm_y_pred))

from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier(learning_rate=1.75,n_estimators=300)
ada.fit(X_train, y_train)
y_ada = ada.predict(X_test)
ada_cm = confusion_matrix(y_test,y_ada)
ada_accuracy = accuracy_score(y_test,y_ada)

print("confusion matrics=",ada_cm)
print("  ")
print("accuracy=",ada_accuracy*100)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,y_ada))
print(confusion_matrix(y_test,y_ada))

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(random_state=1, max_iter=300).fit(X_train, y_train)
y_mlp=clf.predict(X_test)
mlp_cm = confusion_matrix(y_test,y_mlp)
mlp_accuracy = accuracy_score(y_test,y_mlp)

print("confusion matrics=",mlp_cm)
print("  ")
print("accuracy=",mlp_accuracy*100)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,y_mlp))
print(confusion_matrix(y_test,y_mlp))