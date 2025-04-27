import pytest


@pytest.mark.important_test
def test_pass():
    assert (1,2,3) == (1,2,3)