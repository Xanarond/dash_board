import os

import numpy as np
import pandas as pd

lower_limits = {
    'CO2': 200,
    'CO': 0.01,
    'NO': 0.001,
    'CH3': 0.001,
    'Temperature': 25,
    'Humidity': 23,
    'Pressure': 983,
    'Spirometry': 0.1
}

upper_limits = {
    'CO2': 10000,
    'CO': 50,
    'NO': 0.1,
    'CH3': 0.1,
    'Temperature': 40,
    'Humidity': 80,
    'Pressure': 1020,
    'Spirometry': 2.5
}


# Pointed functions
# CO

def CO_mean(data_csv, json_table=''):
    return round(data_csv["CO"].mean(), 4), "Average"


def CO_min(data_csv, json_table):
    return f'{round(data_csv["CO"].min(), 4)}', "Minimum"


def CO_max(data_csv, json_table):
    return f'{round(data_csv["CO"].max(), 4)}', "Maximum"


def CO_var(data_csv, json_table):
    return f'{round(data_csv["CO"].var(), 4)}', "Variance"


def CO_mode(data_csv, json_table):
    return f'{round(data_csv["CO"].mode().iloc[0])}', "Mode"


def CO_top_5_percent_mean(data_csv, json_table):
    return f'{round(data_csv["CO"][data_csv["CO"] > data_csv["CO"].quantile(0.95)].mean(), 4)}', "Top 5% mean"


def CO_bottom_5_percent_mean(data_csv, json_table):
    return f'{round(data_csv["CO"][data_csv["CO"] < data_csv["CO"].quantile(0.05)].mean(), 4)}', "Bottom 5% mean"


def CO_mean_top_outlier(data_csv, json_table):
    return data_csv["CO"][data_csv["CO"] > upper_limits["CO"]].mean() * data_csv["CO"][
        data_csv["CO"] > upper_limits["CO"]].count() / len(data_csv), "Mean top outlier"


def CO_mean_bottom_outlier(data_csv, json_table):
    return data_csv["CO"][data_csv["CO"] < lower_limits["CO"]].mean() * data_csv["CO"][
        data_csv["CO"] < lower_limits["CO"]].count() / len(data_csv), "Mean bottom outlier"


# NO

def NO_mean(data_csv, json_table):
    return f'{round(data_csv["NO"].mean(), 4)}', "Average"


def NO_min(data_csv, json_table):
    return f'{round(data_csv["NO"].min(), 4)}', "Minimum"


def NO_max(data_csv, json_table):
    return f'{round(data_csv["NO"].max(), 4)}', "Maximum"


def NO_var(data_csv, json_table):
    return f'{round(data_csv["NO"].var(), 4)}', "Variance"


def NO_mode(data_csv, json_table):
    return f'{round(data_csv["NO"].mode().iloc[0], 4)}', "Mode"


def NO_top_5_percent_mean(data_csv, json_table):
    return f'{round(data_csv["NO"][data_csv["NO"] > data_csv["NO"].quantile(0.95)].mean())}', "Top 5% mean"


def NO_bottom_5_percent_mean(data_csv, json_table):
    return f'{round(data_csv["NO"][data_csv["NO"] < data_csv["NO"].quantile(0.05)].mean(), 4)}', "Bottom 5% mean"


def NO_mean_top_outlier(data_csv, json_table):
    return data_csv["NO"][data_csv["NO"] > upper_limits["NO"]].mean() * data_csv["NO"][
        data_csv["NO"] > upper_limits["NO"]].count() / len(data_csv), "Mean top outlier"


def NO_mean_bottom_outlier(data_csv, json_table):
    return data_csv["NO"][data_csv["NO"] < lower_limits["NO"]].mean() * data_csv["NO"][
        data_csv["NO"] < lower_limits["NO"]].count() / len(data_csv), "Mean bottom outlier"


# CH3

def CH3_mean(data_csv, json_table=''):
    return f'{round(data_csv["CH3"].mean(), 4)}', "Average"


