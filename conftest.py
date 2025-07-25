import pytest
from praktikum.bun import Bun
from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database
from data import BunData, IngredientData

@pytest.fixture
def bun():
    name = BunData.name
    price = BunData.price
    bun = Bun(name, price)
    return bun

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def burger_with_ingredient(burger, ingredient_sausage):
    burger.add_ingredient(ingredient_sausage)
    return burger

@pytest.fixture
def burger_with_two_ingredients(burger, ingredient_sausage, ingredient_hot_sauce):
    burger.add_ingredient(ingredient_sausage)
    burger.add_ingredient(ingredient_hot_sauce)
    return burger

@pytest.fixture
def cooked_burger(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.name = 'White'
    bun.price = 200
    bun.get_name.return_value = 'White'
    bun.get_price.return_value = 200
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.type = 'FILLING'
    ingredient.name = 'dinosaur'
    ingredient.price = 200
    ingredient.get_type.return_value = 'FILLING'
    ingredient.get_name.return_value = 'dinosaur'
    ingredient.get_price.return_value = 200
    return ingredient

@pytest.fixture
def ingredient_sausage():
    type = IngredientData.sausage['type']
    name = IngredientData.sausage['name']
    price = IngredientData.sausage['price']
    ingredient = Ingredient(type, name, price)
    return ingredient

@pytest.fixture
def ingredient_hot_sauce():
    type = IngredientData.hot_sauce['type']
    name = IngredientData.hot_sauce['name']
    price = IngredientData.hot_sauce['price']
    ingredient = Ingredient(type, name, price)
    return ingredient

@pytest.fixture
def database():
    database = Database()
    return database
