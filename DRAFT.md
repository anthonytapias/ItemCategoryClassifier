# What Class is this APP?

## Introduction
For this project we decided to try and build a Machine Learning model that would accurately predict the category in which an apps description would be. To do this we did some natural language processing and ran a lot of models with different parameters to test the accuracy of our predictions on the training data using CV and then on the testing data to test for overfitting. 

## Gathering and Cleaning The Data
To gather data we built a webscrapper using Beautiful Soup (BS4) and scraped first the top 50 Free apps of 18 categories. Then we scraped each of the apps page and pulled the description of the application. After that we did a little EDA via doing a frequency word count and some word clouds. Seeing as this showed some repeated and common terms we then used NLTK to change all words to lower-case, to remove all punctuation using REGEX and to tokenize and stem them. Once that was done we joined each description again and we placed them and labeled them in a dataframe.

## Models?

## Conclusions?

## Creating The Visualizations

## Future Plans
