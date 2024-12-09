'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
df=fetch_openml('titanic',version=1,as_frame=True)['data']
sns.set_theme()
miss_val_per = (df.isnull().sum() / len(df)) * 100
miss_val_per.plt(kind="bar",title="Missing Values in percentage",ylabel='percentage')
plt.show()'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

# Load Titanic dataset
df = fetch_openml('titanic', version=1, as_frame=True)['data']
sns.set_theme()
miss_val_per = (df.isnull().sum() / len(df)) * 100

# Plot missing values as a bar chart
miss_val_per.plot(kind="bar",  color='skyblue')
plt.title("Missing Values in Percentage")
plt.ylabel("Percentage")
plt.xlabel("Features")
plt.show()
