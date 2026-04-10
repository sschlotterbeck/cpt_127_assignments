# Sylvia Schlotterbeck 8-12-25
# CPT 127 - Final Exam

"""
This program is my code for the final exam of CPT 127 - Summer Term.
I included the instructions for each step listed in the description of the exam
as comments in the code, and also added my own comments for steps that include
multiple actions to accomplish.
"""

import pandas as pd
import matplotlib.pyplot as plt


# (1 of 10) Read the CSV file into a single Pandas DataFrame using the appropriate join (5 points)

# read each csv file into a separate DataFrame
e_cars_sales_df = pd.read_csv('EcarSalesByCountryAndYear.csv')
countries_df = pd.read_csv('countries.csv') 
# set the index of each DataFrame to their column "Country", so they
# have the same index and can be properly joined together
e_cars_sales_df = e_cars_sales_df.set_index('Country')
countries_df = countries_df.set_index('Country')
# join countries_df with e_cars_sales_df into a single DataFrame
e_cars_sales_joined_df = countries_df.join(e_cars_sales_df)

# (2 of 10) Read the CSV file into a Pandas DataFrame and display the first 5 rows. (5 points)
e_cars_sales_joined_df.head()

# (3 of 10) Write a function called calculate_growth(df) that:
# • Adds a column Growth calculated as: (Sales2021 ‐ Sales2020) / Sales2020
# • Converts growth to a percentage and rounds to 1 decimal place
# • Returns the updated DataFrame
# (10 points)

# Adds a column Growth calculated as: (Sales2021 ‐ Sales2020) / Sales2020
Growth = (e_cars_sales_joined_df.Sales2021 - e_cars_sales_joined_df.Sales2020) / e_cars_sales_joined_df.Sales2020
e_cars_sales_joined_df['Growth'] = Growth
# converts 'Growth' column to a percentage
e_cars_sales_joined_df['Growth'] = e_cars_sales_joined_df['Growth'] * 100
# rounds 'Growth' column to one decimal place
e_cars_sales_joined_df['Growth'] = e_cars_sales_joined_df['Growth'].round(1)
# prints the updated DataFrame
print(e_cars_sales_joined_df)

# (4 of 10) Sort the DataFrame by Growth from highest to lowest and display the result. (5 points)
sorted_by_growth_df = e_cars_sales_joined_df.sort_values('Growth', ascending = False)
print(sorted_by_growth_df)

# (5 of 10) What country had the highest sales growth from 2020 to 2021? Print this with a one‐line explanation. (5 points)
print("China had the highest sales growth from 2020 to 2021, with a growth of", sorted_by_growth_df.at['China', 'Growth'], "percent.")

# (6 of 10) Create a new DataFrame called dfRecent containing only the columns Sales2020 and Sales2021. (2 points)
sales_2021_df = pd.DataFrame(sorted_by_growth_df['Sales2021'])
sales_2020_df = pd.DataFrame(sorted_by_growth_df['Sales2020'])
dfRecent = sales_2021_df.join(sales_2020_df)

# (7 of 10) From dfRecent, display only the data for United States and Canada. (3 points)
print(dfRecent[(dfRecent.index == 'United States') | (dfRecent.index == 'Canada')])

# (8 of 10) Use dfRecent to calculate and display the total sales for 2020 and 2021 across all countries. (5 points)
print(dfRecent.sum())

# (9 of 10) Group the original DataFrame by Continent and show the total sales for each year (2019, 2020, 2021). (5 points)

# group original DataFrame by continent and sum values for the groups for each column
grouped_df = e_cars_sales_joined_df.groupby('Continent').sum()
# deletes 'Growth' column so the grouped_df only displays sales by year for each continent 
del grouped_df['Growth']
# displays the total sales for each year by continent
print(grouped_df)

# (10 of 10) Based on your group‐by results, calculate and display the growth percentage by continent from 2020 to 2021
# (rounded to 1 decimal place). (5 points)

# calculate sales growth by continent from 2020 to 2021
growth_by_continent = (grouped_df.Sales2021 - grouped_df.Sales2020) / grouped_df.Sales2020
# add sales by continent data column to the grouped by continent DataFrame
grouped_df['Growth from 2020 to 2021'] = growth_by_continent
# convert the sale growth data from a decimal to a percent, rounded to one decimal place
grouped_df['Growth from 2020 to 2021'] = (grouped_df['Growth from 2020 to 2021'] * 100).round(1)
# create a new data frame in preparation to display the sales growth data by continent
growth_by_continent_display_df = grouped_df
# drop columns other than the growth column
growth_by_continent_display_df.drop(columns=['Sales2021', 'Sales2020', 'Sales2019', 'Sales2018', 'Sales2017'], inplace=True)
# rename the growth column to percent growth for clarity
growth_by_continent_display_df.rename(columns={'Growth from 2020 to 2021': 'Percent Growth from 2020 to 2021'}, inplace=True)
# display the percent growth by continent from 2020 to 2021
print(growth_by_continent_display_df)

# Bonus (Optional, up to +5 points)
# Create a simple bar chart using Matplotlib or Pandas showing total 2021 sales by continent.
grouped_df.plot(kind='bar', xlabel='Continent', ylabel='Percent Growth 2020 to 2021', title="Sales Growth of Electric Vehicles from 2020 to 2021", legend=False, color='green')

