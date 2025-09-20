import pytest
from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun"""

    def test_get_name_returns_correct_name(self):
        """Тестирование метода get_name"""
        bun = Bun("black bun", 100.0)
        assert bun.get_name() == "black bun"

    def test_get_price_returns_correct_price(self):
        """Тестирование метода get_price"""
        bun = Bun("black bun", 100.0)
        assert bun.get_price() == 100.0

    def test_bun_with_empty_name(self):
        """Тестирование булочки с пустым именем"""
        bun = Bun("", 100.0)
        assert bun.get_name() == ""

    def test_bun_with_zero_price(self):
        """Тестирование булочки с нулевой ценой"""
        bun = Bun("test bun", 0.0)
        assert bun.get_price() == 0.0

    def test_bun_with_float_price(self):
        """Тестирование булочки с дробной ценой"""
        bun = Bun("test bun", 99.99)
        assert bun.get_price() == 99.99

    @pytest.mark.parametrize("name", ["black bun", "white bun", "red bun"])
    def test_bun_with_different_names(self, name):
        """Параметризованный тест разных имен булочек"""
        bun = Bun(name, 100.0)
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", [100.0, 200.0, 300.0])
    def test_bun_with_different_prices(self, price):
        """Параметризованный тест разных цен булочек"""
        bun = Bun("test bun", price)
        assert bun.get_price() == price
