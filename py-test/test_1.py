import pytest

@pytest.fixture
def some_value():
    "some_value fixture"
    print("called")
    return 42

def test_func_1(some_value):
    assert some_value == 42

@pytest.mark.skip
def test_func_2(some_value):
    assert some_value == 42

def test_func_3(some_value):
    pytest.skip("testing")
    assert some_value == 42

def test_func_4(some_value):
    assert some_value == 42

