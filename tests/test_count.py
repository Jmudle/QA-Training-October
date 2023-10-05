from test_lint import count

def test_count():
    assert count([1,2,2,2,2,3,4,5,6], 2) == 4
    assert count(["tim", "tim", "tom"], "tim") == 1