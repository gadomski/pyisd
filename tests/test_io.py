from isd import io


def test_read(vance_brand: str) -> None:
    records = io.read(vance_brand)
    assert len(records) == 500


def test_read_to_geodataframe_lite(vance_brand: str) -> None:
    data_frame = io.read_to_geodataframe_lite(vance_brand)
    assert len(data_frame) == 500
