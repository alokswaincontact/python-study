import pytest

@pytest.fixture(params=[42,43])
def some_value(request):
    "some_value fixture"
    print("called")
    return request.param

def test_func_1(some_value):
    assert (some_value == 42 or some_value == 43)

@pytest.mark.skip
def test_func_2(some_value):
    assert some_value == 42
