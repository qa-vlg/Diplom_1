from praktikum.burger import Burger

class TestBurger:

    def test_default_bun_value_true(self):
        burger = Burger()
        assert burger.bun == None

    def test_default_ingredients_value_true(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_add_bun_true(self, mock_bun, burger):
        name = mock_bun.name
        burger.set_buns(mock_bun)
        assert burger.bun.name == name
    
    def test_add_ingredient_true(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].name == mock_ingredient.name

    def test_remove_ingredient_true(self, burger_with_ingredient):
        initial_size = len(burger_with_ingredient.ingredients)
        burger_with_ingredient.remove_ingredient(0)
        assert len(burger_with_ingredient.ingredients) == (initial_size - 1)

    def test_move_ingredient_true(self, burger_with_two_ingredients):
        ingredient_to_be_moved = burger_with_two_ingredients.ingredients[1].name
        burger_with_two_ingredients.move_ingredient(1, 0)
        assert burger_with_two_ingredients.ingredients[0].name == ingredient_to_be_moved

    def test_burger_get_price_true(self, burger, mock_bun, mock_ingredient):
        expected_result = (mock_bun.price * 2) + mock_ingredient.price
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == expected_result

    def test_get_receipt_true(self, cooked_burger):
        bun_name = cooked_burger.bun.get_name()
        ingredient_type = cooked_burger.ingredients[0].get_type().lower()
        ingredient_name = cooked_burger.ingredients[0].get_name()
        total = cooked_burger.get_price()
        expected_result = f"(==== {bun_name} ====)\n= {ingredient_type} {ingredient_name} =\n(==== {bun_name} ====)\n\nPrice: {total}"
        assert cooked_burger.get_receipt() == expected_result
        