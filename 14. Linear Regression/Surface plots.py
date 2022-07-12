#!/usr/bin/env python
# coding: utf-8

# ### Surface Plots | Data Visualisation
# Surface plots are used to
# ```
# - Visualise Loss Functions in Machine Learning and Deep Learning
# - Visualise State or State Value Functions in Reinforcement Learning
# ```

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[5]:


# a = np.array([1,2,3])
# b = np.array([4,5,6,7])

a = np.arange(-1,1,0.02)
b = a

a,b = np.meshgrid(a,b)
print(a)
print(b)


# In[12]:


fig = plt.figure(figsize = (10,10))
axes = plt.axes(projection = '3d') # plt.axes() is used in place of fig.gca()
axes.plot_surface(a,b,a**2+b**2,cmap = "rainbow")
plt.show()


# In[13]:


fig = plt.figure(figsize = (10,10))
axes = plt.axes(projection = '3d')
axes.contour(a,b,a**2+b**2,cmap = "rainbow")
plt.show()


# In[ ]:




