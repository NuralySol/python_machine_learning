import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create a DataFrame
df = pd.DataFrame()
df["Area"] = [2600, 3000, 3200, 3600, 4000]
df["Price"] = [550000, 565000, 610000, 680000, 725000]

# Print the DataFrame
print(df)

# Plotting the data
plt.scatter(df["Area"], df["Price"], color='blue')
plt.xlabel("Area of the House (sq ft)")
plt.ylabel("Price of the House (USD)")
plt.title("House Price vs Area")
plt.show()

# Create a LinearRegression model
model = LinearRegression()

# Reshape the data and fit the model
X = df["Area"].values.reshape(-1, 1)  # Area as input feature (2D array required)
y = df["Price"].values  # Price as the target/output

# Fit the model to the data
model.fit(X, y)

# Get the slope (coefficient) and intercept
slope = model.coef_[0]
intercept = model.intercept_

# Print the slope and intercept
print(f"Slope (Coefficient): {slope}")
print(f"Intercept: {intercept}")

# Predict the price for the given areas
predicted_prices = model.predict(X)

# Plot the regression line along with the data points
plt.scatter(df["Area"], df["Price"], color='blue')  # Original data points
plt.plot(df["Area"], predicted_prices, color='red', linewidth=2)  # Regression line

# Plot the predicted prices with green stars
plt.scatter(df["Area"], predicted_prices, color='green', marker='*', s=100, label='Predicted Prices')

# Predict the price for a house with an area of 5000 sq ft
predicted_price_5000 = model.predict([[5000]])  # 2D array required for prediction
print(f"Predicted price for a house with 5000 sq ft area: {predicted_price_5000[0]}")

# Plot the 5000 sq ft prediction with an orange star
plt.scatter([5000], predicted_price_5000, color='orange', marker='*', s=200, label='Predicted Price (5000 sq ft)')

# Add labels and title
plt.xlabel("Area of the House (sq ft)")
plt.ylabel("Price of the House (USD)")
plt.title("House Price vs Area with Regression Line and Predicted Prices")
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()