from sklearn import datasets
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

iris = datasets.load_iris()
X = iris.data
print(X)
y = iris.target
ida = LinearDiscriminantAnalysis(n_components=2) 
X_ida = ida.fit(X, y).transform(X)
print(X_ida)
print("Original number of features:", X.shape[1])
print("Reduced number of features:", X_ida.shape[1])
pd_Frame=pd.DataFrame(X,columns=iris.feature_names)
print(pd_Frame.to_string())
