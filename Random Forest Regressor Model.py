#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestRegressor


# In[2]:


df1 = pd.read_csv('/Users/seamuswalsh/Flatiron/Course Materials/Phase 5/Capstone Project/Data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2021 (1).csv')


# In[3]:


# Only keeping patients who are uninsured

values_to_keep = ['Self-Pay']

df1 = df1[df1['Payment Typology 1'].isin(values_to_keep)]
df1['Payment Typology 1'].value_counts()


# ## Adding and merging other data sets
# 

# In[4]:


df2 = pd.read_csv('/Users/seamuswalsh/Flatiron/Course Materials/Phase 5/Capstone Project/Data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2020.csv')


# In[5]:


df2 = df2[df2['Payment Typology 1'].isin(values_to_keep)]
df2['Payment Typology 1'].value_counts()


# In[6]:


df = pd.concat([df1, df2])
df.info()


# In[7]:


df3 = pd.read_csv('/Users/seamuswalsh/Flatiron/Course Materials/Phase 5/Capstone Project/Data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2019.csv')


# In[8]:


df3 = df3[df3['Payment Typology 1'].isin(values_to_keep)]
df3['Payment Typology 1'].value_counts()


# In[9]:


df = pd.concat([df, df3])
df.info()


# In[10]:


df4 = pd.read_csv('/Users/seamuswalsh/Flatiron/Course Materials/Phase 5/Capstone Project/Data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2018.csv')


# In[11]:


df4 = df4[df4['Payment Typology 1'].isin(values_to_keep)]
df4['Payment Typology 1'].value_counts()


# In[12]:


df = pd.concat([df, df4])
df.info()


# In[13]:


df['Length of Stay'] = pd.to_numeric(df['Length of Stay'], errors='coerce')


# In[14]:


df = df[df['Total Charges'] != 0]


# ## Dropping NaNs and some unnecessary columns

# In[16]:


df.dropna(subset=['CCSR Procedure Code'], inplace=True)


# In[18]:


columns_to_drop_1 = ['Operating Certificate Number', 'Permanent Facility Id'
                     , 'Zip Code - 3 digits', 'CCSR Diagnosis Description'
                     , 'CCSR Procedure Description', 'APR DRG Description'
                     , 'APR MDC Description', 'APR Severity of Illness Description'
                     , 'Payment Typology 2', 'Payment Typology 3', 'Birth Weight'
                    , 'Total Costs']
df.drop(columns_to_drop_1, axis=1, inplace=True)


# In[19]:


df.dropna(inplace=True)
df.info()


# ## Updating Length of Stay Variable

# In[21]:


filtered_df = df[df['Length of Stay'] <= 2]


# ## Updating Severity of Illness Variable

# In[23]:


filtered_df['APR Severity of Illness Code'].value_counts()


# In[24]:


filtered_df = filtered_df[filtered_df['APR Severity of Illness Code'] < 2]


# In[25]:


filtered_df['Total Charges'].describe()


# In[26]:


filtered_df = filtered_df[filtered_df['Total Charges'] < 80000]


# ## Scaling necessary columns

# In[28]:


columns_to_scale = ['APR DRG Code', 'APR MDC Code']

selected_data = filtered_df[columns_to_scale]

print("Missing values in selected_data before scaling:")
print(selected_data.isna().sum())


# In[29]:


scaler = MinMaxScaler()

scaler.fit(selected_data)

scaled_data = scaler.transform(selected_data)

scaled_df = pd.DataFrame(scaled_data, columns=columns_to_scale)

print("\nMissing values in scaled_df:")
print(scaled_df.isna().sum())


print("\nData types of original DataFrame:")
print(filtered_df[columns_to_scale].dtypes)

print("\nData types of scaled DataFrame:")
print(scaled_df.dtypes)


# In[30]:


if not filtered_df.index.equals(scaled_df.index):
    scaled_df.set_index(filtered_df.index, inplace=True)


# In[31]:


filtered_df[columns_to_scale] = scaled_df


# ## Dummy encoding and dropping the remaining unnecessary columns

# In[35]:


df_encoded = pd.get_dummies(filtered_df, columns=['Hospital Service Area', 'Hospital County', 'Facility Name'
                                         , 'Age Group', 'Gender', 'Race', 'Ethnicity', 'Type of Admission'
                                         , 'Patient Disposition', 'CCSR Diagnosis Code', 'CCSR Procedure Code'
                                         , 'APR Risk of Mortality', 'APR Medical Surgical Description'
                                         , 'Emergency Department Indicator']
                            ,prefix=['Hospital Service Area', 'Hospital County', 'Facility'
                                     , 'Age Group', 'Gender', 'Race', 'Ethnicity', 'Type of Admission'
                                     , 'Patient Disposition', 'CCSR Diagnosis Code', 'CCSR Procedure Code'
                                     , 'APR Risk of Mortality', 'APR Medical Surgical Description'
                                     , 'Emergency Department Indicator'])


# In[36]:


columns_to_drop_2 = ['Hospital Service Area', 'Hospital County'
                  , 'Facility Name', 'Age Group', 'Gender', 'Race', 'Ethnicity'
                  , 'Type of Admission', 'Patient Disposition', 'CCSR Diagnosis Code'
                  , 'CCSR Procedure Code', 'APR Risk of Mortality'
                  , 'APR Medical Surgical Description', 'Payment Typology 1'
                  , 'Emergency Department Indicator']


# In[37]:


for col in columns_to_drop_2:
    try:
        df_encoded.drop(columns=[col], inplace=True)
    except:
        print(col)


# ## Log Transforming the target variable to account for skew

# In[38]:


df_encoded['log_Total Charges'] = df_encoded['Total Charges'].apply(lambda x: np.log(x))


# ## Testing on a Random Forest Regressor Model
# 

# In[40]:


y = df_encoded['log_Total Charges']
X = df_encoded.drop(columns =['Total Charges', 'log_Total Charges'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)


# In[41]:


rfr = RandomForestRegressor()
rfr.fit(X_train,y_train)
print(rfr.score(X_test,y_test))

preds = rfr.predict(X_test)


# In[42]:


print(rfr.score(X_test,y_test))
mse = mean_squared_error(np.exp(y_test), np.exp(preds))
print("Mean Squared Error (MSE):", mse)


# In[43]:


import plotly.express as px
px.scatter(x = np.exp(y_test), y = np.exp(preds) )

