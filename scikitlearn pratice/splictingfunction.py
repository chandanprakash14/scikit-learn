from sklearn.model_selection import train_test_split 
X=list(range(0,15))
y=[x*x for x in X]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=42)
print(X_train)
print(X_test)
print(y_test)
print(y_train)