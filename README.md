# sqlalchemy-challenge
Assignment 10 - SQL Alchemy

INTRO - Use Hawaii temperature data to create an app.

Part 1 - Precipitation and Station Analysis
Using the 2 data sources, extract the name of the stations, precipitation for the previous year and also run statistic analysis on the data. Find max, min and average values. Use pandas to calculate statistics and matplotlib to plot results. 

Part 2 - Create a Flask App using the information in Part 1
Create a homepage and list possible routs/ urls for the different data. Link those routes to:
1) /api/v1.0/precipitation - Retrive precipitaion values for the last 12 months
2) /api/v1.0/stations - List the unique weather station id's used in this data
3) /api/v1.0/tobs - Using the most active weather station, state the max, min and average temperatures.
4) /api/v1.0/<start> and /api/v1.0/<start>/<end> - Allow user to input start and end date, and have the minimum, maximum and average temperature for the specified date.
Also, use the jsonify function to output clean data. 
