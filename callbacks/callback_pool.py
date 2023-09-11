from callbacks.charts.linear_callback import linear1_callback_register
from callbacks.charts.linear_callback2 import linear2_callback_register
from callbacks.charts.linear_callback4 import linear4_callback_register
from callbacks.linear_callback3 import linear3_callback_register
from callbacks.tables.co2_callback import register_co2_callback
from callbacks.tables.co_callback import register_co_callback
from callbacks.tables.no_callback import register_no_callback
from callbacks.tables.spyrometry_callback import register_spyrometry_callback


def callback_pool(app):
    register_co_callback(app)
    register_no_callback(app)
    register_co2_callback(app)
    register_spyrometry_callback(app)
    linear1_callback_register(app)
    linear2_callback_register(app)
    linear3_callback_register(app)
    linear4_callback_register(app)