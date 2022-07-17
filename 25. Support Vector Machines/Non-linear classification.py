#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from mpl_toolkits.mplot3d import Axes3D


# In[2]:


X,Y = make_circles(n_samples = 500,noise = 0.05)
print(X.shape,Y.shape)


# In[3]:


plt.scatter(X[:,0],X[:,1],c = Y)
plt.show()


# In[4]:


def phi(X):
    '''Non linear transformation'''
    X1 = X[:,0]
    X2 = X[:,1]
    X3 = X1**2 + X2**2
    
    X_ = np.zeros((X.shape[0],3))
    print(X_.shape)
    
    X_[:,:-1] = X
    X_[:,-1] = X3
    
    return X_


# In[5]:


X_ = phi(X)


# In[6]:


print(X_[:3,:])


# In[7]:


def plot3d(X,show=True):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111,projection='3d')
    X1 = X[:,0]
    X2 = X[:,1]
    X3 = X[:,2]
    
    ax.scatter(X1,X2,X3,zdir='z',s=20,c=Y,depthshade=True)
    
    if(show==True):
        plt.show()
    return ax


# In[8]:


ax = plot3d(X_)


# ### Logistic Classifier

# In[9]:


from sklearn.linear_model import LogisticRegression


# In[10]:


from sklearn.model_selection import cross_val_score


# In[11]:


lr = LogisticRegression()


# In[12]:


acc = cross_val_score(lr,X,Y,cv = 5).mean()
print("Accuracy of X(2D) is %.4f"%(acc*100))


# ### Logistic Classifier on Higher Dimension Space

# In[13]:


acc = cross_val_score(lr,X_,Y,cv = 5).mean()
print("Accuracy of X(2D) is %.4f"%(acc*100))


# ### Visualise the Decision Surface

# In[14]:


lr.fit(X_,Y)


# In[15]:


lr.coef_


# In[16]:


lr.intercept_


# In[17]:


xx,yy = np.meshgrid(range(-2,2),range(-2,2))
print(xx)
print(yy)


# In[18]:


wts = lr.coef_
bias = lr.intercept_


# In[19]:


z = -(wts[0,0]*xx + wts[0,1]*yy + bias)/wts[0,2]
print(z)


# In[20]:


ax = plot3d(X_,False)
ax.plot_surface(xx,yy,z,alpha=0.2)
plt.show()


# In[ ]:




