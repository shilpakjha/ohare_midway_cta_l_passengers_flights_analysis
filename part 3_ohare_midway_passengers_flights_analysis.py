# Part 3 - Airport fligghts and passenger volume analysis
# Get the Data 1 and 2 Files Use API to connect with the portal and get with Data 1 and 2

import pandas as pd
import matplotlib.pyplot as plt
import bokeh as bk
import math
from ast import literal_eval

ohare_midway_flight_traveler_2014_2020_data = pd.read_csv(
    r"/Users/shilpakamath-jha/Desktop/2014_2020_aiprort_flight_traveler_data.csv",
    sep=",",
)
ohare_midway_flight_traveler_2014_2020_data
# Creates a pivot table which now has year as index and flight number data from Ohare and Midway for 2015 to 2020 as columns
# ohare_midway_flight_traveler_2014_2020_data.rename(columns = {"Midway Airport": "midway_no_of_flights", "O'Hare Airport": "ohare_no_of_flights"})


ohare_midway_flights_2014_2020 = ohare_midway_flight_traveler_2014_2020_data.pivot_table(
    "number_flights", "year", ["airport"]
)
ohare_midway_flights_2014_2020.rename(
    columns={
        "Midway Airport": "midway_no_of_flights",
        "O'Hare Airport": "ohare_no_of_flights",
    },
    inplace=True,
)
ohare_midway_flights_2014_2020


# Gives number of flights in 2015 and 2019 with the years as columns for O'Hare and Midway
ohare_midway_2016_2019 = ohare_midway_flights_2014_2020.query(
    "year == [2016, 2019]"
).copy()
ohare_midway_2016_2019
ohare_midway_2016_2019_flights = pd.pivot_table(
    data=ohare_midway_2016_2019,
    columns=["year"],
    values=["midway_no_of_flights", "ohare_no_of_flights"],
).reset_index()
ohare_midway_2016_2019_flights["percent_diff_2016_2019"] = (
    (ohare_midway_2016_2019_flights[2019] - ohare_midway_2016_2019_flights[2016])
    * 100
    / ohare_midway_2016_2019_flights[2016]
)
ohare_midway_2016_2019_flights
# Changes the values to comma and percent format. Datatype changes to object
ohare_midway_2016_2019_flights[2016] = (
    ohare_midway_2016_2019_flights[2016].astype(int).apply(lambda x: "{:,}".format(x))
)
ohare_midway_2016_2019_flights[2019] = (
    ohare_midway_2016_2019_flights[2019].astype(int).apply(lambda x: "{:,}".format(x))
)

ohare_midway_2016_2019_flights["percent_diff_2016_2019"] = (
    ohare_midway_2016_2019_flights["percent_diff_2016_2019"]
    .astype(float)
    .apply(lambda x: "{:.2f}%".format(x))
)
ohare_midway_2016_2019_flights


# O'Hare and Midway Traveler Data comparison between 2015 and 2019
# gives number of travelers and customs agents in 2016 and 2019 with the years as columns

ohare_midway_passengers_2014_2020 = ohare_midway_flight_traveler_2014_2020_data.pivot_table(
    "passenger_volume", "year", ["airport"]
)
ohare_midway_passengers_2014_2020.rename(
    columns={
        "Midway Airport": "midway_passenger_vol",
        "O'Hare Airport": "ohare_passenger_vol",
    },
    inplace=True,
)
ohare_midway_passengers_2014_2020
df_2014_to_2019_passenger = ohare_midway_passengers_2014_2020.query(
    "year == [2016, 2019]"
).copy()
df_2014_to_2019_passenger
ohare_midway_2016_2019_passenger = pd.pivot_table(
    data=df_2014_to_2019_passenger,
    columns=["year"],
    values=["ohare_passenger_vol", "midway_passenger_vol"],
).reset_index()
ohare_midway_2016_2019_passenger["percent_diff_2016_2019"] = (
    (ohare_midway_2016_2019_passenger[2019] - ohare_midway_2016_2019_passenger[2016])
    * 100
    / ohare_midway_2016_2019_passenger[2016]
)
ohare_midway_2016_2019_passenger

# Changes the values to comma and percent format. Datatype changes to object
ohare_midway_2016_2019_passenger[2016] = (
    ohare_midway_2016_2019_passenger[2016].astype(int).apply(lambda x: "{:,}".format(x))
)
ohare_midway_2016_2019_passenger[2019] = (
    ohare_midway_2016_2019_passenger[2019].astype(int).apply(lambda x: "{:,}".format(x))
)

ohare_midway_2016_2019_passenger["percent_diff_2016_2019"] = (
    ohare_midway_2016_2019_passenger["percent_diff_2016_2019"]
    .astype(float)
    .apply(lambda x: "{:.2f}%".format(x))
)
ohare_midway_2016_2019_passenger
