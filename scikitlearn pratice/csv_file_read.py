import pandas as pd
from sklearn.model_selection import train_test_split

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("data.csv")  # Replace with the path to your CSV file

# Split the DataFrame into features (X) and labels (y)
# Assuming the target/label is in the last column and the rest are features
X = df.iloc[:, :-1].values  # All columns except the last one (features)
y = df.iloc[:, -1].values   # The last column (target/label)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=42)

# Print the data
print('X_train')
print(X_train)
print("X_test")
print(X_test)
print('y_train')
print(y_train)
print('y_test')
print(y_test)
