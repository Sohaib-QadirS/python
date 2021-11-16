import pytest
from WeightItem import WeightItem

@pytest.fixture
def weight_items():
    return [WeightItem(7.99,"Fish"),WeightItem(2.99,"Banana"),WeightItem(13,"Tomato")]

def test_info(weight_items):
    assert weight_items[0].info() == "Fish $7.99 {:,.2f}Kg ${:,.2f}".format(weight_items[0].get_myWeight, weight_items[0].calculateCost())

def test_calculateCost(weight_items):
    assert weight_items[0].calculateCost() == 7.99 * weight_items[0].get_myWeight