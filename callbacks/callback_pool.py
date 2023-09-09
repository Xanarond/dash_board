from callbacks.charts.blox_callback import register_blox_callback
from callbacks.tables.co2_callback import register_co2_callback
from callbacks.tables.co_callback import register_co_callback
from callbacks.tables.no_callback import register_no_callback
from callbacks.tables.spyrometry_callback import register_spyrometry_callback


def callback_pool(app):
    register_co_callback(app)
    register_no_callback(app)
    register_co2_callback(app)
    register_spyrometry_callback(app)
    register_blox_callback(app)