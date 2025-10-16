import pytest

from ..bun import Bun


@pytest.fixture   
def sample_bun():
    return Bun("Classik", 100.0)


def test_bun_get_name(sample_bun):
    assert sample_bun.get_name() == "Classik"
    assert isinstance(sample_bun.get_name(), str)


def test_bun_get_price(sample_bun):
    assert sample_bun.get_price() == 100
    assert isinstance(sample_bun.get_price(), float)