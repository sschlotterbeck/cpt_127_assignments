"""
File 1 of 2 to accompany: Public Libraries in Maine: A Geospatial Research Project
CPT 127 - Exploring Geospatial Data with GeoPandas
Sylvia Schlotterbeck 7/28/25

This code imports datasets of all libraries and public libraries
in Maine, and harmonizes the discrepancies between the datasets. It also
imports a geoJSON dataset of the Maine state boundary, although I ultimately
did make use the state boundary in my final analysis. 
This code generates two figures:
1) a geospatial distribution of public libraries in Maine 
2) a partial outline of the state of Maine boundary

'query.json' data derived from the MaineGeoLibray
 --accessed on July 17, 2025 at:
https://services1.arcgis.com/RbMX0mRVOFNTdLzd/ArcGIS/rest/services/
Maine_GeoLibrary_Structure/FeatureServer/4/query?where=1%3D1&
objectIds=&geometry=&geometryType=esriGeometryEnvelope&inSR=&
spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&
units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=&
returnGeometry=true&featureEncoding=esriDefault&
multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&
defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&
returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&
returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&collation=&
orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&
resultRecordCount=&returnZ=false&returnM=false&returnTrueCurves=false&
returnExceededLimitFeatures=true&quantizationParameters=&
sqlFormat=none&f=pgeojson&token=

'maine_public_library_list_w_counties.csv' data derived from the Maine State Library
Public Library Directory -- accessed on July 17, 2025 at
https://www.maine.gov/msl/libs/directories/public.shtml. I copied the list of
libraries from the page, pasted it into a spreadsheet, and saved it as a csv.

'query_maine_state_boundary.json' derived from the MaineGeoLibrary 
--accessed on July 17, 2025 at:
https://services1.arcgis.com/RbMX0mRVOFNTdLzd/ArcGIS/rest/services/
Maine_State_Boundary_Line/FeatureServer/query?layerDefs=1%3D1&geometry=&
geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&outSR=&
datumTransformation=&applyVCSProjection=false&returnGeometry=true&maxAllowableOffset=&
geometryPrecision=&returnIdsOnly=false&returnCountOnly=false&returnDistinctValues=false&
returnZ=false&returnM=false&sqlFormat=none&f=pjson&token=
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# read file of public libraries in Maine into a DataFrame and strip
# extraneous spaces on left and right
pub_libs = pd.read_csv("maine_public_library_list_w_counties.csv")
pub_libs['Library'] = pub_libs['Library'].str.strip()

# read the geoJSON file of all libraries in Maine from the Maine GeoLibrary
# database and strip extraneous spaces on left and right
data = gpd.read_file("query.json")
data['Name'] = data['Name'].str.strip()

"""
Note: I left this next section in the code since it is what I did to compare the two
library lists and make all the name changes, typo fixes, and adjustments necessary to
harmonize the two lists of libraries so that when I used the '.isin()' method again
to create the final version of my GeoDataFrame for plotting, all the public libraries
in the public list would be properly recognized.
"""

#convert file of all libraries to a DataFrame for comparison with the dataset of public libraries
all_libs = data['Name']
all_libs = pd.DataFrame(all_libs)

# create two separate DataFrames for the libraries that overlap and those that don't
# to allow further examination for any discrepencies in format or punctuation
all_pub_libs = all_libs[all_libs['Name'].isin(pub_libs['Library'])]
not_pub_libs = all_libs[~all_libs['Name'].isin(pub_libs['Library'])]

# export DataFrame of matching libraries as a csv file for further examination and comparison
all_pub_lib_names = all_pub_libs['Name']
all_pub_lib_names.to_csv('all_pub_libs.csv', index=False)

# export DataFrame of non-matching libraries as a csv file for further examination and comparison
not_pub_lib_names = not_pub_libs['Name']
not_pub_lib_names.to_csv('not_pub_libs.csv', index=False)

"""
End of the section used to process and export the library lists as csv files for comparison
"""

# adjust library names to harmonize with Maine GeoLibrary library names
pub_libs['Library'] = pub_libs['Library'].str.replace('.', ' ')
pub_libs['Library'] = pub_libs['Library'].str.replace('  ', ' ')
pub_libs['Library'] = pub_libs['Library'].str.replace('&', 'and')
pub_libs['Library'] = pub_libs['Library'].str.replace('Brownville Free Public Library', 'Brownville Public Library')
pub_libs['Library'] = pub_libs['Library'].str.replace('Brown Memorial Library - Clinton', 'Brown Memorial Library')
pub_libs['Library'] = pub_libs['Library'].str.replace('Brown Memorial Library - East Baldwin', 'Brown Memorial Library')
pub_libs['Library'] = pub_libs['Library'].str.replace('Shaw Public Library - Greenville', 'Shaw Public Library')
pub_libs['Library'] = pub_libs['Library'].str.replace('Shaw Public Library - Mercer', 'Shaw Public Library')
pub_libs['Library'] = pub_libs['Library'].str.replace('Stetson Library', 'Stetson Public Library')
pub_libs['Library'] = pub_libs['Library'].str.replace('South Portland Public Library - Memorial Branch Library', 'South Portland Public Library - Memorial Branch')

# format the 'Name' column so it is stripped of potential spaces on
# the left and right, and then pull it out and turn it into a pandas DataFrame.
data['Name'] = data['Name'].str.replace('&', 'and')
data['Name'] = data['Name'].str.replace('  ', ' ')
data['Name'] = data['Name'].str.replace('Pubilc', 'Public')
data['Name'] = data['Name'].str.replace('Abbot', 'Abbott')
data['Name'] = data['Name'].str.replace('Jessup', 'Jesup')
data['Name'] = data['Name'].str.replace('Ivan O Davis-', '')
data['Name'] = data['Name'].str.replace("Orr`s Island Library", "Orr's Island Library")
data['Name'] = data['Name'].str.replace("Lisbon Library Department", "Lisbon Library")
data['Name'] = data['Name'].str.replace("Webster Free Library", "Webster Library")
data['Name'] = data['Name'].str.replace("Mexico Free Public Library", "Mexico Public Library")
data['Name'] = data['Name'].str.replace("Norridgewock Free Public Library", "Norridgewock Public Library")
data['Name'] = data['Name'].str.replace("Lithgow Library", "Lithgow Public Library")
data['Name'] = data['Name'].str.replace("Coolidge Library", "Coolidge Public Library")
data['Name'] = data['Name'].str.replace("Edythe L Dyer Community Library", "Edythe Dyer Community Library")
data['Name'] = data['Name'].str.replace("Ashland Community Library", "Gladys J Craig Memorial Library")
data['Name'] = data['Name'].str.replace("Newport Cultural Center", "Newport Public Library - Newport Cultural Center")
data['Name'] = data['Name'].str.replace("Somerville Town Library", "Whitefield Library")
data['Name'] = data['Name'].str.replace("South Portland Public Library Memorial Branch", "South Portland Public Library - Memorial Branch")

# create a new GeoDataFrame that contains only the harmonized dataset of 
# public libraries
data_select = data[data['Name'].isin(pub_libs['Library'])]

# load a file containing a dataset of the Maine state boundary from the 
#Maine GeoLibrary database
state_boundary = gpd.read_file('query_maine_state_boundary.json')

# check that crs formats of the two GeoDataFrames match one another
state_boundary.crs
data_select.crs

#plot state boundary GeoDataFrame
state_boundary.plot(color='black', figsize=(15,9))

#plot Maine public libraries GeoDataFrame
data_select.plot(color='black', figsize=(15,9), marker='*', markersize=10)

"""
In the next section here, I attempted to alter the parameters and shapes of the state boundary
and public libraries figures so that I could more easily overlay the distribution of libraries 
onto a pre-existing population distribution map of Maine, but I was unsuccessful in my attempts. 
I left this in here as a record of what I tried, in case I can figure out what I did wrong or need to
do in the future. 
"""
# create a figure to plot both data_select and state_boundary onto
fig, axs = plt.subplots(1, 2, figsize=(15, 9))

# plot data_select (public library locations in Maine)
data_select.plot(ax=axs[0], color='black', marker='*', markersize=10)

# plot state_boundary (partial outline of Maine, with the same crs format as
# data_select, so data_select can be lined up with the state boundary outline
# and then placed onto a figure of Maine population density in the correct
# place 
state_boundary.plot(ax=axs[1], color='black')

# set the same width for both plots, so the scale is the same for both
# (the state boundary data is incomplete, so its height is different)
for ax in axs:
    ax.set_aspect(aspect='equal', adjustable='datalim')

# adjust the layout to automatically adjust subplot parameters for a better fit
plt.tight_layout()

#saves the plotted figure
side_by_side_maps = plt.savefig

# display the side-by-side figures
plt.show()