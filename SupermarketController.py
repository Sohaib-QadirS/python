
# The Controller (Supermarket) Class
# You will need a Supermarket class. There will only be one object of Supermarket class and
# this will act as the controller. It should have public methods that will be available to the
# different views. The supermarket should be able to:
# • Create and maintain objects of all the classes in the model – assume that the actual
# data for the objects will be provided correctly by the view.

from Customer import Customer
from ShoppingCart import ShoppingCart

from UnitItem import UnitItem
from WeightItem import WeightItem
from typing import List

'''
This is our controller class. It deals with both of our Model classes 
i.e. Customer Class and the Video class. It also maintains instances of
both classes.
'''


class Supermarket:

    # This is the constructor.It has 2 list to maintain all instances of our 2 model
    # classes
    def __init__(self):
        self.__allCustomers: List[Customer] = []

    # 1 getter for the list of customers
    @property
    def getCustomerList(self) -> List[Customer]:
        return self.__allCustomers

    # 2 Add a customer
    def addCustomer(self, cus_name: str):
        customer = Customer(cus_name)
        self.getCustomerList.append(customer)

    # 3 • Find a customer based on a customer’s product_name.
    def findCustomer(self, cus_name: str) -> Customer:
        for customer in self.getCustomerList:
            if customer.getMyName == cus_name:
                return customer

    # 4 finds a customer's card number based on a customer's product_name
    def findCustomerID(self, cus_name: str) -> int:
        cus = self.findCustomer(cus_name)
        return cus.getMyCardNumber

    # 4 • Return full information of a given customer.
    def cusInfo(self, cus_name: str) -> str:
        cus = self.findCustomer(cus_name)
        return cus.info()

    def cusName(self, customer: Customer) -> str:
        return customer.getMyName

    # 6 Add a unit item
    def addUnitItem(self, cus_name: str, item: str, price: float, amount: int):
        cus = self.findCustomer(cus_name)
        cus.addItemToCart(UnitItem(amount, price, item))

    # 7 Add a weight item
    def addWeightItem(self, cus_name: str, item: str, price: float):
        cus = self.findCustomer(cus_name)
        wItem = WeightItem(price, item)
        cus.addItemToCart(wItem)
        print(wItem.info())
        return (wItem.get_myWeight)

    # 8 Calculate customers current cart total
    def calCartTotal(self, cus_name: str) -> float:
        cus = self.findCustomer(cus_name)
        return cus.getMyCurrentCart.calcTotalCost()

    # 9 adds the current cart to the customer's cart list
    def addCusCart(self, cus_name: str, cart: ShoppingCart) -> None:
        cus = self.findCustomer(cus_name)
        cus.addShoppingCart(cart)

    # 10 customer starts shopping with an empty cart
    def startShopping(self, cus_name: str) -> None:
        cus = self.findCustomer(cus_name)
        cus.setMyCurrentCart = ShoppingCart()

    # 11 • Return the total sales earned by the supermarket.
    def totalSalesCus(self) -> float:
        total = 0
        for cus in self.getCustomerList:
            total = total + cus.getMyTotal
        return float(total)

    # see salesbycustomer
    # 12 • Return a summary of all the sales.(Each customer and the dates and totals of their carts, and overall total.)
    # # Each Customer product_name will be the key of the dictionary and their relevant info will be a list stored as value
    def salesByCustomer(self):
        allCusInfo = []
        for cus in self.getCustomerList:
            allCusInfo.append("{}".format(cus.info()))
            allCusInfo.append(" {}".format(cus.custTrans()))
        return allCusInfo

    # see findLargestPurchaseTotal
    # 13 • Return the customer with the most purchases
    # • Return the customer with the largest purchase total.
    def findLargestPurchaseTotal(self) -> str:
        curr = 0.0
        currCus: Customer = self.getCustomerList[0]
        for cus in self.getCustomerList:
            cusinf = cus.getMyTotal
            print(cusinf)
            next = cusinf
            if(next > curr):
                curr = next
                currCus = cus
        return currCus.getMyName

    # 14 calculates the customer's cart average
    def getCustAvg(self) -> float:
        totalAvg = 0
        for avg in self.avgCustomerSpending().keys():
            totalAvg = totalAvg + self.avgCustomerSpending()[avg]
        return round(totalAvg/float(self.totalCustomers()), 2)

    # # 15 displays transaction details for a customer
    def cusInformation(self, cus_name):
        cusInfo = []
        cus = self.findCustomer(cus_name)
        cusInfo.append("{}".format(self.cusInfo(cus_name)))
        cusInfo.append(cus.custDetailTrans())
        return cusInfo

    # • Return the total number of customers of the supermarket.
    def totalCustomers(self) -> int:
        return len(self.getCustomerList)

    # • Return the average spending of each customer per transaction.
    # each customer name will be the key and their avg spending the val
    def avgCustomerSpending(self) -> dict:
        avgDict = {}
        for cus in self.getCustomerList:
            avgDict.update({cus.getMyName: round(cus.cartAverage(),2)})
        return avgDict

    ####################    ******  ####################

    #Gets the weight of the current item
    def findCurrWeight(self, cart: ShoppingCart):
        if (cart.get_myItemList != []):
            itemWeight = (cart.get_myItemList[-1].info()).split()
            return itemWeight[2]

    #finds the current cart
    def findCurrCart(self, cus_name):
        cus = self.findCustomer(cus_name)
        return cus.getMyCurrentCart

    #gets the info for the current cart
    def currCartinfo(self, cus_name):
        cart = self.findCustomer(cus_name).getMyCurrentCart
        return cart.info()

    #Finds the current item in the cart i.e. last inserted item
    def findCurrItem(self, cart: ShoppingCart):
        if (cart.get_myItemList != []):
            itemInfo = (cart.get_myItemList[-1].info()).split()
            name_price = "{} {}".format(itemInfo[0], itemInfo[3])
            return name_price

    ######
    #Does everything that the the addcart button wants it to do
    def addCart(self, cus_name) -> None:
        cus = self.findCustomer(cus_name)
        self.addCusCart(cus_name, cus.getMyCurrentCart)
        cus.updateTotal(self.calCartTotal(cus.getMyName))
        cus.updateMyClubPoint(cus.calcClubPoints(cus.getMyTotal))

    #Complete functionality for the extended part of the project
    def salesByMonth(self, m):

        cusByMonth = {}
        for cus in self.getCustomerList:
            for cart in cus.getCartsList:
                if cart.get_myShoppingDate[3:5] == m:
                    cartPrice = cart.info().split()
                    cartPrice = float(cartPrice[1][1:])
                    if (("{} {}".format(cus.getMyName,cus.getMyCardNumber)) in cusByMonth):
                        cusByMonth[("{} {}".format(cus.getMyName,cus.getMyCardNumber))] += cartPrice
                    else:
                            cusByMonth.update({("{} {}".format(cus.getMyName,cus.getMyCardNumber)): cartPrice})
        formatedCustomers = ["Sales for Month: {}".format(m)]
        total = 0.0
        for c in cusByMonth.items():
            total += c[1]
            formatedCustomers.append("{} ${:,.2f}".format(c[0], c[1]))
        formatedCustomers.append("Total ${:,.2f}".format(total))
        return formatedCustomers

    #############################################

    # # • Return the list of shopping carts of a given customer.
    # def cusShoppingCarts(self, cus_name: str) -> List:
    #     cus = self.findCustomer(cus_name)
    #     return cus.getCartsList

    # # • Return the total due for customer’s list of shopping cart.
    # def totalDue(self, cus_name: str) -> float:
    #     cus = self.findCustomer(cus_name)
    #     return cus.getMyTotal

    # # 5 • Return the current club points for a given customer.
    # def currClubPoints(self, cus_name: str) -> int:
    #     cus = self.findCustomer(cus_name)
    #     return cus.getMyClubPoints

    # # 5 • Return the club points earned by a customer’s current shopping cart.
    # def cartClubPoints(self, cus_name: str) -> int:
    #     cus = self.findCustomer(cus_name)
    #     return cus.calcClubPoints()