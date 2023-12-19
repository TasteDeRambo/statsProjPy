import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('Police_Arrests.csv', dtype={30: str, 45: str, 46: str})

# Filter out rows with empty 'AgeAtArrestTime'
df = df[df['AgeAtArrestTime'].notna()]

# Group by 'ArLZip' and get the mode, mean of 'AgeAtArrestTime'
zipCodeAges = df.groupby('ArLZip')['AgeAtArrestTime'].agg(['mean', lambda x: x.mode().iloc[0]])

# Find the 'ArLZip' with the most arrests
mostArrestZipCode = df['ArLZip'].mode().iloc[0]

# Get 'AgeAtArrestTime' for the 'ArLZip' with the most arrests
arrestAgesInZip = df[df['ArLZip'] == mostArrestZipCode]['AgeAtArrestTime']

# Plot histogram
plt.figure(figsize=(12, 8))
plt.hist(arrestAgesInZip, bins=20, edgecolor='black')
plt.title('Histogram of Arrest Ages in Zip Code ' + str(mostArrestZipCode))
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plot box plot
plt.figure(figsize=(12, 8))
plt.boxplot(arrestAgesInZip)
plt.title('Box Plot of Arrest Ages in Zip Code ' + str(mostArrestZipCode))
plt.ylabel('Age')
plt.show()

# Plot pie chart
plt.figure(figsize=(12, 8))
arrestAgesInZip.value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart of Arrest Ages in Zip Code ' + str(mostArrestZipCode))
plt.ylabel('')
plt.show()

# Plot cumulative frequency
plt.figure(figsize=(12, 8))
plt.hist(arrestAgesInZip, bins=20, edgecolor='black', cumulative=True)
plt.title('Cumulative Frequency of Arrest Ages in Zip Code ' + str(mostArrestZipCode))
plt.xlabel('Age')
plt.ylabel('Cumulative Frequency')
plt.show()

# Plot relative frequency
plt.figure(figsize=(12, 8))
plt.hist(arrestAgesInZip, bins=20, edgecolor='black', weights=np.ones(len(arrestAgesInZip)) / len(arrestAgesInZip))
plt.title('Relative Frequency of Arrest Ages in Zip Code ' + str(mostArrestZipCode))
plt.xlabel('Age')
plt.ylabel('Relative Frequency')
plt.show()

# Plot bar graph
plt.figure(figsize=(12, 8))
arrestAgesInZip.value_counts().plot(kind='bar')
plt.title('Bar Graph of Arrest Ages in Zip Code ' + str(mostArrestZipCode))
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
