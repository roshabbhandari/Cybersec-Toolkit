from core.aug22_status_rank import rank_status

def test_rank_status():
    assert rank_status("HIGH") == 3
    assert rank_status("unknown") == -1
