import numpy as np
from sklearn.linear_model import LinearRegression

# Example data (X should be 2D, y should be 1D)
X = np.array([[1], [2], [3], [4], [5]])  # Feature matrix
y = np.array([1.5, 3.0, 4.5, 6.0, 7.5])  # Target values

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)
X_new = np.array([[6], [7]])  
predictions = model.predict(X_new)
print("Predictions for X_new:", predictions)
