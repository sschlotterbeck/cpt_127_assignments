# Sylvia Schlotterbeck - 7/6/25 - CPT 127
# "Analyzing Electric Car Sales Using Pandas"

import pandas as pd

# 1. Read the CSV file EcarSalesByCountryAndYear.csv into a DataFrame,
#    display the full DataFrame.
e_cars_df = pd.read_csv('EcarSalesByCountryAndYear.csv')
print(e_cars_df)
print()

# 2. Re-read the same CSV file, this time setting Country as the index of the
#    DataFrame; display the updated DataFrame.
e_cars_df = pd.read_csv('EcarSalesByCountryAndYear.csv', index_col='Country')
print(e_cars_df)
print()

# 3. Calculate the sales growth between 2021 and 2020 using the formula:
#    Growth = (Sales2021 - Sales2020) / Sales2020;
#    Add a new column to the DataFrame called 'Growth'.
Growth = (e_cars_df.Sales2021 - e_cars_df.Sales2020) / e_cars_df.Sales2020
e_cars_df['Growth'] = Growth

# 4. Rescale the growth column to show percentages (e.g., 0.25 becomes 25.0).
Growth = Growth * 100
e_cars_df['Growth'] = Growth

# 5. Round the values in the Growth column to 1 decimal place.
Growth = round(Growth, 1)
e_cars_df['Growth'] = Growth

# 6. Display the DataFrame sorted by the Growth column, from highest to lowest.
sorted_df = e_cars_df.sort_values('Growth', ascending = False)
print(sorted_df)
print()

# 7. Create a new DataFrame called dfRecent that only includes the columns
#    Sales2020 and Sales2021.
dfSales2021 = pd.DataFrame(sorted_df['Sales2021'])
dfSales2020 = pd.DataFrame(sorted_df['Sales2020'])
dfRecent = dfSales2021.join(dfSales2020)
print(dfRecent)
print()

# 8. Filter dfRecent to display only the rows for United States and Canada.
print(dfRecent[(dfRecent.index == 'United States') | (dfRecent.index == 'Canada')])

# 9. Use dfRecent to display the total global sales in 2020 and 2021
#    (across all countries in the dataset).
print(dfRecent.sum())

# 10. Group the original DataFrame by Continent and calculate total sales by year
#     for each continent.
print(e_cars_df)
Continents = ['North Am.', 'Asia', 'Europe', 'Europe', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe', 'North Am.']
dfContinents = pd.DataFrame(Continents)
dfContinents.columns = ['Continent']
dfContinents = dfContinents.set_index(e_cars_df.index)
e_cars_df['Continent'] = dfContinents['Continent']
grouped_totals_df = e_cars_df.groupby('Continent').sum()
del grouped_totals_df['Growth']
print(grouped_totals_df)
