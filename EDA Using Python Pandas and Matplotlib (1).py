#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Loading csv file to perform data analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\91705\Downloads\matches.csv")


# In[2]:


#printing first 10 rows of dataset to help us in understanding the dataset
df.head(10)


# In[4]:


#checking Datatypes

df.dtypes


# In[5]:


## get the number of rows and columns from dataset

df.shape


# In[6]:


# get the count of null values from each column in the dataset

df.isnull().sum()


# In[7]:


# we have 636 rows and 18 columns from the above result we can see that 'umpire3' column is entirely null so we dont need such column 

new_df = df.drop(['umpire3'], axis = 1)
new_df


# In[8]:


# Display summary statistics 

new_df.describe()


# In[9]:


#sorting the dataframe based on season in ascending manner

new_df.sort_values(by=['season'],ascending=True)[:20]


# In[10]:


# Getting most match winning team

new_df['winner'].value_counts()


# In[11]:


# plotting the top 5 teams who have won most number of matches

plt.figure(figsize=(7,5))
plt.bar(list(new_df['winner'].value_counts()[0:5].keys()),list(new_df['winner'].value_counts()[0:5]),color=['royalblue','yellow','purple','firebrick','crimson'],edgecolor='black')
plt.xticks(rotation=45)
plt.show()


# In[12]:


#Getting the top 10 players with most man of the match awards
new_df['player_of_match'].value_counts()[0:10]


# In[13]:


plt.figure(figsize=(9,5))
c = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:cyan','tab:pink','tab:olive','tab:gray']
plt.bar(list(new_df['player_of_match'].value_counts()[0:10].keys()),list(new_df['player_of_match'].value_counts()[0:10]),color = c,edgecolor='black')
plt.xticks(rotation=45)
plt.show()


# In[14]:


#Finding out which team won toss most of the time

new_df['toss_winner'].value_counts()


# In[15]:


# getting first 10 teams who won batting first

first_bat=new_df[new_df['win_by_runs']!=0]
first_bat.head(10)


# In[16]:


#Finding out how many match a team won after choosing to bat first and plotting graph of first 5 team

first_bat['winner'].value_counts()
plt.figure(figsize=(7,5))
c1 = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple']
plt.bar(list(first_bat['winner'].value_counts()[0:5].keys()),list(first_bat['winner'].value_counts()[0:5]),color=c1,edgecolor = 'k')
plt.xticks(rotation=45)
plt.ylabel('Number Of Wins',fontsize=14)
plt.xlabel('Team',fontsize=14)
plt.show()


# In[17]:


# Making a histogram to show that the team who chose to bat first and by how many runs they won over the other team

yt = np.arange(10,101,10)
plt.figure(figsize=(10,7))
plt.hist(first_bat['win_by_runs'],edgecolor='k')
plt.yticks(yt)
plt.title("Distribution of Runs" ,fontsize = 14)
plt.xlabel("Runs",fontsize = 14)
plt.show()


# In[18]:


#Making a pie chart of first 10 teams who chose to bat first and won the match

plt.figure(figsize=(7,7))
explode1 = [0.2,0.1,0,0,0,0,0,0,0,0]
plt.pie(list(first_bat['winner'].value_counts()[:10]),labels=list(first_bat['winner'].value_counts()[:10].keys()),autopct='%0.2f%%',explode=explode1,startangle = 90,counterclock=False)
plt.show()


# In[19]:


# getting those teams who won after batting at second place

second_bat=new_df[new_df['win_by_wickets']!=0]

# histogram for frequency of wins w.r.t number of wickets
plt.figure(figsize=(10,7))
plt.hist(second_bat['win_by_wickets'],bins=4,edgecolor='k')
plt.show()


# In[20]:


#Making a bar plot for top-5 teams with most wins after batting second

plt.figure(figsize=(7,7))
plt.bar(list(second_bat['winner'].value_counts()[0:5].keys()),list(second_bat['winner'].value_counts()[0:5]),color=['tab:pink','tab:olive','tab:blue','tab:orange','tab:gray'])
plt.xticks(rotation=45)
plt.ylabel('Number Of Wins',fontsize=14)
plt.xlabel('Team',fontsize=14)
plt.show()


# In[21]:


#Making a pie chart of first 10 teams who chose to bat second and won the match
second_bat['winner'].value_counts()
plt.figure(figsize=(7,7))
plt.pie(list(second_bat['winner'].value_counts()[:10]) , labels=list(second_bat['winner'].value_counts()[:10].keys()),autopct='%0.2f%%',explode=explode1,startangle = 90,counterclock=False)
plt.title('Pie Chart',fontsize=14)
plt.show()


# In[22]:


##Looking at the number of matches played each season
new_df['season'].value_counts()


# In[23]:


# plotting number of matches played from year 2008 to 2018

plt.figure(figsize=(10,5))
c3 = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:cyan','tab:pink','tab:olive','tab:gray']
plt.bar(list(new_df['season'].value_counts()[0:10].keys()),list(new_df['season'].value_counts()[0:10]),color=c3,edgecolor = 'k')
plt.grid()
plt.xticks(rotation=45)
plt.ylabel('Number Of Matches Played',fontsize=14)
plt.xlabel('years',fontsize=14)

plt.show()


# In[24]:


new_df['city'].value_counts()

# name of the cities where most matches were played

plt.figure(figsize=(10,5))
c3 = ['tab:green','tab:orange','tab:blue','tab:red','tab:purple','tab:brown','tab:cyan','tab:pink','tab:olive','tab:gray']
plt.bar(list(new_df['city'].value_counts()[0:10].keys()),list(new_df['city'].value_counts()[0:10]),color=c3,edgecolor = 'k')
plt.grid()
plt.xticks(rotation=45)
plt.ylabel('Number Of Matches Played',fontsize=14)
plt.xlabel('city',fontsize=14)

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




