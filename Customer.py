'''
This class has all the attributes and methods related to customer 
'''
from ShoppingCart import ShoppingCart
from Item import Item
import math
from typing import List
import datetime


class Customer:
    # • Every customer should have a product_name, card number, club points, total value of all
    # purchases, current shopping cart and a list of shopping carts (previous purchases). All
    # these values (except for card number) can be accessed and changed after the object
    # is created.
    myNextCardNum = 10001

    def __init__(self, myName):
        self.__myCardNumber: int = Customer.myNextCardNum
        self.__myClubPoints: int = 0
        self.__myCurrentCart: ShoppingCart = ShoppingCart()
        self.__myName: str = myName
        self.__myTotal: float = 0
        self.__myCartsList: List[ShoppingCart] = []
        Customer.myNextCardNum += 1

    ##### Getters #####
    @property
    def getMyCardNumber(self) -> int:
        return self.__myCardNumber

    @property
    def getMyClubPoints(self) -> int:
        return self.__myClubPoints

    @property
    def getMyCurrentCart(self) -> ShoppingCart:
        return self.__myCurrentCart

    @property
    def getMyName(self) -> str:
        return self.__myName

    @property
    def getMyTotal(self) -> float:
        return self.__myTotal

    @property
    def getCartsList(self) -> List[ShoppingCart]:
        return self.__myCartsList

    ##### Setters ####

    @getMyClubPoints.setter
    def setMyClubPoints(self, value: int):
        self.__myClubPoints = value

    # This is meant to ensure that the date is current
    @getMyCurrentCart.setter
    def setMyCurrentCart(self, cart: ShoppingCart):
        self.__myCurrentCart = cart

    @getMyName.setter
    def setMyName(self, value: str):
        self.__myName = value

    # update the total purchase,
    @getMyTotal.setter
    def setMyTotal(self, value: float):
        self.__myTotal = value

    @getCartsList.setter
    def setMyCartList(self, value: ShoppingCart):
        self.__myTotal = value



    #update total purchase to date
    def updateTotal(self, value: float) -> None:
        self.setMyTotal = value + self.getMyTotal

    # • It should be able to provide customer information (string) about the customer’s
    # product_name, card number and the club points.
    def info(self) -> str:
        return "{} {} {} ${:,.2f}".format(self.getMyName, self.getMyCardNumber,
                                                                       self.getMyClubPoints,
                                                                       self.getMyTotal)

    # Adds item to curr cart
    def addItemToCart(self, item: Item):
        self.getMyCurrentCart.addItem(item)
        
    # • It should provide methods to add a shopping cart to its list of shopping carts, 
    def addShoppingCart(self, cart: ShoppingCart):
        self.getCartsList.append(cart)

    # calculate club points earned for the current purchase
    def calcClubPoints(self, value: float) -> int:
        return math.floor(value/10)
        
    # update the total club points.
    def updateMyClubPoint(self, value: int):
        self.setMyClubPoints = value

    ##########################
    # list the summary of all the previous transactions
    def custTrans(self) -> str:
        cartDetails = []
        for cart in self.getCartsList:
            cartDetails.append(cart.info())
        return '\n '.join(cartDetails)

    # List the details of all the previous transactions
    def custDetailTrans(self) -> str:
        cartDetails = []
        for cart in self.getCartsList:
            cartDetails.append(" {}".format(cart.info()))
            for item in cart.get_myItemList:
                cartDetails.append("   {}".format(item.info()))
        return '\n'.join(cartDetails)

    # average cart total
    def cartAverage(self) -> float:
        total = 0
        if len(self.getCartsList) != 0:
            for cart in self.getCartsList:
                total += cart.calcTotalCost()
            return float(total/len(self.getCartsList))
        else:
            return 0
