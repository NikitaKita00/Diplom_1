import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.helpers.mocks import create_mock_bun, create_mock_ingredient


@pytest.fixture
def mock_bun():
    """Фикстура для создания мока булочки"""
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_ingredient_sauce():
    """Фикстура для создания мока соуса"""
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 100.0
    return ingredient


@pytest.fixture
def mock_ingredient_filling():
    """Фикстура для создания мока начинки"""
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_price.return_value = 100.0
    return ingredient


@pytest.fixture
def real_database():
    """Фикстура для создания реальной базы данных"""
    from praktikum.database import Database

    return Database()


@pytest.fixture
def mock_bun():
    return create_mock_bun()


@pytest.fixture
def mock_ingredient():
    return create_mock_ingredient()
