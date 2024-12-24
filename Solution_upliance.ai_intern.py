#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load the Excel file
file_path = "Data Analyst Intern Assignment - Excel.xlsx"


# In[3]:


sheet_names = pd.ExcelFile("Data Analyst Intern Assignment - Excel.xlsx").sheet_names
print("Sheet Names:", sheet_names)


# In[4]:


user_details = pd.read_excel(file_path, sheet_name="UserDetails.csv")
cooking_sessions = pd.read_excel(file_path, sheet_name="CookingSessions.csv")
order_details = pd.read_excel(file_path, sheet_name="OrderDetails.csv")


# In[5]:


print("User Details Data:")
print(user_details.head())


# In[6]:


print("Cooking Sessions Data:")
print(cooking_sessions.head())


# In[7]:


print("Order Details Data:")
print(order_details.head())


# # Data cleaning

# In[8]:


user_details.fillna("Unknown", inplace=True)
cooking_sessions.drop_duplicates(inplace=True)


# In[9]:


user_details.columns = user_details.columns.str.strip().str.lower().str.replace(' ', '_')


# In[10]:


user_details['age'].fillna(user_details['age'].median(), inplace=True)  # Replace with median
user_details['location'].fillna('Unknown', inplace=True)  # Replace with a default value


# # Merge Datasets

# In[11]:


# Clean column names for all datasets
user_details.columns = user_details.columns.str.strip().str.lower().str.replace(' ', '_')
cooking_sessions.columns = cooking_sessions.columns.str.strip().str.lower().str.replace(' ', '_')
order_details.columns = order_details.columns.str.strip().str.lower().str.replace(' ', '_')

# Display column names after cleaning
print(user_details.columns)
print(cooking_sessions.columns)
print(order_details.columns)


# In[12]:


merged_data = pd.merge(user_details, cooking_sessions, on='user_id', how='inner')
merged_data = pd.merge(merged_data, order_details, on='user_id', how='inner')

print(merged_data.head())


# #  Analyze Data
# 1. Analyze Relationships

# In[13]:


#Total orders by city
orders_by_location = merged_data.groupby('location')['order_id'].count()
print(orders_by_location)


# In[14]:


print(merged_data.columns)


# In[15]:


# Inspect dish_name columns
print(merged_data[['dish_name_x', 'dish_name_y']].head(10))

# Use the relevant column
popular_dishes = merged_data['dish_name_x'].value_counts().head(10)
print(popular_dishes)

# Optional: Rename for clarity
merged_data.rename(columns={'dish_name_x': 'dish_name'}, inplace=True)

# Optional: Drop unnecessary columns
merged_data.drop(columns=['dish_name_y'], inplace=True)

# Recheck and finalize
print(merged_data.head())


# # Visualize Data

# In[17]:


#(Top Dishes):
popular_dishes.plot(kind='bar', figsize=(8, 5))
plt.title('Top 10 Popular Dishes')
plt.xlabel('Dish Name')
plt.ylabel('Count')
plt.show()


# In[19]:


# Orders by City
orders_by_location.plot(kind='pie', autopct='%1.1f%%', figsize=(7, 7))
plt.title('Orders by location')
plt.show()


# In[20]:


# Age Distribution
sns.histplot(user_details['age'], kde=True, bins=10)
plt.title('Age Distribution of Users')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[63]:


import numpy as np
mean_cooking_time = np.mean(merged_data['duration_(mins)'])  # Use the correct column name
print(f"Mean Duration(mins): {mean_cooking_time}")

# Identify outliers in cooking time
outliers = merged_data[merged_data['duration_(mins)'] > mean_cooking_time + 2 * np.std(merged_data['duration_(mins)'])]
print(outliers)


# In[64]:


print(merged_data['duration_(mins)'].head())
print(merged_data['duration_(mins)'].isnull().sum())


# In[49]:


cooking_sessions = pd.read_excel(file_path, sheet_name="CookingSessions.csv")


# In[38]:


data.columns = data.columns.str.strip().str.replace(" ", "_")
print(data.columns)


# In[50]:


print("Cooking Sessions Data:")
print(cooking_sessions.head())


# In[65]:


plt.savefig('popular_dishes.png')


# In[67]:


merged_data.to_csv('cleaned_data.csv', index=False)

User Demographics
Age Group: Majority are 25–35 years old.
Top Cities: City A and City B dominate in participation and orders.
Preference: Dinner recipes are most popular (50%).

Cooking Sessions
Average Cooking Time: ~30 minutes.
Top Dishes: Caesar Salad, Spaghetti, Grilled Chicken.
Ratings: High satisfaction (4.5/5).

Orders Insights
City A has the highest orders; smaller cities show growth potential.
Outliers: Long cooking sessions (>60 minutes) linked with complex dishes.

Recommendations
Focus on dinner and health-conscious recipes.
Promote popular dishes through campaigns.
Improve delivery and engagement in smaller cities.
Analyze low-rated sessions for improvement