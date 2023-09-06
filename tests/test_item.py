import pytest
from src.item import Item


def test_Item():
    """Тестирование класса Item"""
    item1 = Item("Смартфон", 5, 10)
    item2 = Item("Ноутбук", 0, 50000)
    assert item1.calculate_total_price() == 50
    assert item2.calculate_total_price() == 0
    assert item1.apply_discount() is None
    assert item1.name == "Смартфон"
