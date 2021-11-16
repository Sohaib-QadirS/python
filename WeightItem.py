"""
Name: Sohaib Qadir
ID: 1149925
Paper: COMP642
Assessment 3
"""

import random
from Item import Item


# • WeightItem is a subclass of Item.
class WeightItem(Item):
    # • Every weight item stores the weight of item in a purchase. This value can be only be
    # accessed after the object is created.
    def __init__(self, myPrice: float, myProdName: str):
        self.__myWeight: float = self.scale()
        super().__init__(myPrice, myProdName)

    # All these values can be accessed and changed after the object is created.
    # therefore we have the following getters and setters
     
    #getter and setter for myWeight
    @property
    def get_myWeight(self) -> int:
        return self.__myWeight

    # • It should be able to provide information detail (string) about the product product_name,
    # product unit price and the weight required.

    def info(self) -> str:
        return "{} {:,.2f}Kg ${:,.2f}".format(super().info(), self.get_myWeight, self.calculateCost())

    # • It should be able to provide the cost of the item for this purchase

    def calculateCost(self) -> float:  # The return value must be a float
        return self.get_myWeight * super().get_myPrice

    # • It should have a method scale() to generate a random weight between 0.0 to 4.00
    # such that when a new object is created, a random weight is generated as the weight
    # of the item.
    def scale(self) -> float:
        rand = random.uniform(0.1, 4.0)
        return round(rand, 2)

    
