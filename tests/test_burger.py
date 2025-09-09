import pytest
from praktikum.burger import Burger
from tests.helpers.mocks import create_mock_bun, create_mock_ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты для класса Burger"""

    def test_set_buns(self):
        burger = Burger()
        mock_bun = create_mock_bun()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = create_mock_ingredient()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = create_mock_ingredient()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_changes_order(self):
        burger = Burger()
        ing1 = create_mock_ingredient(name="ing1")
        ing2 = create_mock_ingredient(name="ing2")

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ing2, ing1]

    def test_get_price_calculations(self):
        burger = Burger()
        bun = create_mock_bun(price=150)
        ingredient = create_mock_ingredient(price=75)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 375  

    def test_get_price_without_bun_returns_zero(self):
        burger = Burger()
        ingredient = create_mock_ingredient(price=50)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 0

    def test_get_price_empty_burger_returns_zero(self):
        assert Burger().get_price() == 0

    def test_get_receipt_full_burger(self):
        burger = Burger()
        bun = create_mock_bun(name="test bun", price=500)
        sauce = create_mock_ingredient(
            name="test sauce", price=100, ingredient_type=INGREDIENT_TYPE_SAUCE
        )
        filling = create_mock_ingredient(
            name="test filling", price=200, ingredient_type=INGREDIENT_TYPE_FILLING
        )

        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        expected = (
            "(==== test bun ====)\n"
            "= sauce test sauce =\n"
            "= filling test filling =\n"
            "(==== test bun ====)\n"
            "\n"
            "Price: 1300"
        )

        assert burger.get_receipt() == expected

    def test_get_receipt_only_bun(self):
        burger = Burger()
        bun = create_mock_bun(name="black bun", price=100)
        burger.set_buns(bun)

        expected = "(==== black bun ====)\n" "(==== black bun ====)\n" "\n" "Price: 200"

        assert burger.get_receipt() == expected

    def test_get_receipt_empty_burger_contains_zero_price(self):
        assert "Price: 0" in Burger().get_receipt()
