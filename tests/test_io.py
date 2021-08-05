from isd import io


def test_read(data_file_path: str) -> None:
    records = io.read(data_file_path)
    assert len(records) == 500


def test_read_to_geodataframe_lite(data_file_path: str) -> None:
    data_frame = io.read_to_geodataframe_lite(data_file_path)
    assert len(data_frame) == 500
