DS-340-Proj

This project performs sentiment analysis on hotel reviews using deep learning models. The primary goal is to classify hotel reviews as either positive or negative based on the review text.

Dataset

The project uses the "Datafiniti Hotel Reviews" dataset, which is expected to be in a CSV file named Datafiniti_Hotel_Reviews.csv. The dataset contains various information about hotel reviews, but this project primarily focuses on the reviews.rating and reviews.text columns.

Models

The following models are implemented in this project:

Simple LSTM: A basic Long Short-Term Memory network for sequence classification.
Stacked LSTM: An LSTM model with two stacked LSTM layers for potentially capturing more complex patterns in the sequence data.
GRU: A Gated Recurrent Unit model, which is a variation of the LSTM.
BERT: The project also includes an initial exploration of using a pre-trained BERT model for sentiment analysis, although it is not fully implemented.
Hyperparameter Tuning

Hyperparameter tuning is performed for the simple LSTM model to find the optimal combination of the following hyperparameters:

Embedding Dimension
LSTM Units
Dropout Rate
Optimizer
The tuning process uses TensorFlow's HParams API and can be monitored using TensorBoard.

Usage

To use this project, you will need to have Python and the necessary libraries installed. The primary libraries used are pandas, scikit-learn, and TensorFlow.

Data Preparation: Ensure the Datafiniti_Hotel_Reviews.csv file is in the same directory as the notebooks.
Run the Notebooks:
DS-340-Proj.ipynb: Contains initial data exploration and an incomplete BERT implementation.
340_Proj_LSTM.ipynb: Contains the main workflow for training and evaluating the LSTM and GRU models.
Results

The models are trained to classify hotel reviews as positive (rating >= 4) or negative (rating < 3). The performance of the models is evaluated based on their accuracy on a validation set. The 340_Proj_LSTM.ipynb notebook saves the best performing models, which can then be used for inference on new review data.

---

Analysis of Maternal Health & Infant Outcomes in the U.S.

This repository contains the source code for an interactive website built with R and Quarto for the MA415/MA4615 Data Science course. The project analyzes the impact of maternal lifestyle choices, particularly smoking, on infant health outcomes using U.S. natality data.

Live Website: https://ma-415-n8hl1cp2x-rohan-anands-projects.vercel.app Project Presentation Video: https://youtu.be/idH7NyRJwKc

Project Overview

Maternal smoking is a significant and preventable risk factor for poor pregnancy outcomes, contributing to both individual health consequences and large-scale economic costs. This project explores the current landscape of maternal smoking in the United States and its correlation with key infant health metrics, specifically birth weight and APGAR scores.

Beyond smoking, the analysis also investigates other significant factors like maternal BMI to provide a broader picture of the maternal health crisis in America. The goal is to highlight these health risk factors to inform better prenatal health practices and potential public policy.

Key Research Questions Addressed

What racial group has the highest proportion of mothers who smoke before and during pregnancy?
Does smoking negatively impact the birth weight and APGAR scores of babies, regardless of race?
Is there a statistically significant difference in birth weights between babies of smoking and non-smoking mothers?
What has been the trend in maternal smoking over the past decade?
Is there an association between the prevalence of smoking in a state and the average gestation period?
Can a linear model accurately predict birth weight and APGAR scores based on maternal lifestyle factors?
Key Findings

Racial Disparities in Smoking: American Indian and Alaskan Native (AIAN) mothers have the highest proportion of smoking before and during all trimesters of pregnancy.
Negative Health Correlation: There is a consistent inverse relationship between smoking and mean birth weight/APGAR scores across all racial groups.
Decline in Smoking Rates: There has been a considerable decline in the proportion of mothers who smoke during pregnancy for most racial groups between 2014 and 2021.
BMI as a Major Predictor: Maternal BMI was found to be a more significant feature than cigarette use in predicting an infant's APGAR score.
Technology Stack

Language: R
Website Framework: Quarto
Core Libraries: tidyverse, ggplot2, dplyr, gt
Deployment: Vercel / GitHub Pages
Data Source

The analysis uses the Natality Data from the National Vital Statistics System, provided by the National Center for Health Statistics (NCHS), a unit of the CDC. The data is compiled from a 100% sample of birth certificates from some states and a 50% sample from others, providing comprehensive demographic and health data for births in the United States.

---

The Effect of Unemployment on Democratic Vote Share: An Analysis of Swing States in the 2020 Presidential Election

Project Overview

This project analyzes the relationship between county-level unemployment rates, age demographics, and the Democratic vote share in the 2020 U.S. Presidential Election. The analysis focuses on seven key swing states: Arizona, Georgia, Michigan, Nevada, North Carolina, Pennsylvania, and Wisconsin.

The primary research questions are:

What is the relationship between county-level unemployment rates and Democratic vote share?
Does this relationship vary across different age demographics?
How do these patterns differ across the selected swing states?
Methodology

The analysis uses regression models to examine the effect of unemployment on voting patterns. The key variables are:

Independent Variable: County-level unemployment rate.
Dependent Variable: Democratic vote share in the 2020 presidential election.
The project also incorporates age demographics by categorizing counties as predominantly young (18-35), middle-aged (36-55), or older (56+) and using interaction terms in the regression models.

Key Findings

Overall, there is a statistically significant, but weak, positive relationship between unemployment and Democratic vote share. A 1 percentage point increase in unemployment is associated with a 1.58 percentage point increase in Democratic vote share.
The relationship between unemployment and Democratic votes varies by state. Georgia and Nevada showed strong positive relationships, while Michigan showed a negative relationship.
Younger--dominant counties (ages 18-35) showed the strongest positive relationship between unemployment and Democratic support.
The low R-squared values in the models suggest that other factors, such as education, urban-rural divides, and pandemic response, were also significant in determining voting patterns.
Files in this Project

399poster.Rmd: The R Markdown file containing the code for the analysis and the poster generation.
399_final_poster-2.pdf: The final poster presenting the research question, analysis, and conclusions.
usa_county_shapefile.rds, unemployment_rate_by_county.rds, election_data_president_2012_2020.rds, age_data_by_county_2020.rds: The data files used in the analysis.
