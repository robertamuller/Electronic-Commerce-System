from enum import Enum

class Brand(Enum):
    WEPINK = 1
    READRAGON = 2
    ROUPA = 3

# Product Class structure:
class Product:
    def __init__(self, name, bar_code, price):
        self.name = name
        self.bar_code = bar_code
        self.price = price

# Creates a new product specialization: "Beauty Products"
class Makeup_Base(Product):
    #Some examples of beauty product classification are nail polish, makeup, perfumes...
    def __init__(self, name, bar_code, price):
        super().__init__(name, bar_code, price)
        self.brand = Brand.WEPINK
    
# Creates a new product specialization: "Game Products"
class Headset(Product):
    def __init__(self, name, bar_code, price):
        super().__init__(name, bar_code, price)
        self.brand = Brand.READRAGON

# Creates a new product specialization: "Game Products"
class ALGO(Product):
    def __init__(self, name, bar_code, price):
        super().__init__(name, bar_code, price)
        self.brand = Brand.ROUPA

class Inventory(Product):
    Storage = []
    Sold_itens = []

    def Restocking(self, Storage):
        Storage.append(self.name)

    def Sell(self, Storage, Sold_itens):

        if self.name not in Storage:
            raise ValueError("Não tem no estoque")
        Storage.remove(self.name)
        Sold_itens.append(self.name)

    def Return(self, Storage, Sold_itens):
        Storage.append(self.name)
        Sold_itens.remove(self.name)


# base = Makeup_Base('Base da Vírginia', '1234567', 'R$ 799,99', 'Wepink Beauty')
# zeus = Headset('Headset Gamer Redragon Zeus', '87217217', 'R$ 199,99', 'Redragon')
zeus_2 = Headset('Headset Gamer Redragon Zeus 2', '87217216', 'R$ 399,99')
zeus_3 = Headset('Headset Gamer Redragon Zeus 3', '87217216', 'R$ 399,99')


Inventory.Restocking(zeus_2, Inventory.Storage)

print(Inventory.Storage)
print(Inventory.Sold_itens)

Inventory.Sell(zeus_3, Inventory.Storage, Inventory.Sold_itens)

print(Inventory.Storage)
print(Inventory.Sold_itens)



