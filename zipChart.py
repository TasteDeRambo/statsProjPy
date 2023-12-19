import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('Police_Arrests.csv')

# Filter out rows where 'AgeAtArrestTime' is empty
df = df[df['AgeAtArrestTime'].notna()]

# Find the mode of 'arLZip'
mostArrestZipCode = df['arLZip'].mode()[0]

# Filter the DataFrame for the most arrested zip code
df_most_arrest = df[df['arLZip'] == mostArrestZipCode]

# Plot histogram
plt.hist(df_most_arrest['arLZip'], bins=10, edgecolor='black')
plt.title('Histogram of Most Arrested Zip Code')
plt.show()

# Plot relative frequency histogram
plt.hist(df_most_arrest['arLZip'], bins=10, edgecolor='black', density=True)
plt.title('Relative Frequency Histogram of Most Arrested Zip Code')
plt.show()

# Plot cumulative frequency histogram
plt.hist(df_most_arrest['arLZip'], bins=10, edgecolor='black', cumulative=True)
plt.title('Cumulative Frequency Histogram of Most Arrested Zip Code')
plt.show()

# Plot box plot
plt.boxplot(df_most_arrest['arLZip'])
plt.title('Box Plot of Most Arrested Zip Code')
plt.show()

# Plot bar graph
df_most_arrest['arLZip'].value_counts().plot(kind='bar')
plt.title('Bar Graph of Most Arrested Zip Code')
plt.show()

# Plot pie chart
df_most_arrest['arLZip'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart of Most Arrested Zip Code')
plt.show()
