import pytest
import csv
from Customer import Customer
from ShoppingCart import ShoppingCart
from UnitItem import UnitItem
from WeightItem import WeightItem
# loading all customers
@pytest.fixture
def my_customers():
    customers = []
    with open('Customers.txt', newline='') as csvfile:
        spreader = csv.reader(csvfile, quotechar='|')
        for row in spreader:
            customers.append(Customer(row[0]))
    return customers

@pytest.fixture
def unit_items():
    return [UnitItem(3,5.5,"Milk"),UnitItem(6,1.75,"Bread"),UnitItem(1,7,"Eggs")]

@pytest.fixture
def weight_items():
    return [WeightItem(7.99,"Fish"),WeightItem(2.99,"Banana"),WeightItem(13,"Tomato")]

@pytest.fixture
def cart():
    cartUnitItems = ShoppingCart()
    cartUnitItems.set_myItemList = [UnitItem(3, 5.5, "Milk"), UnitItem(6, 1.75, "Bread"), UnitItem(1, 7, "Eggs")]
    cartWeightItems = ShoppingCart()
    cartWeightItems.set_myItemList = [WeightItem(7.99,"Fish"),WeightItem(2.99,"Banana"),WeightItem(13,"Tomato")]
    return [cartUnitItems, cartWeightItems]

def test_customer_AddItemsToCart(my_customers,weight_items):
    my_customers[0].setMyCurrentCart = ShoppingCart()
    assert my_customers[0].getMyCurrentCart.get_myItemList == []
    my_customers[0].addItemToCart(weight_items[0])
    assert len(my_customers[0].getMyCurrentCart.get_myItemList) == 1
    my_customers[0].addItemToCart(weight_items[1])
    assert len(my_customers[0].getMyCurrentCart.get_myItemList) == 2

def test_customer_updateTotal(my_customers):
    assert my_customers[0].getMyTotal == 0
    my_customers[0].updateTotal(5.69)
    assert my_customers[0].getMyTotal == 5.69

def test_customer_ClubPoints(my_customers):
    assert my_customers[0].getMyClubPoints == 0
    my_customers[0].updateMyClubPoint(my_customers[0].calcClubPoints(29))
    assert my_customers[0].getMyClubPoints == 2

def test_customer_addShoppingCart(my_customers,cart):
    assert my_customers[0].getCartsList == []
    my_customers[0].addShoppingCart(cart[0])
    assert my_customers[0].getCartsList != []

def test_customer_custTrans(my_customers, cart):
    assert (my_customers[0].custTrans()) == ""
    my_customers[0].addShoppingCart(cart[0])
    assert (my_customers[0].custTrans()) == "24/10/2021 $34.00"

def test_customer_custDetailTrans(my_customers, cart):
    assert (my_customers[0].custDetailTrans()) == ""
    my_customers[0].addShoppingCart(cart[0])
    assert (my_customers[0].custDetailTrans()) == " 24/10/2021 $34.00\n   Milk $5.50 3 $16.50\n   Bread $1.75 6 $10.50\n   Eggs $7.00 1 $7.00"

def test_customer_cartAverage(my_customers, cart):
    assert my_customers[0].cartAverage() == 0
    my_customers[0].addShoppingCart(cart[0])
    assert my_customers[0].cartAverage() == 34

