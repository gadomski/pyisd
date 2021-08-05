import isd


def test_read(data_file_path: str) -> None:
    records = isd.read(data_file_path)
    assert len(records) == 500
