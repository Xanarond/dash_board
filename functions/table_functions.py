import os

import numpy as np
import pandas as pd

lower_limits = {
    'CO2': 200,
    'CO': 0.01,
    'NO': 0.001,
    'Temperature': 25,
    'Humidity': 23,
    'Pressure': 983,
    'Spirometry': 0.1
}

upper_limits = {
    'CO2': 10000,
    'CO': 50,
    'NO': 0.1,
    'Temperature': 40,
    'Humidity': 80,
    'Pressure': 1020,
    'Spirometry': 2.5
}


# Pointed functions
# CO

def CO_mean(data_csv, json_table=''):
    return data_csv["CO"].mean(), "Average"


def CO_min(data_csv, json_table):
    return data_csv["CO"].min(), "Minimum"


def CO_max(data_csv, json_table):
    return data_csv["CO"].max(), "Maximum"


def CO_var(data_csv, json_table):
    return data_csv["CO"].var(), "Variance"


def CO_mode(data_csv, json_table):
    return data_csv["CO"].mode().iloc[0], "Mode"


def CO_top_5_percent_mean(data_csv, json_table):
    return data_csv["CO"][data_csv["CO"] > data_csv["CO"].quantile(0.95)].mean(), "Top 5% mean"


def CO_bottom_5_percent_mean(data_csv, json_table):
    return data_csv["CO"][data_csv["CO"] < data_csv["CO"].quantile(0.05)].mean(), "Bottom 5% mean"


def CO_mean_top_outlier(data_csv, json_table):
    return data_csv["CO"][data_csv["CO"] > upper_limits["CO"]].mean() * data_csv["CO"][
        data_csv["CO"] > upper_limits["CO"]].count() / len(data_csv), "Mean top outlier"


def CO_mean_bottom_outlier(data_csv, json_table):
    return data_csv["CO"][data_csv["CO"] < lower_limits["CO"]].mean() * data_csv["CO"][
        data_csv["CO"] < lower_limits["CO"]].count() / len(data_csv), "Mean bottom outlier"


# NO

def NO_mean(data_csv, json_table):
    return data_csv["NO"].mean(), "Average"


def NO_min(data_csv, json_table):
    return data_csv["NO"].min(), "Minimum"


def NO_max(data_csv, json_table):
    return data_csv["NO"].max(), "Maximum"


def NO_var(data_csv, json_table):
    return data_csv["NO"].var(), "Variance"


def NO_mode(data_csv, json_table):
    return data_csv["NO"].mode().iloc[0], "Mode"


def NO_top_5_percent_mean(data_csv, json_table):
    return data_csv["NO"][data_csv["NO"] > data_csv["NO"].quantile(0.95)].mean(), "Top 5% mean"


def NO_bottom_5_percent_mean(data_csv, json_table):
    return data_csv["NO"][data_csv["NO"] < data_csv["NO"].quantile(0.05)].mean(), "Bottom 5% mean"


def NO_mean_top_outlier(data_csv, json_table):
    return data_csv["NO"][data_csv["NO"] > upper_limits["NO"]].mean() * data_csv["NO"][
        data_csv["NO"] > upper_limits["NO"]].count() / len(data_csv), "Mean top outlier"


def NO_mean_bottom_outlier(data_csv, json_table):
    return data_csv["NO"][data_csv["NO"] < lower_limits["NO"]].mean() * data_csv["NO"][
        data_csv["NO"] < lower_limits["NO"]].count() / len(data_csv), "Mean bottom outlier"


# CO2

def CO2_mean(data_csv, json_table):
    return data_csv["CO2"].mean(), "Average"


def CO2_min(data_csv, json_table):
    return data_csv["CO2"].min(), "Minimum"


def CO2_max(data_csv, json_table):
    return data_csv["CO2"].max(), "Maximum"


def CO2_var(data_csv, json_table):
    return data_csv["CO2"].var(), "Variance"


def CO2_mode(data_csv, json_table):
    return data_csv["CO2"].mode().iloc[0], "Mode"


def CO2_top_5_percent_mean(data_csv, json_table):
    return data_csv["CO2"][data_csv["CO2"] > data_csv["CO2"].quantile(0.95)].mean(), "Top 5% mean"


def CO2_bottom_5_percent_mean(data_csv, json_table):
    return data_csv["CO2"][data_csv["CO2"] < data_csv["CO2"].quantile(0.05)].mean(), "Bottom 5% mean"


def CO2_mean_top_outlier(data_csv, json_table):
    return data_csv["CO2"][data_csv["CO2"] > upper_limits["CO2"]].mean() * data_csv["CO2"][
        data_csv["CO2"] > upper_limits["CO2"]].count() / len(data_csv), "Mean top outlier"


def CO2_mean_bottom_outlier(data_csv, json_table):
    return data_csv["CO2"][data_csv["CO2"] < lower_limits["CO2"]].mean() * data_csv["CO2"][
        data_csv["CO2"] < lower_limits["CO2"]].count() / len(data_csv), "Mean bottom outlier"


# Spirometry

def Spirometry_mean(data_csv, json_table):
    return data_csv["Spirometry"].mean(), "Average"


def Spirometry_min(data_csv, json_table):
    return data_csv["Spirometry"].min(), "Minimum"


def Spirometry_max(data_csv, json_table):
    return data_csv["Spirometry"].max(), "Maximum"


def Spirometry_var(data_csv, json_table):
    return data_csv["Spirometry"].var(), "Variance"


def Spirometry_mode(data_csv, json_table):
    return data_csv["Spirometry"].mode().iloc[0], "Mode"


def Spirometry_top_5_percent_mean(data_csv, json_table):
    return data_csv["Spirometry"][data_csv["Spirometry"] > data_csv["Spirometry"].quantile(0.95)].mean(), "Top 5% mean"


def Spirometry_bottom_5_percent_mean(data_csv, json_table):
    return data_csv["Spirometry"][
        data_csv["Spirometry"] < data_csv["Spirometry"].quantile(0.05)].mean(), "Bottom 5% mean"


def Spirometry_mean_top_outlier(data_csv, json_table):
    return data_csv["Spirometry"][data_csv["Spirometry"] > upper_limits["Spirometry"]].mean() * data_csv["Spirometry"][
        data_csv["Spirometry"] > upper_limits["Spirometry"]].count() / len(data_csv), "Mean top outlier"


def Spirometry_mean_bottom_outlier(data_csv, json_table):
    return data_csv["Spirometry"][data_csv["Spirometry"] < lower_limits["Spirometry"]].mean() * data_csv["Spirometry"][
        data_csv["Spirometry"] < lower_limits["Spirometry"]].count() / len(data_csv), "Mean bottom outlier"


