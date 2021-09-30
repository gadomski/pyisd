Command Line Interface (CLI)
============================

**isd** comes with a very simple command-line interface.
To print a single record from a file as JSON:

.. code-block:: shell

    $ isd record 720538-00164-2020
    {
        "usaf_id": "720538",
        "ncei_id": "00164",
        "year": 2021,
        "month": 1,
        "day": 1,
        "hour": 0,
        "minute": 15,
        "data_source": "4",
        "latitude": 40.167,
        "longitude": -105.167,
        "report_type": "FM-15",
        "elevation": 1541.0,
        "call_letters": null,
        "quality_control_process": "V020",
        "wind_direction": null,
        "wind_direction_quality_code": "9",
        "wind_observation_type": "C",
        "wind_speed": 0.0,
        "wind_speed_quality_code": "1",
        "ceiling": 3353,
        "ceiling_quality_code": "1",
        "ceiling_determination_code": null,
        "cavok_code": "N",
        "visibility": 16093,
        "visibility_quality_code": "1",
        "visibility_variability_code": null,
        "visibility_variability_quality_code": "9",
        "air_temperature": 3.1,
        "air_temperature_quality_code": "1",
        "dew_point_temperature": -5.8,
        "dew_point_temperature_quality_code": "1",
        "sea_level_pressure": null,
        "sea_level_pressure_quality_code": "9",
        "additional_data": "GD14991+0335399GE19MSL   +99999+99999GF199999999999033531999999MA1101561999999",
        "remarks": "MET075METAR KLMO 010015Z AUTO 00000KT 10SM OVC110 03/M06 A2999 RMK AO2 T00311058=",
        "element_quality_data": "",
        "original_observation_data": ""
    }

Note that this works with both compressed and uncompressed files as well, e.g.:

.. code-block:: shell

    $ isd record 720538-00164-2020.gz
    ...
