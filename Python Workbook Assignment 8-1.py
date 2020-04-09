#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Workbook Assignment 8-1
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:\MUNJA_DATA\Courses\Data Visualization\learn-data-analysis-w-python-master\datasets\gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[5]:


df.hist(column="age", by="gender")


# In[ ]:




