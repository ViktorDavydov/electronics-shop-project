import pytest
from src.phone import Phone


def test_Phone():
    """Тестирование поля кол-ва сим карт класса Phone"""
    phone = Phone("Смартфон", 50000, 10, 2)
    assert phone.number_of_sim == 2


def test_repr():
    """Тестирование repr"""
    phone = Phone("Смартфон", 10000, 8, 3)
    assert repr(phone) == "Phone('Смартфон', 10000, 8, 3)"


def test_setter():
    """Тестирование сеттера"""
    phone = Phone("Смартфон", 20000, 10, 3)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2
    phone.number_of_sim = 0
    assert phone.number_of_sim == 2
