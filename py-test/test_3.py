import pytest
import math

@pytest.fixture(params=[42,43])
def some_value(request):
    "some_value fixture"
    print("called")
    return request.param

@pytest.fixture
def square_value(some_value):
    "square value fixture"
    print("called")
    return math.pow(some_value, 2)

def test_func_1(square_value):
    assert (square_value == 42*42 or square_value == 43*43)
