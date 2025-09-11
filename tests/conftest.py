import pytest
from praktikum.database import Database
from tests.helpers.mocks import create_mock_bun, create_mock_ingredient


@pytest.fixture
def real_database():
    """Фикстура для создания реальной базы данных"""
    return Database()


@pytest.fixture
def mock_bun():
    """Фикстура для создания мока булочки"""
    return create_mock_bun()


@pytest.fixture
def mock_ingredient():
    """Фикстура для создания мока ингредиента"""
    return create_mock_ingredient()
