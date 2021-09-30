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
