from sklearn.preprocessing import OneHotEncoder
from sklearn.datasets import fetch_openml
df = fetch_openml('titanic', version=1, as_frame=True)['data']
df[['female','male']]=OneHotEncoder().fit_transform(df[['sex']]).toarray()
df[['sex','female','male']]