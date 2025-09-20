import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient"""

    def test_get_type_returns_correct_type(self):
        """Тестирование метода get_type"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_name_returns_correct_name(self):
        """Тестирование метода get_name"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        assert ingredient.get_name() == "hot sauce"

    def test_get_price_returns_correct_price(self):
        """Тестирование метода get_price"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        assert ingredient.get_price() == 100.0

    def test_ingredient_with_sauce_type(self):
        """Тестирование ингредиента типа SAUCE"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_ingredient_with_filling_type(self):
        """Тестирование ингредиента типа FILLING"""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100.0)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

    def test_ingredient_with_empty_name(self):
        """Тестирование ингредиента с пустым именем"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "", 100.0)
        assert ingredient.get_name() == ""

    def test_ingredient_with_zero_price(self):
        """Тестирование ингредиента с нулевой ценой"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 0.0)
        assert ingredient.get_price() == 0.0

    def test_ingredient_with_float_price(self):
        """Тестирование ингредиента с дробной ценой"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50.5)
        assert ingredient.get_price() == 50.5

    @pytest.mark.parametrize(
        "ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
    )
    def test_ingredient_with_different_types(self, ingredient_type):
        """Параметризованный тест разных типов ингредиентов"""
        ingredient = Ingredient(ingredient_type, "test", 100.0)
        assert ingredient.get_type() == ingredient_type
