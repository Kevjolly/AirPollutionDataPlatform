#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module inserts data into the necessary field dataset
"""

from utility import log_config
from utility import utils
from utility import config

LOGGER = log_config.setup_logger('ckan_import_default_log')

ID_BRISTOL_NECESSARY_FIELDS = config.dict_resource_id["resource_id_main_air_pollution_bristol_necessary"]
#ID_LONDON_NECESSARY_FIELDS = "262940a0-7d73-4eb4-abf5-a7711cc025b5"

RECORDS_BRISTOL_NECESSARY_FIELDS = [
    {
        "geometry": "Point",
        "necessary_fields": ["pm1",
                             "pm25",
                             "pm10",
                             "no",
                             "nox",
                             "no2",
                             "o3",
                             "co",
                             "temperature",
                             "rh",
                             "tvoc",
                             "eCO2",
                             "light",
                             "noise",
                             "pressure",
                             "ws",
                             "wd"]
    }, {
        "geometry": "Polygon",
        "necessary_fields": ["population_estimate",
                             "average_number_of_cars_per_household",
                             "number_of_cars_or_vans_in_the_area",
                             "all_households",
                             "no_cars_or_vans_in_household",
                             "per_of_households_with_no_car",
                             "1_car_or_van_in_household",
                             "per_of_households_with_1_car",
                             "2_cars_or_vans_in_household",
                             "per_of_households_with_2_cars",
                             "3_cars_or_vans_in_household",
                             "per_of_households_with_3_cars",
                             "4_or_more_cars_or_vans_in_household",
                             "per_of_households_with_4_or_more_cars"]
    }
]

RECORDS_LONDON_NECESSARY_FIELDS = [
    {
        "geometry": "Point",
        "necessary_fields": ["pm1",
                             "pm25",
                             "pm10",
                             "no",
                             "nox",
                             "no2",
                             "o3",
                             "co",
                             "temperature",
                             "rh",
                             "tvoc",
                             "eCO2",
                             "light",
                             "noise",
                             "pressure",
                             "ws",
                             "wd"]
    }
]

def insert_necessary_fields():

   try:
       utils.ckan_upsert(ID_BRISTOL_NECESSARY_FIELDS, RECORDS_BRISTOL_NECESSARY_FIELDS)
       print("done")
   except Exception as exception_returned:
       print(exception_returned)

