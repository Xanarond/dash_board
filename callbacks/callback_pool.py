from callbacks.charts.linear_callback import linear1_callback_register
from callbacks.charts.linear_callback2 import linear2_callback_register
from callbacks.charts.linear_callback3 import linear3_callback_register
from callbacks.charts.linear_callback4 import linear4_callback_register
from callbacks.file_reading_callback import file_reading_callback
from callbacks.tables.co2_callback import register_co2_callback
from callbacks.tables.co_callback import register_co_callback
from callbacks.tables.no_callback import register_no_callback
from callbacks.tables.spyrometry_callback import register_spirometry_callback
from callbacks.tables.survey_callback import register_survey_callback


def callback_pool(app):
    file_reading_callback(app)
    register_co_callback(app)
    register_no_callback(app)
    register_co2_callback(app)
    register_spirometry_callback(app)
    register_survey_callback(app)
    linear1_callback_register(app)
    linear2_callback_register(app)
    linear3_callback_register(app)
    linear4_callback_register(app)
