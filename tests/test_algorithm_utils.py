import pytest
from core.algorithm_utils import AlgorithmUtils

def test_normalize_hash():
    assert AlgorithmUtils.normalize_hash(" SHA256 ") == "sha256"

def test_reject_unknown_hash():
    with pytest.raises(ValueError):
        AlgorithmUtils.normalize_hash("sha999")
