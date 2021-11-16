import pytest
import csv
from Customer import Customer
from ShoppingCart import ShoppingCart

from UnitItem import UnitItem
from WeightItem import WeightItem
from SupermarketController import Supermarket
from typing import List

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
def market():
    supermarket = Supermarket()
    with open('Customers.txt', newline='') as csvfile:
        spreader = csv.reader(csvfile, quotechar='|')
        for row in spreader:
            supermarket.getCustomerList.append(Customer(row[0]))
    return supermarket

@pytest.fixture
def cart():
    cartUnitItems = ShoppingCart()
    cartUnitItems.set_myItemList = [UnitItem(3, 5.5, "Milk"), UnitItem(6, 1.75, "Bread"), UnitItem(1, 7, "Eggs")]
    cartWeightItems = ShoppingCart()
    cartWeightItems.set_myItemList = [WeightItem(7.99,"Fish"),WeightItem(2.99,"Banana"),WeightItem(13,"Tomato")]
    return [cartUnitItems, cartWeightItems]

def test_addCustomer():
    supermarket = Supermarket()
    assert len(supermarket.getCustomerList) == 0
    supermarket.addCustomer("Mark Z")
    assert len(supermarket.getCustomerList) == 1

def test_findCustomer(market):
    market.addCustomer("Mark Z")
    assert market.findCustomer("Mark Z") == market.getCustomerList[16]

def test_findCustomerID(market):
    market.addCustomer("Mark Z")
    assert market.findCustomerID("Mark Z") == 10035

def test_cusInfo(market):
    market.addCustomer("Mark Z")
    assert market.cusInfo("Mark Z") == "Mark Z 10052 0 $0.00"

def test_cusName(market):
    market.addCustomer("Mark Z")
    assert market.cusName(market.getCustomerList[16]) == "Mark Z"

def test_UnitItem(market):
    market.addCustomer("Mark Z")
    market.addUnitItem("Mark Z", "Silk", 5.5, 2)
    assert market.getCustomerList[16].getMyCurrentCart.get_myItemList[0].get_myProdName == "Silk"

def test_WeightItem(market):
    market.addCustomer("Mark Z")
    market.addWeightItem("Mark Z", "Silk", 5.5)
    assert market.getCustomerList[16].getMyCurrentCart.get_myItemList[0].get_myProdName == "Silk"

def test_calCartTotal(market):
    market.addCustomer("Mark Z")
    market.addUnitItem("Mark Z", "Silk", 5.5, 2)
    assert (market.calCartTotal("Mark Z")) == 11.0

def test_addCusCart(market):
    market.addCustomer("Mark Z")
    assert len(market.getCustomerList[16].getCartsList) == 0
    market.addUnitItem("Mark Z", "Silk", 5.5, 2)
    market.addCusCart("Mark Z", market.getCustomerList[16].getMyCurrentCart)
    assert len(market.getCustomerList[16].getCartsList) == 1

def test_startShopping(market):
    market.addCustomer("Mark Z")
    market.addUnitItem("Mark Z", "Silk", 5.5, 2)
    market.addCusCart("Mark Z", market.getCustomerList[16].getMyCurrentCart)
    assert len(market.getCustomerList[16].getMyCurrentCart.get_myItemList) == 1
    market.startShopping("Mark Z")
    assert len(market.getCustomerList[16].getMyCurrentCart.get_myItemList) == 0

def test_totalSalesCus(market, cart):
    market.addCustomer("Mark Z")
    market.addUnitItem("Mark Z", "Silk", 5.5, 2)
    market.addCart("Mark Z")
    assert (market.totalSalesCus()) == 11.0

# salesByCustomer

def test_salesByCustomer(market, cart):
    market.addCustomer("Mark Z")
    market.addUnitItem("Mark Z", "Silk", 5.5, 2)
    market.addCart("Mark Z")
    assert (market.salesByCustomer()) == ['John Gray 10172 0 $0.00', ' ', 'Louise Smith 10173 0 $0.00', ' ',
                                          'Henry Waite 10174 0 $0.00', ' ', 'Harry Liu 10175 0 $0.00', ' ',
                                          'Joe Blogg 10176 0 $0.00', ' ', 'Kitty Anderson 10177 0 $0.00', ' ',
                                          'Sara Peters 10178 0 $0.00', ' ', 'Jaime Watson 10179 0 $0.00', ' ',
                                          'Katie Smith 10180 0 $0.00', ' ', 'Jane Tou 10181 0 $0.00', ' ',
                                          'Grace Yapp 10182 0 $0.00', ' ', 'Mary Evans 10183 0 $0.00', ' ',
                                          'Carla Robertson 10184 0 $0.00', ' ', 'Martin Davis 10185 0 $0.00', ' ',
                                          'Ian Morgan 10186 0 $0.00', ' ', 'Sam Stephenson 10187 0 $0.00', ' ',
                                          'Mark Z 10188 1 $11.00', ' 24/10/2021 $11.00']

def test_findLargestPurchaseTotal(market, cart):
    market.addCustomer("Mark Z")
    market.addUnitItem("Mark Z", "Silk", 5.5, 2)
    market.addCart("Mark Z")
    assert (market.findLargestPurchaseTotal()) == "Mark Z"

def test_getCustAvg(market, cart):
    market.addCustomer("Mark Z")
    market.addCustomer("Mark A")
    market.addUnitItem("Mark Z", "Silk", 9, 2)
    market.addCart("Mark Z")
    assert (market.getCustAvg()) == 1

def test_cusInformation(market, cart):
    market.addCustomer("Mark Z")
    market.addUnitItem("Mark Z", "Silk", 5.5, 2)
    market.addCart("Mark Z")
    assert (market.cusInformation("Mark Z")) == ['Mark Z 10240 1 $11.00', ' 24/10/2021 $11.00\n   Silk $5.50 2 $11.00']

def test_totalCustomers(market):
    assert market.totalCustomers() == 16

def test_avgCustomerSpending(market):
    assert (market.avgCustomerSpending()) == {'John Gray': 0, 'Louise Smith': 0, 'Henry Waite': 0, 'Harry Liu': 0, 'Joe Blogg': 0, 'Kitty Anderson': 0, 'Sara Peters': 0, 'Jaime Watson': 0, 'Katie Smith': 0, 'Jane Tou': 0, 'Grace Yapp': 0, 'Mary Evans': 0, 'Carla Robertson': 0, 'Martin Davis': 0, 'Ian Morgan': 0, 'Sam Stephenson': 0}

def test_findCurrCart(market):
    market.addCustomer("Mark Z")
    assert (market.findCurrCart("Mark Z")) == market.getCustomerList[16].getMyCurrentCart

def test_currCartinfo(market):
    market.addCustomer("Mark Z")
    assert (market.currCartinfo("Mark Z")) == market.getCustomerList[16].getMyCurrentCart.info()

def test_findCurrItem(market,cart):
    market.addCustomer("Mark Z")
    assert (market.findCurrItem(cart[0])) == "Eggs $7.00"

def test_salesByMonth(market,cart):
    market.addCustomer("Mark Z")
    assert (market.salesByMonth(10)) == ['Sales for Month: 10', 'Total $0.00']