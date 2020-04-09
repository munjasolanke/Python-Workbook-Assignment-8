#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Python Workbook Assignment 8-3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
location = "C:\MUNJA_DATA\Courses\Data Visualization\learn-data-analysis-w-python-master\datasets\gradedata.csv"
df = pd.read_csv(location)
df.head()


# In[62]:


plt.scatter(df.hours, df.grade)
plt.show()


# In[ ]:


#By looking above scatter plot, we can see there is specific pattern for scatter plot.

