# imports
import pytest
from src.keyboard import Keyboard


def test_Keyboard():
    """Class Keyboard testing"""
    kb = Keyboard("Razer Anansi", 5000, 5)
    assert kb.name == "Razer Anansi"
    assert kb.price == 5000
    assert kb.quantity == 5
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"
