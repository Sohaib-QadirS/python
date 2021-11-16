import pytest
from UnitItem import UnitItem

@pytest.fixture
def unit_items():
    return [UnitItem(3,5.5,"Milk"),UnitItem(6,1.75,"Bread"),UnitItem(1,7,"Eggs")]

def test_info(unit_items):
    assert unit_items[0].info() == "Milk $5.50 3 $16.50"

def test_calculateCost(unit_items):
    assert unit_items[0].calculateCost() == 16.50
