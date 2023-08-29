#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Data Wrangling Lab**
# 

# Estimated time needed: **45 to 60** minutes
# 

# In this assignment you will be performing data wrangling.
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# -   Identify duplicate values in the dataset.
# 
# -   Remove duplicate values from the dataset.
# 
# -   Identify missing values in the dataset.
# 
# -   Impute the missing values in the dataset.
# 
# -   Normalize data in the dataset.
# 

# <hr>
# 

# ## Hands on Lab
# 

# Import pandas module.
# 

# In[1]:


import pandas as pd


# Load the dataset into a dataframe.
# 

# In[29]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv")


# ## Finding duplicates
# 

# In this section you will identify duplicate values in the dataset.
# 

#  Find how many duplicate rows exist in the dataframe.
# 

# In[30]:


# your code goes here

df2 = df[df.duplicated()]
# df2.shape[0]
df.head()


# ## Removing duplicates
# 

# Remove the duplicate rows from the dataframe.
# 

# In[14]:


# your code goes here
df.drop_duplicates(keep=False, inplace=True)


# Verify if duplicates were actually dropped.
# 

# In[23]:


# your code goes here
df3 = df[df.duplicated()]
df3.shape[0]


# ## Finding Missing values
# 

# Find the missing values for all columns.
# 

# In[43]:


# your code goes here
missing_data = df.isnull()
missing_data.head()
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("") 


# Find out how many rows are missing in the column 'WorkLoc'
# 

# In[27]:


# your code goes here
print(missing_data['WorkLoc'].value_counts())
    
    


# ## Imputing missing values
# 

# Find the  value counts for the column WorkLoc.
# 

# In[31]:


# your code goes here
print(df['WorkLoc'].value_counts())


# Identify the value that is most frequent (majority) in the WorkLoc column.
# 

# In[33]:


#make a note of the majority value here, for future reference
#
df['WorkLoc'].value_counts().idxmax()


# Impute (replace) all the empty rows in the column WorkLoc with the value that you have identified as majority.
# 

# In[40]:


# your code goes here
import numpy as np
df['WorkLoc'].replace(np.nan, "Office",inplace= True)


# After imputation there should ideally not be any empty rows in the WorkLoc column.
# 

# Verify if imputing was successful.
# 

# In[41]:


# your code goes here
mdata = df.isnull()
print(mdata['WorkLoc'].value_counts())


# ## Normalizing data
# 

# There are two columns in the dataset that talk about compensation.
# 
# One is "CompFreq". This column shows how often a developer is paid (Yearly, Monthly, Weekly).
# 
# The other is "CompTotal". This column talks about how much the developer is paid per Year, Month, or Week depending upon his/her "CompFreq". 
# 
# This makes it difficult to compare the total compensation of the developers.
# 
# In this section you will create a new column called 'NormalizedAnnualCompensation' which contains the 'Annual Compensation' irrespective of the 'CompFreq'.
# 
# Once this column is ready, it makes comparison of salaries easy.
# 

# <hr>
# 

# List out the various categories in the column 'CompFreq'
# 

# In[42]:


# your code goes here
df['CompFreq'].value_counts()


# Create a new column named 'NormalizedAnnualCompensation'. Use the hint given below if needed.
# 

# Double click to see the **Hint**.
# 
# <!--
# 
# Use the below logic to arrive at the values for the column NormalizedAnnualCompensation.
# 
# If the CompFreq is Yearly then use the exising value in CompTotal
# If the CompFreq is Monthly then multiply the value in CompTotal with 12 (months in an year)
# If the CompFreq is Weekly then multiply the value in CompTotal with 52 (weeks in an year)
# 
# -->
# 

# In[46]:


# your code goes here
normalAC = []
for i in range(len(df)):
    if df['CompFreq'].iloc[i] == "Weekly":
        normalAC.append(df['CompTotal'].iloc[i]*52)
    elif df['CompFreq'].iloc[i] == "Monthly":
        normalAC.append(df['CompTotal'].iloc[i]*12)
    else:
        normalAC.append(df['CompTotal'].iloc[i])
df['NormalizedAnnualCompensation']= normalAC
df.head()


# ## Authors
# 

# Ramesh Sannareddy
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
# 

#  Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
