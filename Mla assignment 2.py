#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
import re

# set the graphs to show in the jupyter notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# set seabor graphs to a better style
sns.set(style="ticks")


# In[2]:


raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']                        
            }


# In[3]:


# Assign it to a object called pokemon and it should be a pandas DataFrame

pokemon = pd.Series(raw_data)
pokemon


# In[4]:


# 4. If the DataFrame columns are in alphabetical order, change the order of the columns as name, type, hp, evolution, pokedex

pokemon1 = pd.DataFrame.from_dict(raw_data)
pokemon1 = pokemon1[["name", "type", "hp", "evolution", "pokedex"]]
pokemon1


# In[5]:


# 5. Add another column called place, and insert places (lakes, parks, hills, forest etc) of your choice.

place = ["Hills","Volcano","Lakes","park"]
pokemon1["Place"] = place
pokemon1


# In[6]:


# 6. Display the data type of each column

pokemon1.dtypes


# In[7]:


# 7. Display the info of dataframe

pokemon1.info()


# In[8]:


# 8. Import the dataset wine.txt from the folder and assign it to a object called wine
# Please note that the original data text file doesn't contain any header. Please ensure that when you import the data, you should use a suitable argument so as to avoid data getting imported as header.

import pandas as pd
file_path = "C:\\Users\\Tousif M Tamboli\\Downloads\\ASSIGNMENT 2 SYDS\\ASSIGNMENT 2 SYDS\\wine.txt"
wine = pd.read_csv(file_path, header=None)
wine.head()


# In[9]:


# 9. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns

columns_to_delete = [0, 3, 6, 8, 10, 12, 13]
wine = wine.drop(columns=columns_to_delete, axis=1)
wine.head()


# In[10]:


### 10. Assign the columns as below:
# The attributes are (dontated by Riccardo Leardi, riclea '@' anchem.unige.it):  
# 1) alcohol  
# 2) malic_acid  
# 3) alcalinity_of_ash  
# 4) magnesium  
# 5) flavanoids  
# 6) proanthocyanins  
# 7) hue 


new_column_names = [
    'alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue'
]
wine.columns = new_column_names
wine.head()


# In[11]:


# 11. Set the values of the first 3 values from alcohol column as NaN

wine.iloc[:3, wine.columns.get_loc('alcohol')] = np.nan
wine.head()


# In[12]:


# 12. Now set the value of the rows 3 and 4 of magnesium as NaN

wine.iloc[2:4, wine.columns.get_loc('magnesium')] = np.nan
wine.head()


# In[13]:


wine.alcohol.fillna(10, inplace = True)

wine.magnesium.fillna(100, inplace = True)

wine.head()


# In[14]:


wine.isnull().sum()


# In[15]:


random = np.random.randint(10, size = 10)
random


# In[16]:


import random
import numpy as np

# Get the index of a random row
random_index = random.choice(wine.index)

# Set the value in the 'alcohol' column of the randomly selected row to NaN
wine.at[random_index, 'alcohol'] = np.nan

# Display the modified DataFrame
wine.head(10)


# In[17]:


# How many missing values do we have?

wine.isnull().sum()


# In[18]:


# Print only the non-null values in alcohol

mask = wine.alcohol.notnull()
mask


# In[19]:


# Delete the rows that contain missing values

wine = wine.dropna(axis = 0, how = "any")
wine.head()


# In[20]:


# Reset the index, so it starts with 0 again

wine = wine.reset_index(drop = True)
wine.head()

