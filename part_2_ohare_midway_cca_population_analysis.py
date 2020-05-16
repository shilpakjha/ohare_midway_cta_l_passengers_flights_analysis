# Part 2- CCA POpulation analysis
# Get the Data 1 and 2 Files Use API to connect with the portal and get with Data 1 and 2
import pandas as pd
import matplotlib.pyplot as plt
import bokeh as bk
import math
from ast import literal_eval

# O'Hare and Midway Population change from 2000 to 2017 and from 2010 to 2017
# CCA for O'Hare is 76
# CCA for Midway is 56

ohare_midway_cca_census = pd.read_csv(
    "/Users/shilpakamath-jha/Desktop/SKJhaPythonProjects/ReferenceCCAProfiles20132017mergedCCAcopy.csv",
    sep=",",
)
ohare_midway_cca_census.sort_values(
    ascending=True, by="chi_community_areas", inplace=True
)
ohare_midway_cca_census
cca_data = pd.pivot_table(
    data=ohare_midway_cca_census,
    index=["chi_community_areas", "GEOG"],
    values=["2000_POP", "2010_POP", "TOT_POP"],
)
cca_data["percent_diff_2017_2000"] = (
    (cca_data["TOT_POP"] - cca_data["2000_POP"]) * 100 / cca_data["2000_POP"]
)
cca_data["percent_diff_2017_2010"] = (
    (cca_data["TOT_POP"] - cca_data["2010_POP"]) * 100 / cca_data["2010_POP"]
)
cca_data
pop_change_cca_56and76 = cca_data.query("chi_community_areas == [56,76]").copy()
pop_change_cca_56and76.sort_values(
    ascending=False, by="percent_diff_2017_2010", inplace=True
)
pop_change_cca_56and76
# Change the values to the comma and percent format
pop_change_cca_56and76["2000_POP"] = (
    pop_change_cca_56and76["2000_POP"].astype(int).apply(lambda x: "{:,}".format(x))
)
pop_change_cca_56and76["2010_POP"] = (
    pop_change_cca_56and76["2010_POP"].astype(int).apply(lambda x: "{:,}".format(x))
)
pop_change_cca_56and76["TOT_POP"] = (
    pop_change_cca_56and76["TOT_POP"].astype(int).apply(lambda x: "{:,}".format(x))
)
pop_change_cca_56and76["percent_diff_2017_2000"] = (
    pop_change_cca_56and76["percent_diff_2017_2000"]
    .astype(float)
    .apply(lambda x: "{:.2f}%".format(x))
)
pop_change_cca_56and76["percent_diff_2017_2010"] = (
    pop_change_cca_56and76["percent_diff_2017_2010"]
    .astype(float)
    .apply(lambda x: "{:.2f}%".format(x))
)
# Final table which shows the 2000 pop, 2010 pop, 2017 population.
# Provides the percent change in pop from 2000 to 2017 and from 2010 to 2017

pop_change_cca_56and76
