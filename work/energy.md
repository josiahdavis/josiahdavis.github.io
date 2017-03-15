---
layout: page
title: ""
---
![Josiah](../../public/electricity_big_1.png)

A large utilities provider wanted to conduct weather-based forecasting for residential customers electricity and gas consumption. Weather-based energy forecasting is of interest to utilities providers for many reasons. It can be used for company planning and resource allocation, measurement and evaluation of energy efficiency measures, and customer care and outreach.

As the lead data scientist on the project, I contributed several ideas that I iteratively tested and refined, combining techniques from classical forecasting, machine learning, and modern portfolio management theory.

* **Individual schedule-effect:** Customer-specific index that that identified their daily and hour schedule and adjusted their time-series
* **Supervised segmentation:** I used classification and regression trees based off of demographic data and typical utility utilization to put customers into segments
* **Spline regression:** I fit regression splines that regressed weather against energy consumption with stepwise generalized cross-validation using the Multivariate Adaptive Regression Splines.
* **Increase at Risk:** One of the key ideas of modern portfolio theory is value-at-risk. I adapted this idea to calculate the increase in energy consumption risk for each individual customer.
* **Model Evaluation:** I evaluated the models under a variety of weather-scenarios against a naive model to provide empirical evidence for the consistency of results.

I spent 95% of my time in R, using the following packages: purrr, tidyr, earth, rpart, randomForest, data.table, ggplot2.