import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

# Load the data
mydf = pd.read_csv('mall_customer.csv')
mydf.rename(columns={'Genre': 'Gender'}, inplace=True)

# Display a sample of the data
st.write("#### Sample of the Data")
st.write(mydf.sample(n=10))

# Display descriptive statistics
st.write("#### Descriptive Statistics")
st.write(mydf.describe())

# Display a scatter plot
st.write("#### Scatter Plot: Annual Income vs Spending Score")
fig, ax = plt.subplots()
sns.regplot(data=mydf, x='Annual_Income_(k$)', y='Spending_Score', ax=ax)
st.pyplot(fig)

# Display a box plot
st.write("#### Box Plot: Annual Income by Gender")
fig, ax = plt.subplots()
sns.boxplot(data=mydf, x='Gender', y='Annual_Income_(k$'), ax=ax)
st.pyplot(fig)
