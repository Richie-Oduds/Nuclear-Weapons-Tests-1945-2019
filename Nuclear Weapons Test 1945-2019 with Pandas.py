#!/usr/bin/env python
# coding: utf-8

# ### ANALYSIS ON NUCLEAR WEAPONS TESTS FROM 1945 TO 2019
# 
# INTRODUCTION
# 
#  According to wiikipedia Nuclear weapons tests are experiments carried out to determine nuclear weapons' effectiveness, yield, and explosive capability. Testing nuclear weapons offers practical information about how the weapons function, how detonations are affected by different conditions, and how personnel, structures, and equipment are affected when subjected to nuclear explosions. However, nuclear testing has often been used as an indicator of scientific and military strength. Many tests have been overtly political in their intention; most nuclear weapons states publicly declared their nuclear status through a nuclear test. 
#  
#  ABOUT THE DATA
#  
#   This data was collected from https://www.kaggle.com,  The data shows the year of each nuclear test by their country. The dataset is reliable, original and comprehensive. The source has their own licence over the dataset. Besides that, the dataset doesn't have any personal information. All the files have consistent columns and each column has the correct type of data. Finally, It would be good to have some updated information about the nuclear weapons tests.

# In[1]:


# Nuclear Weapons Tests Analysis with Pandas & Plotly
# We will be using the following Python Libraries: 
# • Pandas
# • Matplotlib
# • Pandas Profiling Report
# • AutoViz
# • Plotly


# In[2]:


# We will cover the following chart types:
# • Histogram
# • Area Chart
# • Pie Chart
# • Bar Charts


# ### CONTENTS
# - [x] Libraries imports 
# - [x] Loading of dataset 
# - [x] Dataset exploration 
# - [x] Profiling report
# - [x] AutoViz report
# - [x] Data manipulation
# - [x] Data visualization
# - [x] Conclusion

# ### IMPORT OUR LIBRARIES

# In[3]:


# Imports:
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
from pandas_profiling import ProfileReport
from autoviz.AutoViz_Class import AutoViz_Class


# LOADING DATASET

# In[4]:


# Now we are going to load our dataset
df = pd.read_csv("nuclear.csv")


# In[5]:


df.head()


# ### DATASET EXPLORATION
# In this part I will be exploring the dataset

# In[6]:


# Basic info about the DataFrame
df.info()


# In[7]:


# Describe methed
df.describe()


# In[8]:


# Get a view of a unique value in column e.g. 'country_name'
df['country_name'].unique()


# In[9]:


# Check for null values
df.isnull()


# In[10]:


# NoN count for each column
df.isnull().sum()


# ### PANDAS PROFILING REPORT
# I will be using pandas-profiling to generate profile reports from my data [nuclear.csv]

# In[11]:


# AUTOMATED REPORTS
# Generate pandas profiling report
profile = ProfileReport(df, title = "nuclear.csv Profiling Report")

# To view in Notebook
profile.to_notebook_iframe()


# ### AutoViz REPORT 
# Using AutoViz to perform automatic visualization report on my dataset 

# In[12]:


# AutoViz report
# Here we would show the AutoViz report 
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('classic')
AV = AutoViz_Class()
df_autoviz = AV.AutoViz('nuclear.csv')


# ### DATA MANIPULATION
# Carrying out data manipulation on my dataset in order to gain more insights from my dataset.

# First, we find country with the highest and lowest nuclear weapons tests in a year

# In[13]:


# Country with the highest Nuclear weapons tests in a year
df.nlargest(1,'nuclear_weapons_tests')


# In[14]:


# Country with the smallest Nuclear testsin a year
df.nsmallest(1, 'nuclear_weapons_tests')


# Finding total sum of nuclear weapons tests per country and grouping them by country names

# In[15]:


# Find the total Nuclear weapon tests per country since 1945 to 2019
total =  df.groupby('country_name', as_index=False)['nuclear_weapons_tests'].sum()
total.head()


# In[16]:


total.tail()


#  ### DATA VISUALIZATION
#  Visualizing my data 

# #### CHART 1: HISTOGRAM SHOWING TOTAL NUCLEAR WEAPONS TEST PER COUNTRY FROM 1945-2019
# Creating a histogram chart to show the total nuclear weapons test per country from 1945 to 2019

