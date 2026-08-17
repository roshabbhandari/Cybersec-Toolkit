from core.byte_size import ByteSize

def test_negative_bytes_are_supported():
    assert ByteSize.human(-1024) == "-1.00 KiB"
