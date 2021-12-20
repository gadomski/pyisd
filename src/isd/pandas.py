import datetime
from typing import Iterable, Optional

import pandas
from pandas import CategoricalDtype, DataFrame

from isd import Record

DataSourceDtype = CategoricalDtype(
    [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
    ]
)
ReportTypeDtype = CategoricalDtype(
    [
        "AERO",
        "AUST",
        "AUTO",
        "BOGUS",
        "BRAZ",
        "COOPD",
        "COOPS",
        "CRB",
        "CRN05",
        "CRN15",
        "FM-12",
        "FM-13",
        "FM-14",
        "FM-15",
        "FM-16",
        "FM-18",
        "GREEN",
        "MESOH",
        "MESOS",
        "MESOW",
        "MEXIC",
        "NSRDB",
        "PCP15",
        "PCP60",
        "S-S-A",
        "SA-AU",
        "SAO",
        "SAOSP",
        "SHEF",
        "SMARS",
        "SOD",
        "SOM",
        "SURF",
        "SY-AE",
        "SY-AU",
        "SY-MT",
        "SY-SA",
        "WBO",
        "WNO",
    ]
)
QualityControlProcessDtype = CategoricalDtype(["V01", "V02", "V03"])
QualityCodeDtype = CategoricalDtype(
    [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "9",
        "A",
        "U",
        "P",
        "I",
        "M",
        "C",
        "R",
    ]
)
WindObservationTypeDtype = CategoricalDtype(
    ["A", "B", "C", "H", "N", "R", "Q", "T", "V"]
)
CeilingDeterminationCodeDtype = CategoricalDtype(
    ["A", "B", "C", "D", "E", "M", "P", "R", "S", "U", "V", "W"]
)
CavokCodeDtype = CategoricalDtype(["N", "Y"])
VisibilityVariabilityCodeDtype = CategoricalDtype(["N", "V"])


def data_frame(
    records: Iterable[Record], since: Optional[datetime.datetime] = None
) -> DataFrame:
    """Constructs a pandas data frame from an iterable of Records.

    Uses appropriate datatypes and categorical variables.
    """
    data_frame = DataFrame(records).astype(
        {
            "usaf_id": "string",
            "ncei_id": "string",
            "year": "UInt16",
            "month": "UInt8",
            "day": "UInt8",
            "hour": "UInt8",
            "minute": "UInt8",
            "data_source": DataSourceDtype,
            "latitude": "float",
            "longitude": "float",
            "report_type": ReportTypeDtype,
            "elevation": "Int16",
            "call_letters": "string",
            "quality_control_process": QualityControlProcessDtype,
            "wind_direction": "UInt16",
            "wind_direction_quality_code": QualityCodeDtype,
            "wind_observation_type": WindObservationTypeDtype,
            "wind_speed": "float",
            "wind_speed_quality_code": QualityCodeDtype,
            "ceiling": "float",
            "ceiling_quality_code": QualityCodeDtype,
            "ceiling_determination_code": CeilingDeterminationCodeDtype,
            "cavok_code": CavokCodeDtype,
            "visibility": "UInt32",
            "visibility_quality_code": QualityCodeDtype,
            "visibility_variability_code": VisibilityVariabilityCodeDtype,
            "visibility_variability_quality_code": QualityCodeDtype,
            "air_temperature": "float",
            "air_temperature_quality_code": QualityCodeDtype,
            "dew_point_temperature": "float",
            "dew_point_temperature_quality_code": QualityCodeDtype,
            "sea_level_pressure": "float",
            "sea_level_pressure_quality_code": QualityCodeDtype,
            "additional_data": "string",
            "remarks": "string",
            "element_quality_data": "string",
            "original_observation_data": "string",
        }
    )
    timestamp = pandas.to_datetime(
        data_frame[["year", "month", "day", "hour", "minute"]]
    )
    data_frame["timestamp"] = timestamp
    if since:
        return data_frame[data_frame["timestamp"] > since]
    else:
        return data_frame