# In[17]:


# Create Chart
template_style = 'plotly_white'
fig = px.histogram(total,
                   x ='country_name',
                   y = 'nuclear_weapons_tests',
                   title = '<b>Total Nuclear Weapon Test Per Country 1945-2019</b>',
                   template = template_style,
                   width=800, height=400)
    
# Plot chart
fig.show()


# #### CHART 2: USING AREA CHART TO CHECK FOR TRENDS
# Checking for trends in nuclear weapons tests from 1945-2019 using Area Chart

# In[18]:


# Create Chart
fig = px.area(df,
             x = 'year',
             y = 'nuclear_weapons_tests',
             color = 'country_name',
             template = template_style,
              title = '<b>Area Chart Showing Trends Nuclear Tests</b>',
              width=800, height=400)


# Display Plot
fig.show()


# #### CHART 3: PIE CHART SHOWING PERCENTAGE OF WHOLE
# I would create a pie chart showing the percentage each country has used in wuclear Weapons testing from 1945-2019

# In[19]:



# Create Chart
fig = px.pie(total, 'country_name',
             'nuclear_weapons_tests',
             color = 'nuclear_weapons_tests',
              title = '<b>Pie Chart Nuclear Tests</b>',
             width=800, height=400)


# Display Plot
fig.show()


# #### CHART 4: BAR CHART SHOWING AMOUNT OF YEARLY NUCLEAR WEAPONS TESTS PER EACH COUNTRY

# In[20]:


# Create a chart
template_style = 'plotly_white'
fig = px.bar(df,
             x = 'year',
             y = 'nuclear_weapons_tests',
             color = 'country_name',
             color_continuous_scale = ['green', 'yellow', 'red'],
             title = '<b>Yearly Nuclear Weapons Tests Per Country 1945-2019</b>',
             template = template_style,)
# Display plot
fig.show()


# #### CHART 5: SCATTER PLOT SHOWING LINEAR CORRELATION BETWEEN YEAR/NUCLEAR WEAPONS TESTS
# Is there any correlation between Year/Nuclear Weapons Tests & country [Scatter Plot]

# In[21]:



fig = px.scatter(df,
             x = 'year',
             y = 'nuclear_weapons_tests',
             color = 'country_name',
             width=800, height=400,
                  template = template_style,
            title = '<b>Scatterplot Year/Nuclear Weapons Test</b>')

fig.show()


# ### CONCLUSION

# #### In this conclusion I would talk about the noticed trends in my insights
# 
# Since the end of world war 2, various nuclear weapons tests has been carried out by some countries, which is the basis of my analysis and insights. This analysis gave me some important insights on how countries has been testing nuclear weapons for years. What I found out was that;
# 
# * The United States carried out the highest nuclear weapons test from 1945 to 2019 with a total of 1030 tests.
# * Russia had the second highest nuclear weapons tests from 1945 to 2019 with a total of 715 tests.
# * Pakistan had the lowest nuclear weapons test with a total of 2 tests.
# * The United States had the highest nuclear weapons tests in a calendar year with a total of 96 tests in 1962.
# * China had no nuclear weapons tests in 1945 but had a total of 45 nuclear weapons tests since 1945 to 2019.
# * The United States has tested about 50% of the world's nuclear weapons test from 1945 to 2019.
# * Within 1955 to 1956 the United States has carried out about 36 nuclear weapons tests with each of the year having 18 tests each.
# * The United States had a consistent nuclear weapons tests from 1971 to 1992, making it 21 years of consistent nuclear weapons testing.
# * France also had a consistent nuclear weapons testing from 1970 to 1991 making it 21 years of consistent nuclear weapons testing.
# * Russia's consistent nuclear weapons testing occurred between 1964 to 1985 making it also 21 years of consistent nuclear weapons testing.
# * The U.S, Russia and France had 21 years each of consistent nuclear weapons testing.
# * Russia has tested 34.7% of the world's nuclear weapons tests, while France has tested 10.2% of the world's nuclear weapons tests, making them one of the top 3 nuclear weapons testers.
# * This report shows that the United states, Russia and France has carried out 94.9% of the world's nuclear weapons tests from 1945 to 2019.
# 

# In[ ]:




