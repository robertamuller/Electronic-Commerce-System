from enum import Enum

class Brand(Enum):
    WEPINK = 1
    REDRAGON = 2
    FGV_EDITORA = 3

# Product Class structure
class Product:
    def __init__(self, name: str, bar_code: int, price: float):
        self.name = name
        self.bar_code = bar_code
        self.price = price

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"

# Creating a new product specialization: "Beauty Products"
class Beauty_Products(Product):
    def __init__(self, name, bar_code, price):
        super().__init__(name, bar_code, price)
        self.brand = Brand.WEPINK

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"
    
# Creating a new product specialization: "Redragon Headsets"
class Headset(Product):
    def __init__(self, name, bar_code, price):
        super().__init__(name, bar_code, price)
        self.brand = Brand.REDRAGON
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"

# Creating a new product specialization: "Books from FGV Editora"
class Book(Product):
    def __init__(self, name, bar_code, price):
        super().__init__(name, bar_code, price)
        self.brand = Brand.FGV_EDITORA
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"
    
# Own exception class for selling method
class NotInStorage(Exception):
    def __init__(self, mensagem = "Não há este item no estoque!"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

# Creating the inventory Class
class Inventory:
    Storage = []
    Sold_itens = []

    # Method that restocks a product
    def Restocking(self):
        Inventory.Storage.append(self)
        print(f"{self.name} was restocked, there are currently {Inventory.Storage.count(self)} itens in stock.")

    # Method that sells a product
    def Sell(self):
        if self not in Inventory.Storage:
            raise NotInStorage
        Inventory.Storage.remove(self)
        Inventory.Sold_itens.append(self)
        print(f"{self.name} was sold for R${self.price}.")

    # Method that returns a product
    def Return(self):
        Inventory.Storage.append(self)
        Inventory.Sold_itens.remove(self)
        print(f"{self.name} was returned.")

print('-' * 60, f'\n{"Electronic Commerce System":^60}\n', '-' * 60)

# Restocking
Inventory.Restocking(base_virginia)
Inventory.Restocking(base_virginia)
Inventory.Restocking(base_virginia)
Inventory.Restocking(base_virginia)
Inventory.Restocking(perfume_virginia)
Inventory.Restocking(perfume_virginia)
Inventory.Restocking(rademaker_book)
Inventory.Restocking(rademaker_book)
Inventory.Restocking(rademaker_book)
Inventory.Restocking(asla_book)
Inventory.Restocking(eduardo_wagner_book)
Inventory.Restocking(paulo_cezar_book)
Inventory.Restocking(paulo_cezar_book)
Inventory.Restocking(zeus_2)
Inventory.Restocking(zeus_2)
Inventory.Restocking(pandora)
Inventory.Restocking(pandora)
Inventory.Restocking(pandora)
print('-' * 60)

# Sells
Inventory.Sell(base_virginia)
Inventory.Sell(rademaker_book)
Inventory.Sell(rademaker_book)
Inventory.Sell(zeus_2)
Inventory.Sell(eduardo_wagner_book)
Inventory.Sell(pandora)
print('-' * 60)

# Returning
Inventory.Return(base_virginia)
Inventory.Return(pandora)
print('-' * 60)
