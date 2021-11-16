
from Item import Item


# • UnitItem is a subclass of Item.
class UnitItem(Item):
    # This is the constructor for the UnitItem class.
    # • Every unit item has a quantity to store the number of units in this purchase. 
    def __init__(self, myQuantity: int, myPrice: float, myProdName: str):
        self.__myQuantity: int = myQuantity
        super().__init__(myPrice, myProdName)

    # All these values can be accessed and changed after the object is created.
    # therefore we have the following getters and setters
        
    #getter and setter for myQuantity
    @property
    def get_myQuantity(self) -> int:
        return self.__myQuantity

    @get_myQuantity.setter
    def set_myQuantity(self, qty:int) -> None:
        self.__myQuantity = qty

    # • It should be able to provide information detail (string) about the product product_name,
    # product unit price and the quantity required.

    def info(self) -> str:
        return "{} {} ${:,.2f}".format(super().info(), self.get_myQuantity, self.calculateCost())

    # • It should be able to provide the cost of the item for this purchase.

    def calculateCost(self) -> float:  # The return value must be an float
        return self.get_myQuantity * self.get_myPrice
