import datetime
from dataclasses import dataclass


MIN_LINE_LENGTH = 105


@dataclass
class Record:
    """A single line of an ISD file."""

    usaf_id: str
    ncei_id: str
    datetime: datetime.datetime
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

    @classmethod
    def parse(cls, line: str) -> "Record":
        """Parses an ISD line into a record."""
        if len(line) < MIN_LINE_LENGTH:
            raise ValueError(f"Invalid ISD line (too short): {line}")
        usaf_id = line[4:10]
        ncei_id = line[10:15]
        dt = datetime.datetime(
            int(line[15:19]),
            int(line[19:21]),
            int(line[21:23]),
            int(line[23:25]),
            int(line[25:27]),
            tzinfo=datetime.timezone.utc,
        )
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
        additional_data = line[105:]
        return cls(
            usaf_id=usaf_id,
            ncei_id=ncei_id,
            datetime=dt,
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
        )
