# datafun-06-eda

# Overview
Project 6 is an opportunity to create your own custom exploratory data analysis (EDA) project using GitHub, Git, Jupyter, pandas, Seaborn and other popular data analytics tools.

# Objectives
1) to create a dataset from publicly available weather data
2) to explore what states have the most events related to thunderstorms.  This includes wind, hail, lightning, and tornados.
3) 

# Questions that I want to answer
1) Do some states have more tornadoes than other states?
2) Do all tornados result in injuries or death?
3) Do stronger tornados have more deaths?
4) 

# Lessons learned
- Don't try to upload large csv files to github.  It is a big hassle to try and fix this!
- data format is really important.  It took a lot of detective work to join the fips codes between my two data sets.  One was an object, the other a float.  


# Data Sources
https://www.ncdc.noaa.gov/stormevents/
https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html 

# Metadata
Information about the database
https://www.ncdc.noaa.gov/stormevents/details.jsp

The database structure from NOAA was changed in 1996.  Only the years 1998-2024 were included in this download so this is not a concern; however, NOAA has digitized records going further back in time.

Information about event types
https://www.ncdc.noaa.gov/stormevents/pd01016005curr.pdf
