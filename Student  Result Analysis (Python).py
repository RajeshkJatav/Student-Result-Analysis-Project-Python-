#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[13]:


df= pd.read_csv(r'C:\Users\RAJESH KUMAR\Downloads\Expanded_data_with_more_features.csv', encoding ='unicode_escape')


# In[14]:


df.head()


# In[15]:


df.describe()


# In[20]:


df.info()


# In[50]:


df.isnull().sum()


# In[51]:


df = df.drop("Unnamed: 0", axis =1)


# In[54]:


# change weekly study hours columns 
df["WklyStudyHours"] =df["WklyStudyHours"].str.replace("05-Oct", "5-10")


# In[83]:


#Gender Distribution
plt.figure(figsize=(5,5))
ax = sns.countplot(data=df , x ='Gender')
plt.title("Gender Distribution")
ax.bar_label(ax.containers[0])

plt.show()


# In[ ]:


#from the above chart we have analyzed that the number of females in the data is more then number of males 


# In[77]:


gb = df.groupby("ParentEduc").agg({"MathScore":"mean", "ReadingScore":"mean","WritingScore":"mean"})
print(gb)


# In[84]:


plt.figure(figsize=(5,5))
sns.heatmap(gb , annot= True)
plt.title("Relationship between Parent's Eduction & Student's Score")
plt.show()


# In[ ]:


# From the above graph we can conclude that the education of parents have good impact on their childern's.


# In[86]:


#On the basis of Marital Status
gb = df.groupby("ParentMaritalStatus").agg({"MathScore":"mean", "ReadingScore":"mean","WritingScore":"mean"})
print(gb)


# In[87]:


plt.figure(figsize=(5,5))
sns.heatmap(gb , annot= True)
plt.title("Relationship between Parent's Marital Status & Student's Score")
plt.show()


# In[ ]:


# From the above graph we can conclude that there Parents Marital Staus have no/negligible impact on their childern's.


# In[89]:


sns.boxplot(data=df, x= "MathScore")
plt.show()


# In[90]:


sns.boxplot(data=df, x= "ReadingScore")
plt.show()


# In[93]:


sns.boxplot(data=df, x= "WritingScore")
plt.show()


# In[98]:


print(df['EthnicGroup'].unique())


# # Distribution of Ethnic goups

# In[108]:


# Count the occurrences of each ethnic group
groupA = df.loc[df['EthnicGroup'] == "group A"].shape[0]
groupB = df.loc[df['EthnicGroup'] == "group B"].shape[0]
groupC = df.loc[df['EthnicGroup'] == "group C"].shape[0]
groupD = df.loc[df['EthnicGroup'] == "group D"].shape[0]
groupE = df.loc[df['EthnicGroup'] == "group E"].shape[0]

# Create lists for plotting
ethnic_groups = ["group A", "group B", "group C", "group D", "group E"]
group_counts = [groupA, groupB, groupC, groupD, groupE]

# Plotting a pie chart
plt.pie(group_counts, labels=ethnic_groups, autopct="%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[115]:


ax= sns.countplot(data = df ,x = 'EthnicGroup')
ax.bar_label(ax.containers[0])

