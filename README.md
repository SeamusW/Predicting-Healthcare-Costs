# Predicting-Healthcare-Costs

![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/adaa4d70-3df9-4cd4-8cbb-0cf47e0b2caa)


# Predicting Uninsured Healthcare Costs with Regression
*Seamus Walsh |  August 3, 2023*

## Overview
From a patient's perspective, the US Healthcare system can often seem like a confusing, disorienting mess. Of the many hurdles patients encounter, one of the biggest is the cost. Whether your insured or not, healthcare costs can be ambiguous at best, and often frightening for the average person. It's not uncommon to hear stories of people not wanting to take an ambulance because of the expected bill they will incur afterwards. This project aims to help clear some of that ambiguity as it relates to unsinured hospital admissions.



## Project and Data Links
<a href="https://github.com/SeamusW/NLP-Tweet-Emotions/blob/main/Modeling%20and%20Final%20Analysis.ipynb">Modeling and Final Analysis</a>

<a href="https://github.com/SeamusW/NLP-Tweet-Emotions/blob/main/EDA%2C%20Processing%2C%20and%20Feature%20Engineering%20-%20Twitter%20Sentiment%20Analysis%20Project.ipynb">EDA and Data Preparation</a>
 
<a href="https://github.com/SeamusW/Twitter-Sentiment-Analysis-using-NLP/blob/main/Twitter%20Sentiment%20Analysis%20Slide%20Deck%20-%20July%202023.pdf">Project Slide Deck</a>

<a href="https://data.world/crowdflower/brands-and-product-emotions">Data Source: DataWorld.com</a>


## Business and Data Understanding
The problem of price ambiguity in US Healthcare has long been a problem. So much so that in January 2021 a federal law was passed, the "Hospital Price Transparency Rule". However, the vast majority of hospitals aren't actually complying with this new rule (https://jamanetwork.com/journals/jama/article-abstract/2792987), and there doesn't seem to be much work on ensuring their compliance.

In an effort to provide some meaningful transparency, I sought to create a regression model that can predict uninsured hospital admission costs based on certain features of a hospital visit. The hope is that this information can be used by patients to help guide their healthcare decision-making.


## Data Analysis
For my analysis I examined hospital admissions data provided by the New York Department of Health that included information from 178 different hospitals and over 27,000 patient visits. The data included visit information like diagnoses, procedures, length of stay, and patient disposition, as well as demographic information like gender, race, ethnicity and age. Below, I've included some exploratory analysis, visualizations, and the final model



## Exploratory Analysis
After doing all of the necessary data wrangling and cleaning, I took a look at the breakdown of the target feature "Total Charges" across different groups.

## Distribution of Total Charges

## Total Charges by Hospital Service Area

## Total Charges by County

## Total Charges by Age Group

## Total Charges by Diagnosis

## Total Charges by Length of Stay

## Total Charges by Risk of Mortality

## Total Charges by Type of Admission

## Rough Correlations with Total Charges


Some insights from this analysis:
<li> Total Charges are skewed so that most are less than $20,000 with the distribution lowering as charges increased. This is also after removing the huge outliers (anything above 3 standard deviations/$80,000). Several charges that were excluded for our purposes were in the millions.</li>
<li>There is huge variability across most features. Especially when looking at specific codes across different hospitals and service areas.</li>
<li>The codes are the most highly correlated with Total Charges, however the correlation is difficult to interpret as their numerical value is just a code, rather than a meaningful ordinal relationship. There are additional codes that are included in the analysis that aren't listed here as they will need to be dummy encoded.</li>


## Baseline Model
For our first model, we started with a Random Forest Classifier. We received a training accuracy score of .99 and a test accuracy of .85. For a first model, this looks pretty good!
![image](https://github.com/SeamusW/NLP-Tweet-Emotions/assets/32468677/6cf47eb6-f41b-4086-bd2a-6d523ffad498)


## Logistic Regression Model
One model that specifically performed slightly better than others on accurately predicting negative tweets was the Logistic Regression Model. It received a training accuracy score of .93 and a test accuracy score of .85.
![image](https://github.com/SeamusW/NLP-Tweet-Emotions/assets/32468677/20b59df9-82e9-45dc-99db-869ec3803d2e)


## Final Model
After testing several different models, the one with the best results was the XGBoost Classifier. It had a training accuracy score of .96 and a test accuracy score of .86. Looking at the difference in scores between this and our initial model, this one seems to be overfitting less, and should perform better on unseen data, which is why it was chosen as the final model. However, if you are more interested in exploring negative feedback about your product, we would recommend using the Logistic Regression Model instead.
![image](https://github.com/SeamusW/NLP-Tweet-Emotions/assets/32468677/79c466b1-ed12-4d31-ad3b-3d97a566eb49)




## Recommendations
<li>Gauge implicit brand favorability using our model
<ul class="square">
  <li>Because these are implicit feelings, they have arguably more value than other industry measures on customer satisfaction</li></ul>
<li>Track sentiment trends
 <ul class="square">
   <li>By gathering this information over time, you can use to track trends and make interventions.</li></ul>
<li>Hone in on consumer critiques in negative tweets
<ul class="square">
  <li> Based one the service recovery paradox, focusing on the negative critiques can turn detractors into promoters</li></ul>

## Next Steps
<li>Generate model based on expanded metrics
<li>Integrate data from other companies for cross-comparison
<li>Gather more data

## Repository Structure
  <b>data folder</b> This folder houses the .csv files we used to create these analyses.
  
  <b>Twitter Sentiment Analysis - Slide Deck</b> This file is a slide deck covering our analysis.

  <b>EDA, Processing and Feature Engineering - Twitter Sentiment Analysis Project</b> This file contains our data wrangling and exploratory analysis.

  <b>Data Modeling and Final Analysis</b> This file contains all of our models and analysis.
  
  
  <b>README.md</b> This is the file you are reading now that gives an overview of our project.
