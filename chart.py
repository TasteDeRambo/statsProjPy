import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('Police_Arrests.csv')

# Filter out empty ages
df = df[df['AgeAtArrestTime'].notna()]

# Convert ages to numbers
df['AgeAtArrestTime'] = pd.to_numeric(df['AgeAtArrestTime'])

# Pie chart
df['AgeAtArrestTime'].value_counts().plot(kind='pie')
plt.title('Pie Chart of Arrest Ages')
plt.show()

# Bar graph
df['AgeAtArrestTime'].value_counts().plot(kind='bar')
plt.title('Bar Graph of Arrest Ages')
plt.show()

# Box plot
df['AgeAtArrestTime'].plot(kind='box')
plt.title('Box Plot of Arrest Ages')
plt.show()

# Relative frequency graph
(df['AgeAtArrestTime'].value_counts() / len(df)).plot(kind='bar')
plt.title('Relative Frequency Graph of Arrest Ages')
plt.show()

# Cumulative frequency
df['AgeAtArrestTime'].value_counts().sort_index().cumsum().plot()
plt.title('Cumulative Frequency of Arrest Ages')
plt.show()

# Histogram
df['AgeAtArrestTime'].plot(kind='hist', bins=20)
plt.title('Histogram of Arrest Ages')
plt.show()
# calculate the most arrest by zip code and get all the ages in that zip code