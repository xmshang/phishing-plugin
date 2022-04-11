
# coding: utf-8

# In[1]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
import numpy as np
import json
import dump


# In[2]:

path = 'd:\\NYIT\\project870\\phishing-plugin\\python\\dataset\\'
pathJson = 'd:\\NYIT\\project870\\phishing-plugin\\static\\'

X_train = np.load(path + 'X_train.npy')
y_train = np.load(path + 'y_train.npy')
print('X_train:{0}, y_train:{1}'.format(X_train.shape, y_train.shape))


# In[3]:


clf = RandomForestClassifier()
print('Cross Validation Score: {0}'.format(np.mean(cross_val_score(clf, X_train, y_train, cv=10))))


# In[4]:


clf.fit(X_train, y_train)


# In[5]:


X_test = np.load(path + 'X_test.npy')
y_test = np.load(path + 'y_test.npy')


# In[6]:


pred = clf.predict(X_test)
print('Accuracy: {}'.format(accuracy_score(y_test, pred)))


# In[7]:


#print(forest_to_json(clf))
json.dump(dump.forest_to_json(clf), open(pathJson + 'classifier.json', 'w'))


# How do you use Randomforestclassifier in Sklearn?
# It works in four steps:
# Select random samples from a given dataset.
# Construct a decision tree for each sample and get a prediction result from each decision tree.
# Perform a vote for each predicted result.
# Select the prediction result with the most votes as the final prediction.