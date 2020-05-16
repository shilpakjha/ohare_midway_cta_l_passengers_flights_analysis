# Part 5 - O'Hare L-rides, taxi and tnp rides 2019

import pandas as pd
import matplotlib.pyplot as plt
import bokeh as bk
from bokeh.plotting import figure, show, output_notebook
from bokeh.tile_providers import get_provider, Vendors

get_provider(Vendors.CARTODBPOSITRON)
from bokeh.models import ColumnDataSource, HoverTool
import math
from ast import literal_eval

chi_taxi_tnp_2019 = pd.read_csv(
    r"/Users/shilpakamath-jha/Desktop/chi_lrides_taxi_tnp_2019_airport_pick_drop_rides.csv",
    sep=",",
)
chi_taxi_tnp_2019
chi_taxi_tnp_2019_ohare = chi_taxi_tnp_2019.copy()
chi_taxi_tnp_2019_ohare_pu_do = chi_taxi_tnp_2019_ohare[
    chi_taxi_tnp_2019_ohare["airport"].isin(["O'Hare Airport"])
]
chi_taxi_tnp_2019_ohare_pu_do1 = chi_taxi_tnp_2019_ohare_pu_do.copy()
chi_taxi_tnp_2019_ohare_pu_do1
chi_taxi_tnp_2019_ohare_pu_do1["pick_up_taxi_tnp_comp"] = (
    chi_taxi_tnp_2019_ohare_pu_do1["taxi_pick_up_rides"] * 100
) / (
    chi_taxi_tnp_2019_ohare_pu_do1["tnp_pick_up_rides"]
    + chi_taxi_tnp_2019_ohare_pu_do1["taxi_pick_up_rides"]
)
chi_taxi_tnp_2019_ohare_pu_do1["drop_off_taxi_tnp_comp"] = (
    chi_taxi_tnp_2019_ohare_pu_do1["taxi_drop_off_rides"] * 100
) / (
    chi_taxi_tnp_2019_ohare_pu_do1["tnp_drop_off_rides"]
    + chi_taxi_tnp_2019_ohare_pu_do1["taxi_drop_off_rides"]
)
chi_taxi_tnp_2019_ohare_pu_do1.sort_values(
    ascending=False, by="pick_up_taxi_tnp_comp", inplace=True
)
chi_taxi_tnp_2019_ohare_pu_do1

chi_taxi_tnp_2019_ohare_pu_do1["l_rides"] = (
    chi_taxi_tnp_2019_ohare_pu_do1["l_rides"]
    .astype(int)
    .apply(lambda x: "{:,}".format(x))
)
chi_taxi_tnp_2019_ohare_pu_do1["tnp_pick_up_rides"] = (
    chi_taxi_tnp_2019_ohare_pu_do1["tnp_pick_up_rides"]
    .astype(int)
    .apply(lambda x: "{:,}".format(x))
)
chi_taxi_tnp_2019_ohare_pu_do1["tnp_drop_off_rides"] = (
    chi_taxi_tnp_2019_ohare_pu_do1["tnp_drop_off_rides"]
    .astype(int)
    .apply(lambda x: "{:,}".format(x))
)
chi_taxi_tnp_2019_ohare_pu_do1["taxi_pick_up_rides"] = (
    chi_taxi_tnp_2019_ohare_pu_do1["taxi_pick_up_rides"]
    .astype(int)
    .apply(lambda x: "{:,}".format(x))
)
# chi_taxi_tnp_2019_ohare_pu_do1['taxi_drop_off_rides'] = chi_taxi_tnp_2019_ohare_pu_do1['taxi_drop_off_rides'].astype(int).apply(lambda x: "{:,}".format(x))
chi_taxi_tnp_2019_ohare_pu_do1["pick_up_taxi_tnp_comp"] = (
    chi_taxi_tnp_2019_ohare_pu_do1["pick_up_taxi_tnp_comp"]
    .astype(float)
    .apply(lambda x: "{:.2f}%".format(x))
)
chi_taxi_tnp_2019_ohare_pu_do1["drop_off_taxi_tnp_comp"] = (
    chi_taxi_tnp_2019_ohare_pu_do1["drop_off_taxi_tnp_comp"]
    .astype(float)
    .apply(lambda x: "{:.2f}%".format(x))
)

chi_taxi_tnp_2019_ohare_pu_do1

chi_taxi_tnp_2019_ohare_pu_do1["taxi_drop_off_rides"] = (
    chi_taxi_tnp_2019_ohare_pu_do1["taxi_drop_off_rides"]
    .astype(int)
    .apply(lambda x: "{:,}".format(x))
)

chi_taxi_tnp_2019_ohare_pu_do1
