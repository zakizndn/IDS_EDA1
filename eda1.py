import pandas as pd
import seaborn as sns

mydf = pd.read_csv('mall_customer.csv')
mydf.rename(columns={'Genre': 'Gender'}, inplace=True)
mydf.sample(n = 10)

mydf.describe()

!pip install sweetviz

# Importing sweetviz library
import sweetviz as sv

# Analyzing the dataset
advert_report = sv.analyze(mydf)

# Display the report
advert_report.show_html('Advertising.html')

advert_report.show_notebook()

# Save the notebook as an image
image_path = 'Advertising_Report.png'
advert_report.show_html(image_path)

# Display the image in the notebook
display(Image(filename=image_path))

"""
GROUP 1

Descriptive Question
- What is the average spending score?


Exploratory Question
- What is the relationship between annual income and spending score?

Inferential
- Given that male customers has a higher mean annual income than female. Is this true for Europe population?

Predictive
- Which gender will be having a higher mean spending score in the next year?

Casual Question
- Will an increase in annual income increase the spending score?

Mechanistic Question
- How a higher annual income lead to a higher spending score?
"""

sns.regplot(data = mydf, x = 'Annual_Income_(k$)', y = 'Spending_Score');

sns.boxplot(data = mydf, x = 'Gender', y = 'Annual_Income_(k$)');

corr = mydf.corr(method = 'pearson')
corr

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

plt.figure(figsize=(10,8), dpi =500)
sns.heatmap(corr,annot=True,fmt=".2f", linewidth=.5)
plt.show()