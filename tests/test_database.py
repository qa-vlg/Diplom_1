import pytest

class TestDatabase:

    @pytest.mark.parametrize('index, name, price', [(0, "black bun", 100),
                                                    (1, "white bun", 200),
                                                    (2, "red bun", 300)])
    def test_buns_values_true(self, database, index, name, price):
        buns = database.available_buns()
        assert buns[index].name == name and buns[index].price == price

    @pytest.mark.parametrize('index, type, name, price', [(0, 'SAUCE', "hot sauce", 100),
                                                        (1, 'SAUCE', "sour cream", 200),
                                                        (2, 'SAUCE', "chili sauce", 300),
                                                        (3, 'FILLING', "cutlet", 100),
                                                        (4, 'FILLING', "dinosaur", 200),
                                                        (5, 'FILLING', "sausage", 300)])
    
    def test_ingredients_values_true(self, database, index, type, name, price):
        ingredients = database.available_ingredients()
        assert ingredients[index].type == type and ingredients[index].name == name and ingredients[index].price == price
        