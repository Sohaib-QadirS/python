
import datetime

import time
import random
from WeightItem import WeightItem
from UnitItem import UnitItem

from Item import Item
from typing import List


class ShoppingCart:
    # • Every shopping cart has a date of purchase and a list of items. The date cannot be
    # changed. The list of items can be accessed after the object is created.
    # This is the shopping cart constructor
    def __init__(self):
        self.__myShoppingDate: datetime = datetime.datetime.now().strftime("%d/%m/%Y")  # this must be of type date
        # self.__myShoppingDate: datetime = self.random_date("1/8/2021", "29/12/2021", random.random())
        self.__myItemList = []

    # The following are the getters and the setters.

    @property
    def get_myShoppingDate(self) -> datetime:  # returns date as datetime value
        return self.__myShoppingDate

    @property
    def get_myItemList(self):  # returns a list of items
        return self.__myItemList

    @get_myItemList.setter
    def set_myItemList(self, val: str):  # updatedList
        self.__myItemList = val

    # • It should be able to provide information detail (string) about the list of items, the
    # date and the total cost of all the items in the shopping cart.
    def info(self) -> str:  # The return value must be a string
        # return "{} ${:,.2f}".format(self.get_myShoppingDate.strftime("%d/%m/%Y"), self.calcTotalCost())
        return "{} ${:,.2f}".format(self.get_myShoppingDate, self.calcTotalCost())

    # •It should provide a method to add unit/weighted item to the list of items.
    def addItem(self, item: Item):  # adds the items product_name to the list
        self.__myItemList.append(item)

    # calculate the total cost of the items in the cart
    def calcTotalCost(self) -> float:
        cost = 0
        for item in self.get_myItemList:
            cost += item.calculateCost()
        return cost

###########################################################
    # Creating random dates to be able to use
    # the extended part of the project i.e. sales by date
    def str_time_prop(self, start, end, time_format, prop):
        """Get a time at a proportion of a range of two formatted times.

        start and end should be strings specifying times formatted in the
        given format (strftime-style), giving an interval [start, end].
        prop specifies how a proportion of the interval to be taken after
        start.  The returned time will be in the specified format.
        """

        stime = time.mktime(time.strptime(start, time_format))
        etime = time.mktime(time.strptime(end, time_format))

        ptime = stime + prop * (etime - stime)

        return time.strftime(time_format, time.localtime(ptime))

    def random_date(self,start, end, prop):
        return self.str_time_prop(start, end, '%d/%m/%Y', prop)