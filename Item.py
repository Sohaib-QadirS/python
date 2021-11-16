
# Item
from abc import ABC, abstractmethod


# Item is an abstract class.
# This class is to put together all the common params and funcs
# between WeightItems and UntItems
class Item(ABC):
    # This is the constructor for the Item class.
    # Every item should have a product product_name and a price.
    # the myPrice must be an int and myProdName must be string value.
    def __init__(self, myPrice: float, myProdName: str):
        self._myProdName: str = myProdName
        self._myPrice: float = myPrice

    # All these values can be accessed and changed after the object is created.
    # therefore we have the following getters and setters
    @property
    def get_myPrice(self) -> float:  # The return value must be an float
        return self._myPrice

    @property
    def get_myProdName(self) -> str:  # The return value must be a string
        return self._myProdName

    @get_myPrice.setter
    def set_myPrice(self, val: float):  # The parameter must be an float
        self._myPrice = val

    @get_myProdName.setter
    def set_myProdName(self, val: str):  # The parameter must be an string
        self._myProdName = val

    # • It should be able to provide information detail (string) about the product product_name and
    # the price per unit/weight.
    
    def info(self) -> str:  # The return value must be a string
        return "{} ${:,.2f}".format(self.get_myProdName, self.get_myPrice)

    # • It should also provide an abstract method to calculate the cost of the item.
    @abstractmethod
    def calculateCost(self) -> float:  # The return value must be an float
        pass
