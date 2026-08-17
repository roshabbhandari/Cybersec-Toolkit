from core.file_integrity import FileIntegrity

def test_sha256_empty_file(tmp_path):
    path = tmp_path / "empty.bin"
    path.write_bytes(b"")
    assert len(FileIntegrity.sha256(str(path))) == 64