def CH3_min(data_csv, json_table):
    return f'{round(data_csv["CH3"].min(), 4)}', "Minimum"


def CH3_max(data_csv, json_table):
    return f'{round(data_csv["CH3"].max(), 4)}', "Maximum"


def CH3_var(data_csv, json_table):
    return f'{round(data_csv["CH3"].var(), 4)}', "Variance"


def CH3_mode(data_csv, json_table):
    return f'{round(data_csv["CH3"].mode().iloc[0], 4)}', "Mode"


def CH3_top_5_percent_mean(data_csv, json_table):
    return f'{round(data_csv["CH3"][data_csv["CH3"] > data_csv["CH3"].quantile(0.95)].mean(), 4)}', "Top 5% mean"


def CH3_bottom_5_percent_mean(data_csv, json_table):
    return f'{round(data_csv["CH3"][data_csv["CH3"] < data_csv["CH3"].quantile(0.05)].mean(), 4)}', "Bottom 5% mean"


def CH3_mean_top_outlier(data_csv, json_table):
    return data_csv["CH3"][data_csv["CH3"] < lower_limits["CH3"]].mean() * data_csv["CH3"][
        data_csv["CH3"] < lower_limits["CH3"]].count() / len(data_csv), "Mean bottom outlier"


def CH3_mean_bottom_outlier(data_csv, json_table):
    return data_csv["CH3"][data_csv["CH3"] < lower_limits["CH3"]].mean() * data_csv["CH3"][
        data_csv["CH3"] < lower_limits["CH3"]].count() / len(data_csv), "Mean bottom outlier"

    # CO2


def CO2_mean(data_csv, json_table):
    return f'{round(data_csv["CO2"].mean())}', "Average"


def CO2_min(data_csv, json_table):
    return f'{round(data_csv["CO2"].min())}', "Minimum"


def CO2_max(data_csv, json_table):
    return f'{round(data_csv["CO2"].max())}', "Maximum"


def CO2_var(data_csv, json_table):
    return f'{round(data_csv["CO2"].var())}', "Variance"


def CO2_mode(data_csv, json_table):
    return f'{round(data_csv["CO2"].mode().iloc[0])}', "Mode"


def CO2_top_5_percent_mean(data_csv, json_table):
    return f'{round(data_csv["CO2"][data_csv["CO2"] > data_csv["CO2"].quantile(0.95)].mean())}', "Top 5% mean"


def CO2_bottom_5_percent_mean(data_csv, json_table):
    return f'{round(data_csv["CO2"][data_csv["CO2"] < data_csv["CO2"].quantile(0.05)].mean())}', "Bottom 5% mean"


def CO2_mean_top_outlier(data_csv, json_table):
    return data_csv["CO2"][data_csv["CO2"] > upper_limits["CO2"]].mean() * data_csv["CO2"][
        data_csv["CO2"] > upper_limits["CO2"]].count() / len(data_csv), "Mean top outlier"


def CO2_mean_bottom_outlier(data_csv, json_table):
    return data_csv["CO2"][data_csv["CO2"] < lower_limits["CO2"]].mean() * data_csv["CO2"][
        data_csv["CO2"] < lower_limits["CO2"]].count() / len(data_csv), "Mean bottom outlier"


# Spirometry

def Spirometry_mean(data_csv, json_table):
    return f'{round(data_csv["Spirometry"].mean(), 4)}', "Average"


def Spirometry_min(data_csv, json_table):
    return f'{round(data_csv["Spirometry"].min(), 4)}', "Minimum"


def Spirometry_max(data_csv, json_table):
    return f'{round(data_csv["Spirometry"].max(), 4)}', "Maximum"


def Spirometry_var(data_csv, json_table):
    return f'{round(data_csv["Spirometry"].var(), 4)}', "Variance"


def Spirometry_mode(data_csv, json_table):
    return f'{round(data_csv["Spirometry"].mode().iloc[0], 4)}', "Mode"


