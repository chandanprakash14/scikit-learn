from sklearn.impute import SimpleImputer
from sklearn.datasets import fetch_openml
df = fetch_openml('titanic', version=1, as_frame=True)['data']
print(f"Number of null Value before imputing:{df.age.isnull().sum()}")
imp=SimpleImputer(strategy='mean')
df['age']=imp.fit_transform(df[['age']])
print(f"Number of null Value after imputing:{df.age.isnull().sum()}")