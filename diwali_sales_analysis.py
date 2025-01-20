# Updated Code with Fixed Warnings and Full-Width Occupation Plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import CSV file
df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')

# Data Cleaning
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
df.dropna(inplace=True)
df['Amount'] = df['Amount'].astype('int')
df.rename(columns={'Marital_Status': 'Shaadi'}, inplace=True)

# Set the figure size for the overall plot
fig = plt.figure(figsize=(20, 25))
fig.suptitle('Diwali Sales Analysis', fontsize=24, y=0.95)

# GENDER
ax1 = plt.subplot2grid((5, 2), (0, 0))
sns.countplot(x='Gender', data=df, palette='Set2', ax=ax1, hue=None, legend=False)
ax1.set_title('Count of Buyers by Gender', fontsize=14)
ax1.set_xlabel('Gender')
ax1.set_ylabel('Count')

ax2 = plt.subplot2grid((5, 2), (0, 1))
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender', y='Amount', data=sales_gen, palette='coolwarm', ax=ax2, hue=None, legend=False)
ax2.set_title('Total Sales by Gender', fontsize=14)
ax2.set_xlabel('Gender')
ax2.set_ylabel('Total Amount')

# AGE
ax3 = plt.subplot2grid((5, 2), (1, 0))
sns.countplot(data=df, x='Age Group', hue='Gender', palette='pastel', ax=ax3)
ax3.set_title('Count of Buyers by Age Group and Gender', fontsize=14)
ax3.set_xlabel('Age Group')
ax3.set_ylabel('Count')

ax4 = plt.subplot2grid((5, 2), (1, 1))
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount', data=sales_age, palette='viridis', ax=ax4, hue=None, legend=False)
ax4.set_title('Total Sales by Age Group', fontsize=14)
ax4.set_xlabel('Age Group')
ax4.set_ylabel('Total Amount')

# STATE
ax5 = plt.subplot2grid((5, 2), (2, 0))
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(5)
sns.barplot(data=sales_state, x='State', y='Orders', palette='Blues_d', ax=ax5, hue=None, legend=False)
ax5.set_title('Top 10 States by Number of Orders', fontsize=14)
ax5.set_xlabel('State')
ax5.set_ylabel('Number of Orders')

ax6 = plt.subplot2grid((5, 2), (2, 1))
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(5)
sns.barplot(data=sales_state, x='State', y='Amount', palette='Reds_d', ax=ax6, hue=None, legend=False)
ax6.set_title('Top 10 States by Total Sales', fontsize=14)
ax6.set_xlabel('State')
ax6.set_ylabel('Total Amount')

# OCCUPATION (Full-Width Plot)
ax7 = plt.subplot2grid((5, 2), (3, 0), colspan=2)
sns.countplot(data=df, x='Occupation', palette='Set3', ax=ax7, hue=None, legend=False)
ax7.set_title('Count of Buyers by Occupation', fontsize=14)
ax7.set_xlabel('Occupation')
ax7.set_ylabel('Count')

# Adjust layout to prevent overlap and add padding
plt.subplots_adjust(wspace=1, hspace=1.5)

# Show the plot
plt.show()
