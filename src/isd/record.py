from dataclasses import dataclass
from typing import List, Optional, Tuple, TypeVar

from isd.errors import IsdError

MIN_LINE_LENGTH = 105
Numeric = TypeVar("Numeric", int, float)


@dataclass
class Record:
    """A single line of an ISD file."""

    usaf_id: str
    ncei_id: str
    year: int
    month: int
    day: int
    hour: int
    minute: int
    data_source: str
    latitude: float
    longitude: float
    report_type: str
    elevation: float
    call_letters: str
    quality_control_process: str
    wind_direction: int
    wind_direction_quality_code: str
    wind_observation_type: str
    wind_speed: float
    wind_speed_quality_code: str
    ceiling: int
    ceiling_quality_code: str
    ceiling_determination_code: str
    cavok_code: str
    visibility: int
    visibility_quality_code: str
    visibility_variation_code: str
    visibility_variation_quality_code: str
    air_temperature: float
    air_temperature_quality_code: str
    dew_point_temperature: float
    dew_point_temperature_quality_code: str
    sea_level_pressure: float
    sea_level_pressure_quality_code: str
    additional_data: str
    remarks: str
    element_quality_data: str
    original_observation_data: str

    @classmethod
    def parse(cls, line: str) -> "Record":
        """Parses an ISD line into a record."""
        if len(line) < MIN_LINE_LENGTH:
            raise IsdError(f"Invalid ISD line (too short): {line}")
        line = line.strip()
        usaf_id = line[4:10]
        ncei_id = line[10:15]
        year = int(line[15:19])
        month = int(line[19:21])
        day = int(line[21:23])
        hour = int(line[23:25])
        minute = int(line[25:27])
        data_source = line[27]
        latitude = float(line[28:34]) / 1000
        longitude = float(line[34:41]) / 1000
        report_type = line[41:46]
        elevation = float(line[46:51])
        call_letters = line[51:56]
        quality_control_process = line[56:60]
        wind_direction = int(line[60:63])
        wind_direction_quality_code = line[63]
        wind_observation_type = line[64]
        wind_speed = float(line[65:69]) / 10
        wind_speed_quality_code = line[69]
        ceiling = int(line[70:75])
        ceiling_quality_code = line[75]
        ceiling_determination_code = line[76]
        cavok_code = line[77]
        visibility = int(line[78:84])
        visibility_quality_code = line[84]
        visibility_variation_code = line[85]
        visibility_variation_quality_code = line[86]
        air_temperature = float(line[87:92]) / 10
        air_temperature_quality_code = line[92]
        dew_point_temperature = float(line[93:98]) / 10
        dew_point_temperature_quality_code = line[98]
        sea_level_pressure = float(line[99:104]) / 10
        sea_level_pressure_quality_code = line[104]
        additional_data, remainder = extract_data(
            line[105:], "ADD", ["REM", "EQD", "QNN"]
        )
        remarks, remainder = extract_data(remainder, "REM", ["EQD", "QNN"])
        element_quality_data, remainder = extract_data(remainder, "EQD", ["QNN"])
        original_observation_data, remainder = extract_data(remainder, "QNN", [])
        assert not remainder

        return cls(
            usaf_id=usaf_id,
            ncei_id=ncei_id,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            data_source=data_source,
            latitude=latitude,
            longitude=longitude,
            report_type=report_type,
            elevation=elevation,
            call_letters=call_letters,
            quality_control_process=quality_control_process,
            wind_direction=wind_direction,
            wind_direction_quality_code=wind_direction_quality_code,
            wind_observation_type=wind_observation_type,
            wind_speed=wind_speed,
            wind_speed_quality_code=wind_speed_quality_code,
            ceiling=ceiling,
            ceiling_quality_code=ceiling_quality_code,
            ceiling_determination_code=ceiling_determination_code,
            cavok_code=cavok_code,
            visibility=visibility,
            visibility_quality_code=visibility_quality_code,
            visibility_variation_code=visibility_variation_code,
            visibility_variation_quality_code=visibility_variation_quality_code,
            air_temperature=air_temperature,
            air_temperature_quality_code=air_temperature_quality_code,
            dew_point_temperature=dew_point_temperature,
            dew_point_temperature_quality_code=dew_point_temperature_quality_code,
            sea_level_pressure=sea_level_pressure,
            sea_level_pressure_quality_code=sea_level_pressure_quality_code,
            additional_data=additional_data,
            remarks=remarks,
            element_quality_data=element_quality_data,
            original_observation_data=original_observation_data,
        )

    def sky_condition_code(self) -> Optional[int]:
        """Returns the sky condition code from the additional data."""
        try:
            index = self.additional_data.index("GF1")
        except ValueError:
            return None
        code = self.additional_data[index + 3 : index + 5]
        return check_for_missing(int(code), 99)

    def liquid_precipitation(self, hours: int) -> Optional[float]:
        """Returns the liquid precipitation measurement over the last `hours` hours."""
        for n in [1, 2, 3, 4]:
            try:
                index = self.additional_data.index(f"AA{n}")
            except ValueError:
                continue
            try:
                aa_hours = int(self.additional_data[index + 3 : index + 5])
            except ValueError:
                continue
            if aa_hours == hours:
                value = float(self.additional_data[index + 5 : index + 9]) / 10
                return check_for_missing(float(value), 999.9)
        return None


def check_for_missing(value: Numeric, missing_value: Numeric) -> Optional[Numeric]:
    if value == missing_value:
        return None
    else:
        return value


def extract_data(message: str, tag: str, later_tags: List[str]) -> Tuple[str, str]:
    if message.startswith(tag):
        index = None
        for other_tag in later_tags:
            try:
                index = message.find(other_tag)
            except ValueError:
                continue
            break
        if index != -1:
            data = message[len(tag) : index]
            tail = message[index:]
            return data, tail
        else:
            return message[len(tag) :], ""
    else:
        return "", message
