from math import log10, floor


def round_to_1(x):
    return round(x, -int(floor(log10(abs(x)))))


def create_plot_data(data_csv, datas):
    for i in range(len(datas)):
        datas[i].append(datas[i][0].max() - datas[i][0].min())
    datas = sorted(datas, key=lambda x: x[-1])

    new_datas = []
    for i in range(len(datas)):
        new_datas.append({})
        new_value = round_to_1(datas[i][-1] / (5 * (i + 1)))
        new_datas[-1]["graph"] = datas[i][0] / new_value
        new_datas[-1]["name"] = datas[i][1] + ", 1 unit = " + str(new_value) + " " + datas[i][2]
        new_datas[-1]["lower"] = datas[i][3] / new_value
        new_datas[-1]["upper"] = datas[i][4] / new_value
    return new_datas


# plot1


def CO_conc(data_csv, json_table):
    return data_csv["CO"] * data_csv["Spirometry"], "CO concetration", "%", 2, 23


def NO_conc(data_csv, json_table):
    return data_csv["NO"] * data_csv["Spirometry"], "NO concetration", "%", 0.02, 0.18


def CO2_conc(data_csv, json_table):
    return data_csv["CO2"] * data_csv["Spirometry"], "CO2 concetration", "%", 1000, 12000


def create_plot1(data_csv, json_table):
    datas = [list(CO_conc(data_csv, json_table)), list(NO_conc(data_csv, json_table)),
             list(CO2_conc(data_csv, json_table))]
    return create_plot_data(data_csv, datas)


# plot2


def CO_conc(data_csv, json_table):
    return data_csv["CO"] * data_csv["Spirometry"], "CO concetration", "%", 2, 23


def NO_conc(data_csv, json_table):
    return data_csv["NO"] * data_csv["Spirometry"], "NO concetration", "%", 0.02, 0.18


def CO2_conc(data_csv, json_table):
    return data_csv["CO2"] * data_csv["Spirometry"], "CO2 concetration", "%", 1000, 12000


def create_plot2(data_csv, json_table):
    datas = [list(CO_conc(data_csv, json_table)), list(NO_conc(data_csv, json_table)),
             list(CO2_conc(data_csv, json_table))]
    return create_plot_data(data_csv, datas)


# print(create_plot2(df,''))
# plot3


def CO_conc(data_csv, json_table):
    return data_csv["CO"] * data_csv["Spirometry"], "CO concetration", "%", 2, 23


def NO_conc(data_csv, json_table):
    return data_csv["NO"] * data_csv["Spirometry"], "NO concetration", "%", 0.02, 0.18


def CO2_conc(data_csv, json_table):
    return data_csv["CO2"] * data_csv["Spirometry"], "CO2 concetration", "%", 1000, 12000


def create_plot3(data_csv, json_table):
    datas = [list(CO_conc(data_csv, json_table)), list(NO_conc(data_csv, json_table)),
             list(CO2_conc(data_csv, json_table))]
    return create_plot_data(data_csv, datas)


# print(create_plot3(df,''))
# plot4


def CO_conc(data_csv, json_table):
    return data_csv["CO"] * data_csv["Spirometry"], "CO concetration", "%", 2, 23


def NO_conc(data_csv, json_table):
    return data_csv["NO"] * data_csv["Spirometry"], "NO concetration", "%", 0.02, 0.18


def CO2_conc(data_csv, json_table):
    return data_csv["CO2"] * data_csv["Spirometry"], "CO2 concetration", "%", 1000, 12000


def create_plot4(data_csv, json_table):
    datas = [list(CO_conc(data_csv, json_table)), list(NO_conc(data_csv, json_table)),
             list(CO2_conc(data_csv, json_table))]
    return create_plot_data(data_csv, datas)
