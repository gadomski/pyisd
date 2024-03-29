import datetime
import json

import pytest

from isd import IsdError, Record


def test_parse(record_line: str) -> None:
    record = Record.parse(record_line)
    assert record.usaf_id == "720538"
    assert record.ncei_id == "00164"
    assert record.year == 2021
    assert record.month == 1
    assert record.month == 1
    assert record.day == 1
    assert record.hour == 0
    assert record.minute == 15
    assert record.data_source == "4"
    assert record.latitude == 40.167
    assert record.longitude == -105.167
    assert record.report_type == "FM-15"
    assert record.elevation == 1541
    assert record.call_letters is None
    assert record.quality_control_process == "V020"
    assert record.wind_direction is None
    assert record.wind_direction_quality_code == "9"
    assert record.wind_observation_type == "C"
    assert record.wind_speed == 0
    assert record.wind_speed_quality_code == "1"
    assert record.ceiling == 3353
    assert record.ceiling_quality_code == "1"
    assert record.ceiling_determination_code is None
    assert record.cavok_code == "N"
    assert record.visibility == 16093
    assert record.visibility_quality_code == "1"
    assert record.visibility_variability_code is None
    assert record.visibility_variability_quality_code == "9"
    assert record.air_temperature == 3.1
    assert record.air_temperature_quality_code == "1"
    assert record.dew_point_temperature == -5.8
    assert record.dew_point_temperature_quality_code == "1"
    assert record.sea_level_pressure is None
    assert record.sea_level_pressure_quality_code == "9"
    assert (
        record.additional_data == "GD14991+0335399GE19MSL   +99999+"
        "99999GF199999999999033531999999MA1101561999999"
    )
    assert (
        record.remarks == "MET075METAR KLMO 010015Z AUTO 00000KT "
        "10SM OVC110 03/M06 A2999 RMK AO2 T00311058="
    )


def test_line_too_short() -> None:
    with pytest.raises(IsdError):
        Record.parse("")


def test_record_to_dict(record: Record) -> None:
    assert record.to_dict() == {
        "usaf_id": "720538",
        "ncei_id": "00164",
        "datetime": datetime.datetime(2021, 1, 1, 0, 15),
        "data_source": "4",
        "latitude": 40.167,
        "longitude": -105.167,
        "report_type": "FM-15",
        "elevation": 1541,
        "call_letters": None,
        "quality_control_process": "V020",
        "wind_direction": None,
        "wind_direction_quality_code": "9",
        "wind_observation_type": "C",
        "wind_speed": 0,
        "wind_speed_quality_code": "1",
        "ceiling": 3353,
        "ceiling_quality_code": "1",
        "ceiling_determination_code": None,
        "cavok_code": "N",
        "visibility": 16093,
        "visibility_quality_code": "1",
        "visibility_variability_code": None,
        "visibility_variability_quality_code": "9",
        "air_temperature": 3.1,
        "air_temperature_quality_code": "1",
        "dew_point_temperature": -5.8,
        "dew_point_temperature_quality_code": "1",
        "sea_level_pressure": None,
        "sea_level_pressure_quality_code": "9",
        "additional_data": "GD14991+0335399GE19MSL   +99999+"
        "99999GF199999999999033531999999MA1101561999999",
        "remarks": "MET075METAR KLMO 010015Z AUTO 00000KT "
        "10SM OVC110 03/M06 A2999 RMK AO2 T00311058=",
        "element_quality_data": "",
        "original_observation_data": "",
    }


def test_record_to_json(record: Record) -> None:
    json_string = record.to_json()
    data = json.loads(json_string)
    assert data["usaf_id"] == "720538"
    assert data["ncei_id"] == "00164"
    assert data["datetime"] == "2021-01-01T00:15:00"
