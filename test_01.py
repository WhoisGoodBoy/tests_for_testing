import pytest


@pytest.mark.test01
def test_01():
    assert 1 == 1

@pytest.mark.test02
def test_02():
    assert 1 == 2