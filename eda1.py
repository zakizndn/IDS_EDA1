import pandas as pd
import seaborn as sns

mydf = pd.read_csv('mall_customer.csv')
mydf.rename(columns={'Genre': 'Gender'}, inplace=True)
mydf.sample(n = 10)

mydf.describe()

#!pip install sweetviz

# Importing sweetviz library
#import sweetviz as sv

# Analyzing the dataset
#advert_report = sv.analyze(mydf)

# Display the report
#advert_report.show_html('Advertising.html')

#advert_report.show_notebook()

sns.regplot(data = mydf, x = 'Annual_Income_(k$)', y = 'Spending_Score');

sns.boxplot(data = mydf, x = 'Gender', y = 'Annual_Income_(k$)');

corr = mydf.corr(method = 'pearson')
#corr

import matplotlib.pyplot as plt
#%matplotlib inline

plt.figure(figsize=(10,8), dpi =500)
sns.heatmap(corr,annot=True,fmt=".2f", linewidth=.5)
plt.show()
