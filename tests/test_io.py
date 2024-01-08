import isd.io


def test_open_uncompressed(uncompressed_path: str) -> None:
    with isd.io.open(uncompressed_path) as generator:
        records = list(generator)
    assert len(records) == 500


def test_open_compressed(compressed_path: str) -> None:
    with isd.io.open(compressed_path) as generator:
        records = list(generator)
    assert len(records) == 24252
