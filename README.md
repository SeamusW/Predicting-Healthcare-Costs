# Predicting-Healthcare-Costs

![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/adaa4d70-3df9-4cd4-8cbb-0cf47e0b2caa)


# Predicting Uninsured Healthcare Costs with Regression
*Seamus Walsh |  August 3, 2023*

## Overview
From a patient's perspective, the US Healthcare system can often seem like a confusing, disorienting mess. Of the many hurdles patients encounter, one of the biggest is the cost. Whether your insured or not, healthcare costs can be ambiguous at best, and often frightening for the average person. It's not uncommon to hear stories of people not wanting to take an ambulance because of the expected bill they will incur afterwards. This project aims to help clear some of that ambiguity as it relates to unsinured hospital admissions.



## Project and Data Links
<a href="https://github.com/SeamusW/Predicting-Healthcare-Costs/blob/main/Final%20Model%20SW.ipynb">Modeling and Final Analysis</a>

<a href="https://github.com/SeamusW/Predicting-Healthcare-Costs/blob/main/Exploring%20Different%20Models%20SW.ipynb"> Exploring Different Models</a>

<a href="https://github.com/SeamusW/Predicting-Healthcare-Costs/blob/main/Data%20Cleaning%20and%20EDA%20SW.ipynb">EDA and Data Preparation</a>
 
<a href="https://github.com/SeamusW/Predicting-Healthcare-Costs/blob/main/Predicting%20Hospital%20Admission%20Costs.pdf">Project Slide Deck</a>

<a href="https://health.data.ny.gov/">Data Source: NYS DOH</a>


## Business and Data Understanding
The issue of price ambiguity in US Healthcare has long been a problem. So much so that in January 2021 a federal law was passed, the "Hospital Price Transparency Rule". However, the vast majority of hospitals aren't actually complying with this new rule (https://jamanetwork.com/journals/jama/article-abstract/2792987), and there doesn't seem to be much work on ensuring their compliance.

In an effort to provide some meaningful transparency, I sought to create a regression model that can predict uninsured hospital admission costs based on certain features of a hospital visit. The hope is that this information can be used by patients to help guide their healthcare decision-making.


## Data Analysis
For my analysis I examined hospital admissions data provided by the New York Department of Health that included information from 178 different hospitals and over 27,000 patient visits. The data included visit information like diagnoses, procedures, length of stay, and patient disposition, as well as demographic information like gender, race, ethnicity and age. Below, I've included some exploratory analysis, visualizations, and the final model



## Exploratory Analysis
After doing all of the necessary data wrangling and cleaning, I took a look at the breakdown of the target feature "Total Charges" across different groups.

## Distribution of Total Charges
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/4483b9ca-ea16-4ced-a0f7-237eda81eef7)

## Median Total Charges by Hospital Service Area
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/4c223cfc-5faf-4ecd-8030-09633d4a77cc)

## Median Total Charges by County
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/79e54756-08ee-477b-a5a1-e81851676432)

## Median Total Charges by Diagnosis
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/83f3608a-632c-48ab-aeea-7a4536eeedb5)

## Median Total Charges for Cesarean Delivery in New York State
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/32f9b61a-278d-4f86-9180-b602b318ac84)

## Median Total Charges for Cesarean Delivery in Brooklyn
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/11f7ac9a-9c16-4f62-a5a5-59fd3f5cc73f)

## Median Total Charges for Asthma Treatment in Brooklyn
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/ab1c484d-5e3e-4beb-ad10-0c39289964a0)

## Median Total Charges by Age Group
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/2817d35e-d463-4bd4-a81e-33ce94c4d0b6)

## Median Total Charges by Length of Stay
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/05ac77a6-3271-435b-a32b-3fe2e73c6d9d)

## Median Total Charges by Risk of Mortality
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/906f4476-0ff6-407a-b966-47a5cbde3e88)

## Median Total Charges by Type of Admission
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/98af22a4-b97d-484d-b1e6-949f330b4fc8)

## Rough Correlations with Total Charges
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/02a5ecaf-fc5d-4cd5-93e5-b1de06f5e775)


Some insights from this analysis:
<li> Total Charges are skewed so that most are less than $20,000 with the distribution lowering as charges increase. This is also after removing the huge outliers (anything above 3 standard deviations/$80,000). Several charges that were excluded for our purposes were in the millions.</li>

<li>There is huge variability across features. While you might expect some hospitals to have higher median total charges because of the type of procedures they perform, or the amount of patients they see, when you drill down further and look directly at the exact same procedures, there are still huge differences in charges. For example, a cesarean delivery costs, on average, $20,000 more if it takes place in NYC versus the Finger Lakes region. There are often even bigger discrepencies within local areas. Drilling down even further into Brooklyn alone, there is a $50,000 difference for the same procedure across hospitals. You can see the same thing for multiple different procedures, an example above provided for asthma treatment in brooklyn</li>

<li>The codes are the most highly correlated with Total Charges, however the correlation is difficult to interpret as their numerical value is just a code, rather than a meaningful ordinal relationship. I need to be thoughtful about how these and other categorical coded features are included in the model.</li>


## Baseline Model
I first ran a simple linear regression, but because linear regression allows predicted values below 0, it really isn't the appropriate model (giving me a nonsensical r-square of -6.840362941284886e+19.

Because I needed my predicted values to always be above 0 (there are no negative charges), I next tried a Poisson Regression. It looks too good to be true, with a pseudo r-square of exactly 1.0 telling me that I am definitely overfitting.
Poisson Regression:
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/4f032c94-18e6-48dd-9500-7ffb6e005cce)


## Intermediate Models
Next I tried Ridge and Lasso Regression models to try and prevent overfitting. Getting similar scores for each: R-Square ~ 79%, MSE = 49,799,661
Ridge Regression:
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/eb91ac86-ec37-497c-a36a-efa1a7dffd6a)

Lasso Regression:
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/2e60e168-0e5f-4061-8541-40510fbbe584)

I next tried a Random Forest Regression model, which gave an r-square ~ 81% and MSE = 43449518.215441905
Random Forest Regression:
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/7a9ec967-f2fd-4a8d-ad41-b9ff89834b22)


## Final Model
It looks like the Random Forest Model is the best baseline model. However, I wanted to try some dimensionality reduction, due to my really large amount of features. I also wanted to use clustering to create features that might help explain more variance.

After testing different cluster amounts, and running Principal Component Analysis to reduce the amount of features, I settle on the best working model. R-Square = 82%, MSE = 42843940.78174081

Random Forest Regression with clustering features and PCA:
![image](https://github.com/SeamusW/Predicting-Healthcare-Costs/assets/32468677/5ecf5793-099f-41a8-a0e1-c89c3a97573f)


## Next Steps
<li> Refine the model with more data, and more patient specific features
<li> Develop patient facing app that can be used to predict and compare costs across hospital systems


## Repository Structure
  <b>data folder</b> This folder houses the .csv files that were used to create these analyses.
  
  <b>Predicting Hospital Admissions Costs - Slide Deck</b> This file is a slide deck covering the analysis.

  <b>Data Cleaning and EDA</b> This file contains the data wrangling and exploratory analysis.

  <b>Exploring Different Models</b> This file contains all of the preliminary models and analysis.

  <b>Final Model</b> This file contains the final working model.
  
  
  <b>README.md</b> This is the file you are reading now that gives an overview of our project.
