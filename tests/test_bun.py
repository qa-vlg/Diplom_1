
class TestBun:

    def test_get_name_true(self, bun):
        name = bun.name
        assert bun.get_name() == name
    
    def test_get_price_true(self, bun):
        price = bun.price
        assert bun.get_price() == price