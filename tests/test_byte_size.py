from core.byte_size import ByteSize

def test_bytes():
    assert ByteSize.human(1024) == "1.00 KiB"