def Spirometry_top_5_percent_mean(data_csv, json_table):
    return f'{round(data_csv["Spirometry"][data_csv["Spirometry"] > data_csv["Spirometry"].quantile(0.95)].mean(), 4)}', "Top 5% mean"


def Spirometry_bottom_5_percent_mean(data_csv, json_table):
    return f'{round(data_csv["Spirometry"][data_csv["Spirometry"] < data_csv["Spirometry"].quantile(0.05)].mean(), 4)}', "Bottom 5% mean"


def Spirometry_mean_top_outlier(data_csv, json_table):
    return data_csv["Spirometry"][data_csv["Spirometry"] > upper_limits["Spirometry"]].mean() * data_csv["Spirometry"][
        data_csv["Spirometry"] > upper_limits["Spirometry"]].count() / len(data_csv), "Mean top outlier"


def Spirometry_mean_bottom_outlier(data_csv, json_table):
    return data_csv["Spirometry"][data_csv["Spirometry"] < lower_limits["Spirometry"]].mean() * data_csv["Spirometry"][
        data_csv["Spirometry"] < lower_limits["Spirometry"]].count() / len(data_csv), "Mean bottom outlier"


def Spirometry_FEV(data_csv, json_table):
    return f'{round(np.random.random(), 4)}', "FEV"


def Spirometry_TEV(data_csv, json_table):
    return f'{round(np.random.random(), 4)}', "TEV"


def Spirometry_DEV(data_csv, json_table):
    return f'{round(np.random.random(), 4)}', "DEV"


def Spirometry_LEV(data_csv, json_table):
    return f'{round(np.random.random(), 4)}', "LEV"


def generate_table_1(data_csv, json_table):
    CO_functions = [CO_mean, CO_min, CO_max, CO_var, CO_mode, CO_top_5_percent_mean, CO_bottom_5_percent_mean,
                    CO_mean_top_outlier, CO_mean_bottom_outlier]
    NO_functions = [NO_mean, NO_min, NO_max, NO_var, NO_mode, NO_top_5_percent_mean, NO_bottom_5_percent_mean,
                    NO_mean_top_outlier, NO_mean_bottom_outlier]
    CO2_functions = [CO2_mean, CO2_min, CO2_max, CO2_var, CO2_mode, CO2_top_5_percent_mean, CO2_bottom_5_percent_mean,
                     CO2_mean_top_outlier, CO2_mean_bottom_outlier]
    CH3_functions = [CH3_mean, CH3_min, CH3_max, CH3_var, CH3_mode, CH3_top_5_percent_mean, CH3_bottom_5_percent_mean,
                     CH3_mean_top_outlier, CH3_mean_bottom_outlier]
    CO_data = [func(data_csv, json_table) for func in CO_functions]
    NO_data = [func(data_csv, json_table) for func in NO_functions]
    CO2_data = [func(data_csv, json_table) for func in CO2_functions]
    CH3_data = [func(data_csv, json_table) for func in CH3_functions]
    table_1 = pd.DataFrame()
    table_1.index = [x[1] for x in CO_data]
    table_1["CO"] = [x[0] for x in CO_data]
    table_1["NO"] = [x[0] for x in NO_data]
    table_1["CO2"] = [x[0] for x in CO2_data]
    table_1["CH3"] = [x[0] for x in CH3_data]
    table_1.columns = ["CO, ppm", "NO, ppb", "CO2, %", "Ch3, ppb"]
    return table_1


def generate_table_2(data_csv, json_table):
    SPIROMETRY_functions = [Spirometry_mean, Spirometry_min, Spirometry_max, Spirometry_top_5_percent_mean,
                            Spirometry_bottom_5_percent_mean,
                            Spirometry_FEV, Spirometry_TEV, Spirometry_DEV,
                            Spirometry_LEV]
    SPIROMETRY_data = [func(data_csv, json_table) for func in SPIROMETRY_functions]
    table_2 = pd.DataFrame()
    table_2.index = [x[1] for x in SPIROMETRY_data]
    table_2["SPIROMETRY"] = [x[0] for x in SPIROMETRY_data]
    table_2.fillna(0)
    return table_2
