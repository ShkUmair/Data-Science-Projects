import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



df = pd.read_csv('adult.csv')
df.head(10)

df.shape


df.dtypes

df.nunique()

df.describe().T

df['workclass'].value_counts()

df.columns

df['occupation'].value_counts()

df['native.country'].value_counts()

df['marital.status'].value_counts()

df['race'].value_counts()

df['income'].value_counts()

df['sex'].value_counts()

df['education'].value_counts()



HISTOGRAM


df.hist(figsize=(12,12), layout=(3,3), sharex=False);

sns.heatmap(df.corr(), annot=True);


BOX PLOT


df.plot(kind='box', figsize=(12,12), layout=(3,3), sharex=False, subplots=True);


