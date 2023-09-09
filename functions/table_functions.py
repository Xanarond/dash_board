import numpy as np
import pandas as pd

lower_limits = {
    'CO2': 200,
    'CO': 0.01,
    'NO': 0.001,
    'Temperature': 25,
    'Humidity': 23,
    'Pressure': 983,
    'SpirometerData': 0.1
}

upper_limits = {
    'CO2': 10000,
    'CO': 50,
    'NO': 0.1,
    'Temperature': 40,
    'Humidity': 80,
    'Pressure': 1020,
    'SpirometerData': 2.5
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
        data_csv["CO"] > upper_limits["CO"]].count() / len(df), "Mean top outlier"


def CO_mean_bottom_outlier(data_csv, json_table):
    return data_csv["CO"][data_csv["CO"] < lower_limits["CO"]].mean() * data_csv["CO"][
        data_csv["CO"] < lower_limits["CO"]].count() / len(df), "Mean bottom outlier"


# NO

def NO_mean(data_csv, json_table):
    return data_csv["NO"].mean(), "Average"


def NO_min(data_csv, json_table):
    return data_csv["NO"].min(), "Minimum"


def NO_max(data_csv, json_table):
    return data_csv["NO"].max(), "Minimum"


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
        data_csv["NO"] > upper_limits["NO"]].NOunt() / len(df), "Mean top outlier"


def NO_mean_bottom_outlier(data_csv, json_table):
    return data_csv["NO"][data_csv["NO"] < lower_limits["NO"]].mean() * data_csv["NO"][
        data_csv["NO"] < lower_limits["NO"]].NOunt() / len(df), "Mean bottom outlier"


# CO2

def CO2_mean(data_csv, json_table):
    return data_csv["CO2"].mean(), "Average"


def CO2_min(data_csv, json_table):
    return data_csv["CO2"].min(), "Minimum"


def CO2_max(data_csv, json_table):
    return data_csv["CO2"].max(), "Minimum"


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
        data_csv["CO2"] > upper_limits["CO2"]].CO2unt() / len(df), "Mean top outlier"


def CO2_mean_bottom_outlier(data_csv, json_table):
    return data_csv["CO2"][data_csv["CO2"] < lower_limits["CO2"]].mean() * data_csv["CO2"][
        data_csv["CO2"] < lower_limits["CO2"]].CO2unt() / len(df), "Mean bottom outlier"


# Spyrometry

def Spyrometry_mean(data_csv, json_table):
    return data_csv["Spyrometry"].mean(), "Average"


def Spyrometry_min(data_csv, json_table):
    return data_csv["Spyrometry"].min(), "Minimum"


def Spyrometry_max(data_csv, json_table):
    return data_csv["Spyrometry"].max(), "Minimum"


def Spyrometry_var(data_csv, json_table):
    return data_csv["Spyrometry"].var(), "Variance"


def Spyrometry_mode(data_csv, json_table):
    return data_csv["Spyrometry"].mode().iloc[0], "Mode"


def Spyrometry_top_5_percent_mean(data_csv, json_table):
    return data_csv["Spyrometry"][data_csv["Spyrometry"] > data_csv["Spyrometry"].quantile(0.95)].mean(), "Top 5% mean"


def Spyrometry_bottom_5_percent_mean(data_csv, json_table):
    return data_csv["Spyrometry"][
        data_csv["Spyrometry"] < data_csv["Spyrometry"].quantile(0.05)].mean(), "Bottom 5% mean"


def Spyrometry_mean_top_outlier(data_csv, json_table):
    return data_csv["Spyrometry"][data_csv["Spyrometry"] > upper_limits["Spyrometry"]].mean() * data_csv["Spyrometry"][
        data_csv["Spyrometry"] > upper_limits["Spyrometry"]].Spyrometryunt() / len(df), "Mean top outlier"


def Spyrometry_mean_bottom_outlier(data_csv, json_table):
    return data_csv["Spyrometry"][data_csv["Spyrometry"] < lower_limits["Spyrometry"]].mean() * data_csv["Spyrometry"][
        data_csv["Spyrometry"] < lower_limits["Spyrometry"]].Spyrometryunt() / len(df), "Mean bottom outlier"



