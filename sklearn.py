# imports
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# read in the data
drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/python-data-science-workshop/master/drinks.csv', na_filter=False)

# features
X = drinks[['beer_servings','spirit_servings']]
X.shape

# response
y = drinks['wine_servings']
y.shape

# fit a linear model
lm = LinearRegression()
lm.fit(X, y)

# examine the intercept and coefficients
lm.intercept_
lm.coef_

# manually predict wine servings for the first two countries
drinks.head()
lm.intercept_ + 0*lm.coef_[0] + 0*lm.coef_[1]
lm.intercept_ + 89*lm.coef_[0] + 132*lm.coef_[1]

# predict for all countries
preds = lm.predict(X)
preds

# compute the MSE and RMSE
mean_squared_error(y, preds)
np.sqrt(mean_squared_error(y, preds))

# compute the R^2
lm.score(X, y)

# Important questions:
# Is the relationship actually linear?
# Did we include the right variables?
# Do we have the right data to answer this question?
# Will our model generalize to new data?
