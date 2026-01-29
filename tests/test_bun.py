
def test_bun_initialization(sample_bun):
    assert sample_bun.get_name() == "test bun"
    assert sample_bun.get_price() == 50.0

def test_bun_name(sample_bun):
    assert sample_bun.get_name() == "test bun"

def test_bun_price(sample_bun):
    assert sample_bun.get_price() == 50.0

