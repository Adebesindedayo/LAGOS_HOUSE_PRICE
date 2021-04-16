PROBLEM STATEMENT 
Customers of a Real Estate property aggregation company complain about their user experience on the property site as they are unable to easily get a rent budget without going through several pages of the website.

Proposed Solution
Building a rent budget estimator with a machine learning algorithm that will take in features such as location, bed, bath, etc. which will be provided by customers.

DATA SCIENCE METHODOLOGY USED

METHODOLGY
1. Data Collection - SCRAPING DATA FROM Scrape data from Proprtypro.ng using Request.html because the site is a dynamic website rendered with javascript
2. Data preprocessing - Handling missing values, dealing with outliers
3. Exploratory Data Analysis
4. Feature Engineering - Categorical encoding, ranking,
5. Modelling - Building a baseline model, Optimizing the baseline model
6. Model Evaluation
7. Model/Result Visualization - Plotly Dash app
RESULTS AND INSIGHTS
1. Initial RMSE was very high because initial features available was insufficient
2. Not enough infomation in the data to explain the high variance in price between houses of the same features
3. Plot a graph to show the high variance in price (box plot)
4. Outliers due to wrong infomation entered by agents on the property website
RECOMMENDATIONS/NEXT STEPS
1. Making important features like bed, baths, toilets and price compulsory in the form filled by agents on the propertry website.
2. Making the form structured by adding fields for additional information like newly built, furnished, serviced, terraced, security systems, swimming pools, and other luxury features to account for the high varince in house prices.
3. Using percentile ranges such as 85th & 15th or 90th & 10th percentiles to deal with extremities or outliers when building the model.
4. Building a beta version of the application with the information available as a test version pending when a complete info is gotten.


