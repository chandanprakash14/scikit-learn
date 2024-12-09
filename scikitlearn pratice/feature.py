import matplotlib.pyplot as plot
from sklearn.impute import SimpleImputer
from sklearn.datasets import fetch_openml
df = fetch_openml('titanic', version=1, as_frame=True)['data']
df['family']=df['sibsp']+df['parch']
df.loc[df['family']>0,'travelled_alone']=0
df.loc[df['family']==0,'travelled_alone']=1
df['travelled_alone'].value_counts().plot(title="Passanger travelled alone?",kind='bar')
plot.show()