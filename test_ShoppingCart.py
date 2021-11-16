import pytest
from ShoppingCart import ShoppingCart
from UnitItem import UnitItem


@pytest.fixture
def unit_items():
    return [UnitItem(3,5.5,"Milk"),UnitItem(6,1.75,"Bread"),UnitItem(1,7,"Eggs")]

@pytest.fixture
def cart():
    cartUnitItems = ShoppingCart()
    cartUnitItems.set_myItemList = [UnitItem(3, 5.5, "Milk"), UnitItem(6, 1.75, "Bread"), UnitItem(1, 7, "Eggs")]
    return cartUnitItems

def test_info():
    assert ShoppingCart().info() == "24/10/2021 $0.00"

def test_addItem(unit_items,cart):
    assert len(cart.get_myItemList) == 3
    assert cart.get_myItemList[0].info() == "Milk $5.50 3 $16.50"
    cart.addItem(unit_items[0])
    assert len(cart.get_myItemList) == 4

def test_calcTotalCost(unit_items,cart):
    assert cart.calcTotalCost() == 34.0