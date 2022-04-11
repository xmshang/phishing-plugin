
# coding: utf-8

# In[16]:

import arff
import numpy as np
import json
from sklearn.model_selection import train_test_split, KFold


# In[17]:

path = 'd:\\NYIT\\project870\\phishing-plugin\\python\\dataset\\'
pathJson = 'd:\\NYIT\\project870\\phishing-plugin\\static\\'

# dataset = arff.load(open('dataset.arff', 'r'))
dataset = arff.load(open(path + 'dataset.arff', 'r'))
data = np.array(dataset['data'])


# In[18]:


print('The dataset has {0} datapoints with {1} features'.format(data.shape[0], data.shape[1]-1))
print('Features: {0}'.format([feature[0] for feature in dataset['attributes']]))


# In[19]:


data = data[:, [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 22, 30]]


# In[20]:


X, y = data[:, :-1], data[:, -1]
y.reshape(y.shape[0])
print('Before spliting')
print('X:{0}, y:{1}'.format(X.shape, y.shape))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
print('After spliting')
print('X_train:{0}, y_train:{1}, X_test:{2}, y_test:{3}'.format(X_train.shape, y_train.shape, X_test.shape, y_test.shape))


# In[21]:


np.save(path + 'X_train.npy', X_train)
np.save(path + 'X_test.npy', X_test)
np.save(path + 'y_train.npy', y_train)
np.save(path + 'y_test.npy', y_test)
print('Saved!')


# In[24]:


test_data = dict()
test_data['X_test'] = X_test.tolist()
test_data['y_test'] = y_test.tolist()
# with open('../../static/testdata.json', 'w') as tdfile:
with open(pathJson + 'testdata.json', 'w') as tdfile:
    json.dump(test_data, tdfile)
    print('Test Data written to testdata.json')



# train_test_split
# train_test_split()函数是用来随机划分样本数据为训练集和测试集的，当然也可以人为的切片划分。
# 优点：随机客观的划分数据，减少人为因素

# X_train, X_test, y_train, y_test = train_test_split(train_data, train_target, test_size=0.1, random_state=0)
# 参数解释：
# train_data：待划分样本数据
# train_target：待划分样本数据的结果（标签）
# test_size：测试数据占样本数据的比例，若整数则样本数量
# random_state：设置随机数种子，保证每次都是同一个随机数。若为0或不填，则每次得到数据都不一样
