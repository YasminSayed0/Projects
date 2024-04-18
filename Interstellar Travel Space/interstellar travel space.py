#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


it=pd.read_csv('interstellar_travel.csv')
it


# In[3]:


it.info()


# In[4]:


it[['Booking Date','Departure Date']]=it[['Booking Date','Departure Date']].apply(pd.to_datetime)


# In[5]:


it.duplicated().any()


# In[6]:


it.isnull().any()


# In[7]:


age_values=it['Age'].unique()
age_values.sort()
age_values


# In[10]:


age_categories={'10s':range(0,10),'20s':range(20,30),'30s':range(30,40),'40s':range(40,50),'50s':range(50,60),'60s':range(60,70),'70s':range(70,80),'80s':range(80,90),'90s':range(90,100)}
category_counts={category:0 for category in age_categories}

for age in it['Age']:
    for category ,age_range in age_categories.items():
        if age in age_range:
            category_counts[category]+=1
            break
            
plt.figure(figsize=(8, 8))
labels = list(category_counts.keys())
sizes = list(category_counts.values())

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Age')
plt.axis('equal')  
plt.show()


# In[12]:


purpose_counts = it['Gender'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(purpose_counts, labels=purpose_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution Of Gender')
plt.axis('equal')  
plt.show()


# In[13]:


it['Occupation'].unique()


# In[14]:


purpose_counts = it['Occupation'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(purpose_counts, labels=purpose_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution Of Occupation')
plt.axis('equal')  
plt.show()


# In[15]:


it['Travel Class'].unique()


# In[18]:


loyalty_counts = it['Travel Class'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 6))
color_dict = {'Economy': 'blue', 'Business': 'red', 'Luxury': 'gold'}
bars = loyalty_counts.plot(kind='bar', color=[color_dict[x] for x in loyalty_counts.index]) 
plt.title('Percentage Of Travel Class')
plt.xlabel('Travel Class')
plt.ylabel('Percentage')
plt.xticks(rotation=0) 

for index, value in enumerate(loyalty_counts):
    plt.text(index, value + 1, f'{value:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()


# In[19]:


it['Purpose of Travel'].unique()


# In[20]:


purpose_counts = it['Purpose of Travel'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(purpose_counts, labels=purpose_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution Of Purpose Of Travel ')
plt.axis('equal')  
plt.show()


# In[21]:


it['Year'] = it['Booking Date'].dt.year
year_counts = it['Year'].value_counts()
year_counts


# In[24]:


it.loc[:,'Year'] = it['Booking Date'].dt.year
it = it[it['Year'] != 2024]
year_counts = it['Year'].value_counts()


plt.figure(figsize=(8, 6))
bars = year_counts.plot(kind='bar', color='skyblue')
plt.title('Count of Occurrences by Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)

for index, value in enumerate(year_counts):
     plt.text(index, value+1 , str(value), ha='center', va='bottom')

percentage_increase = ((year_counts[2023] - year_counts[2022]) / year_counts[2022]) * 100
plt.title('Percentage Increase (2022 to 2023): {:.2f}%'.format(percentage_increase))

plt.tight_layout()
plt.show()


# In[27]:


it.loc[:,'Year'] = it['Booking Date'].dt.year
it = it[it['Year'] != 2024]

unique_years = it['Year'].unique()
sums_by_year = {}

for year in unique_years:
    sum_price = it[it['Year'] == year]['Price (Galactic Credits)'].sum()
    sums_by_year[year] = sum_price
    
plt.bar(sums_by_year.keys(), sums_by_year.values(), color='skyblue')
plt.xlabel('Year')
plt.ylabel('Total Price')
plt.title('Total Price for Each Year')

for year, price in sums_by_year.items():
        formatted_price = "{:,.1f}".format(price).rstrip('0').rstrip('.')
        plt.text(year, price + 5, formatted_price, ha='center')

plt.xticks(list(sums_by_year.keys()))
plt.show()


# In[28]:


loyalty_counts = it['Special Requests'].value_counts(normalize=True) * 100
plt.figure(figsize=(10, 7))
bars = loyalty_counts.plot(kind='bar')

plt.title('Percentage of Customer in Special Requests ')
plt.xlabel('Special Requests')
plt.ylabel('Percentage')
plt.xticks(rotation=0) 

for index, value in enumerate(loyalty_counts):
         plt.text(index, value + 1, f'{value:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()


# In[32]:


gender_counts = it.groupby('Special Requests')['Gender'].value_counts(normalize=True) * 100

sr_g = gender_counts.unstack().plot(kind='bar', stacked=True)

plt.xlabel('Special Requests')
plt.ylabel('Percentage')
plt.title('Percentage of Gender by Special Requests')

for p in sr_g.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()    
    sr_g.annotate(f'{height:.1f}%', (x + width/2, y + height/2), ha='center', va='center')

plt.legend(title='Gender', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()


# In[33]:


loyalty_counts = it['Loyalty Program Member'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 6))
bars = loyalty_counts.plot(kind='bar')

plt.title('Percentage Loyalty Program Member ')
plt.xlabel('Loyalty Program')
plt.ylabel('Percentage')
plt.xticks(rotation=0) 

for index, value in enumerate(loyalty_counts):
         plt.text(index, value + 1, f'{value:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()


# In[36]:


customer_satisfaction_score_cate= {'Poor': range(32, 51), 'Medium': range(50, 75), 'High': range(75, 116)}
customer_satisfaction_score_count = {satisfaction: 0 for satisfaction in customer_satisfaction_score_cate}
total_count = 0

customer_satisfaction_scores = it['Customer Satisfaction Score']
for customer_satisfaction in customer_satisfaction_scores:
    satisfaction_int = int(customer_satisfaction)
    for satisfaction, score_range in customer_satisfaction_score_cate.items():
        if satisfaction_int in score_range:
            customer_satisfaction_score_count[satisfaction] += 1
            total_count += 1

plt.figure(figsize=(8, 6))
color_dict = {'Poor': 'blue', 'Medium': 'red', 'High': 'gold'}
percentages = [(count / total_count) * 100 for count in customer_satisfaction_score_count.values()]
bars = plt.bar(customer_satisfaction_score_cate.keys(), percentages, color=[color_dict[x] for x in customer_satisfaction_score_cate.keys()]) 
plt.title('Percentage of Customers in Satisfaction Categories')
plt.xlabel('Satisfaction Category')
plt.ylabel('Percentage')

for index, percentage in enumerate(percentages):
    plt.text(index, percentage + 1, f'{percentage:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()


# In[ ]:




