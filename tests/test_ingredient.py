
class TestIngredient:

    def test_get_ingredient_type_true(self, ingredient_sausage):
        type = ingredient_sausage.type
        assert ingredient_sausage.get_type() == type

    def test_get_ingredient_name_true(self, ingredient_sausage):
        name = ingredient_sausage.name
        assert ingredient_sausage.get_name() == name

    def test_get_ingredient_price_true(self, ingredient_sausage):
        price = ingredient_sausage.price
        assert ingredient_sausage.get_price() == price