import datetime

import pytest

from isd import Record


def test_parse(record_line: str) -> None:
    record = Record.parse(record_line)
    assert record.usaf_id == "720538"
    assert record.ncei_id == "00164"
    assert record.datetime == datetime.datetime(
        2021, 1, 1, 0, 15, tzinfo=datetime.timezone.utc
    )
    assert record.data_source == "4"
    assert record.latitude == 40.167
    assert record.longitude == -105.167
    assert record.report_type == "FM-15"
    assert record.elevation == 1541
    assert record.call_letters == "99999"
    assert record.quality_control_process == "V020"
    assert record.wind_direction == 999
    assert record.wind_direction_quality_code == "9"
    assert record.wind_observation_type == "C"
    assert record.wind_speed == 0
    assert record.wind_speed_quality_code == "1"
    assert record.ceiling == 3353
    assert record.ceiling_quality_code == "1"
    assert record.ceiling_determination_code == "9"
    assert record.cavok_code == "N"
    assert record.visibility == 16093
    assert record.visibility_quality_code == "1"
    assert record.visibility_variation_code == "9"
    assert record.visibility_variation_quality_code == "9"
    assert record.air_temperature == 3.1
    assert record.air_temperature_quality_code == "1"
    assert record.dew_point_temperature == -5.8
    assert record.dew_point_temperature_quality_code == "1"
    assert record.sea_level_pressure == 9999.9
    assert record.sea_level_pressure_quality_code == "9"
    assert record.additional_data


def test_line_too_short() -> None:
    with pytest.raises(ValueError):
        Record.parse("")
