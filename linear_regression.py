
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv(r"C:\Users\sijom\OneDrive\Desktop\Marian\Sem2\ML\Colab2\Web_Performance.csv")

# Select input (X) and output (y)
# Use 'Throughput' as X and 'Response Time(s)' as y
X = data[['Throughput']].values
y = data[['Response Time(s)']].values

# Handle missing values if any
imputer_X = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer_y = SimpleImputer(missing_values=np.nan, strategy='mean')
X1 = imputer_X.fit_transform(X)
y1 = imputer_y.fit_transform(y)

# Split the dataset into train and test set
X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.2, random_state=0)

# Fit the model to the training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict
y_pred = regressor.predict(X_test)

# Print predictions and test values
print("Predicted:", y_pred.flatten())
print("Actual:", y_test.flatten())

# Visualize training set results
plt.scatter(X_train, y_train, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Throughput vs Response Time (Train)")
plt.xlabel("Throughput")
plt.ylabel("Response Time (s)")
plt.show()

# Visualize test set results
plt.scatter(X_test, y_test, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Throughput vs Response Time (Test)")
plt.xlabel("Throughput")
plt.ylabel("Response Time (s)")
plt.show()
