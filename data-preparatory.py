#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd

df_new2 = pd.read_csv('census_11-2.csv')
df_new2


# In[74]:


df_new2.info()


# In[30]:


df_new['House Number'].unique()


# In[29]:


df_new['Street'].unique()


# In[28]:


df_new['First Name'].unique()


# In[27]:


df_new['Surname'].unique()


# In[85]:


df_new2['Age'].unique()


# In[31]:


df_new['Relationship to Head of House'].unique()


# In[9]:


df_new['Marital Status'].unique()


# In[10]:


df_new['Gender'].unique()


# In[11]:


df_new['Occupation'].unique()


# In[12]:


df_new['Infirmity'].unique()


# In[13]:


df_new['Religion'].unique()


# In[32]:


df_new.isnull().sum()


# In[59]:


import numpy as np

df_new.replace(np.nan, "0", inplace=True)
df_new.replace(" ", np.nan, inplace=True)


# In[89]:


df_new2['Age'].unique()


# In[94]:



df_new2["Age"].replace({"Four": "4", "Fifty Two": "52", "Seventeen": "17", " ": "29"}, inplace=True)

df_new2['Age'].unique()


# In[98]:


import numpy as np

age_list = df_new2['Age']
new_age_list = []

for age in age_list:
    try:
        new_age_list.append(int(age))
    except:
        new_age_list.append(int(float(age)))
print(new_age_list)         


# In[100]:


df_new2['Age'] = new_age_list
df_new2


# In[95]:


df_new2['Age'].isnull().sum()


# In[101]:


empty_age = df_new2.loc[df_new2['Age'] == 40] # Locate the row that has empty age value


# In[115]:


# print(empty_age) 
df_new2['Age'].unique()


# In[104]:


df_new2['Religion'].unique()


# In[111]:


empty_religion = df_new2.loc[df_new2['Religion'] == 'Undecided']


# In[112]:


print(empty_religion)


# In[117]:


# df_new2["Age"].replace({-1: 1}, inplace=True)
# df_new2["Age"].unique()


# In[118]:


df_new2["Religion"].replace({"NaN": "N/A"}, inplace=True)


# In[119]:


df_new2


# In[120]:


df_new2.replace(np.nan, "0", inplace=True)


# In[121]:


df_new2


# In[122]:


df_new2["Religion"].replace({"0": "N/A"}, inplace=True)


# In[123]:


df_new2


# In[124]:


df_new2["Religion"].unique()


# In[130]:


babies_count = 0
for age in df_new2['Age']:
    if age == 0:
        babies_count += 1
print(babies_count)


# In[131]:


women_in_child_bearing_age_count = 0
for age in df_new2['Age']:
    if age >= 25 and age <= 29:
        women_in_child_bearing_age_count += 1
print(women_in_child_bearing_age_count)


# In[133]:


birth_rate = 73 / 545
print(birth_rate)


# In[134]:


birth_rate_per_100000 = birth_rate * 100000


# In[135]:


print(birth_rate_per_100000)


# In[ ]:




