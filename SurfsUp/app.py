# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

#################################################
# Database Setup
#################################################

# Create engine:
engine = create_engine('sqlite:///Resources/hawaii.sqlite')

# Reflect an existing database into a new model
Base = automap_base()


# Reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Weather API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
    )
# Convert the query results from your precipitation analysis (i.e. retrieve only the 
# last 12 months of data) to a dictionary using date as the key and prcp as the value.
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Calculate the date one year from the last date in data set.
    date = dt.datetime(2017, 8, 23) - dt.timedelta(days=366)

    # query results from your precipitation analysis (i.e. retrieve only the last 12 months of data):
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precipitation 
    dates = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict[date] = prcp
        dates.append(precipitation_dict)
    return jsonify(dates)

# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query Station Names:
    results_station = session.query(Measurement.station).group_by(Measurement.station).all()
    
    session.close()

    # Convert list of tuples into normal list
    station_all = list(np.ravel(results_station))

    return jsonify(station_all)


# Returns jsonified data for the most active station (USC00519281)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query the dates and temperature of the most-active station for the previous year:
    results_tobs= session.query(func.min(Measurement.tobs),func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.station == 'USC00519281').all()

    session.close()

    tobs_all = list(np.ravel(results_tobs))
    
    return jsonify(tobs_all)

    
if __name__ == '__main__':
    app.run(debug=True)
