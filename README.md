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
The issue of price ambiguity in US Healthcare has long been a problem. So much so that in January 2021 a federal law was passed, the "Hospital Price Transparency Rule". However, the vast majority of hospitals aren't actually complying with this new rule (https://jamanetwork.com/journals/jama/article-abstract/2792987), and there doesn't seem to be much work on ensuring their compliance.

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

<li>There is huge variability across most features. Especially when looking at specific codes across different hospitals and service areas. For example, a cesarean delivery costs, on average, $20,000 more if it takes place in NYC or on Long Island, versus other parts of the state.</li>

<li>The codes are the most highly correlated with Total Charges, however the correlation is difficult to interpret as their numerical value is just a code, rather than a meaningful ordinal relationship. I need to be thoughtful about how these and other categorical coded features are included in the model.</li>


## Baseline Model


## Intermediate Model


## Final Model



## Recommendations
<li>REC 1
<ul class="square">
  <li>Explanation</li></ul>
<li>REC 2
 <ul class="square">
   <li>Explanation</li></ul>
<li>REC 3
<ul class="square">
  <li> Explanation</li></ul>

## Next Steps
<li>1
<li>2
<li>3

## Repository Structure
  <b>data folder</b> This folder houses the .csv files that were used to create these analyses.
  
  <b>Predicting Uninsured Healthcare Costs - Slide Deck</b> This file is a slide deck covering the analysis.

  <b>Data Cleaning and EDA</b> This file contains the data wrangling and exploratory analysis.

  <b>Exploring Different Models</b> This file contains all of the preliminary models and analysis.

  <b>Final Model</b> This file contains the final working model.
  
  
  <b>README.md</b> This is the file you are reading now that gives an overview of our project.
