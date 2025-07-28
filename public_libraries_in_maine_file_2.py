"""
File 2 of 2 to accompany: Public Libraries in Maine: A Geospatial Research Project
CPT 127 - Exploring Geospatial Data with GeoPandas
Sylvia Schlotterbeck 7/28/25

This code imports datasets of public libraries and county statistics
in Maine, and generates two bar graphs that display:
1) libraries per square mile by county 
2) libraries per square mile divided by people per square mile by county
"""

import pandas as pd
import matplotlib.pyplot as plt

# read file of public libraries in Maine into a DataFrame
pub_libs = pd.read_csv("maine_public_library_list_w_counties.csv")

# get count of number of public libraries in each county
county_counts = pub_libs['County'].value_counts()

# convert county_counts from a DataSeries into a DataFrame
county_counts_df = pd.DataFrame(county_counts)

county_counts_df = county_counts_df.reset_index()
county_counts_df.rename(columns={'count': 'Libraries'}, inplace=True)

maine_counties = pd.read_csv('maine_county_stats.csv')
maine_counties['County'] = maine_counties['County'].str.replace(" County", "")

county_counts_df_sorted = county_counts_df.sort_values(by='County', ascending=True)
county_counts_df_sorted = county_counts_df_sorted.reset_index()
del county_counts_df_sorted['index']
county_counts_df_sorted.rename(columns={'County': 'county'}, inplace=True)

maine_counties_merged = maine_counties.join(county_counts_df_sorted)
del maine_counties_merged['county']

maine_counties_merged['Population Density (people/sq mi)'] = maine_counties_merged['Population'] / maine_counties_merged['Area (sq mi)']
maine_counties_merged['Library Density (libraries/sq mi)'] = maine_counties_merged['Libraries'] / maine_counties_merged['Area (sq mi)']
maine_counties_merged['Library to Population Density Ratio (Library Density/Population Density)'] = maine_counties_merged['Library Density (libraries/sq mi)'] / maine_counties_merged['Population Density (people/sq mi)']
maine_counties_merged = maine_counties_merged.set_index('County')

maine_counties_to_plot = maine_counties_merged[['Population Density (people/sq mi)', 'Library Density (libraries/sq mi)', 'Library to Population Density Ratio (Library Density/Population Density)']]
maine_counties_to_plot_sorted = maine_counties_to_plot.sort_values('Population Density (people/sq mi)', ascending=False)

maine_counties_to_plot_sorted['Library Density (libraries/sq mi)'].plot(kind='bar', title='Maine Public Library Density by County', xlabel='County (sorted by Population Density from left to right)', ylabel='Libraries/sq mi)', color = 'brown')
maine_counties_to_plot_sorted['Library to Population Density Ratio (Library Density/Population Density)'].plot(kind='bar', title='Maine Public Library Density to Population Density Ratio by County', xlabel ='County (sorted by Population Density from left to right)', ylabel='Library Density/Population Density', color='blue')