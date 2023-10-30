from enum import Enum

class Brand(Enum):
    WEPINK = 1
    REDRAGON = 2
    FGV_EDITORA = 3

# Product Class structure
class Product:
    def __init__(self, name, bar_code, price):
        self.name = name
        self.bar_code = bar_code
        self.price = price

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"


# Creates a new product specialization: "Makeup Products"
class Makeup_Base(Product):
    def __init__(self, name, bar_code, price):
        super().__init__(name, bar_code, price)
        self.brand = Brand.WEPINK

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"
    
# Creates a new product specialization: "Redragon Headsets"
class Headset(Product):
    def __init__(self, name, bar_code, price):
        super().__init__(name, bar_code, price)
        self.brand = Brand.REDRAGON
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"

# Creates a new product specialization: "Books from FGV Editora"
class Book(Product):
    def __init__(self, name, bar_code, price):
        super().__init__(name, bar_code, price)
        self.brand = Brand.FGV_EDITORA
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"

# Creates the inventory Class
class Inventory:
    Storage = []
    Sold_itens = []

    def Restocking(self, Storage):
        Storage.append(self)

    def Sell(self, Storage, Sold_itens):
        if self not in Storage:
            raise ValueError("Não há deste item no estoque")
        Storage.remove(self)
        Sold_itens.append(self)

    def Return(self, Storage, Sold_itens):
        Storage.append(self)
        Sold_itens.remove(self)



# base = Makeup_Base('Base da Vírginia', '1234567', 'R$ 799,99', 'Wepink Beauty')
# zeus = Headset('Headset Gamer Redragon Zeus', '87217217', 'R$ 199,99', 'Redragon')
zeus_2 = Headset('Headset Gamer Redragon Zeus 2', 87217216, 399.99)
zeus_3 = Headset('Headset Gamer Redragon Zeus 3', 87217216, 399.99)


print(zeus_2)

lista = [zeus_2]

print(lista)

Inventory.Restocking(zeus_2, Inventory.Storage)

print(Inventory.Storage)
print(Inventory.Sold_itens)

Inventory.Sell(zeus_2, Inventory.Storage, Inventory.Sold_itens)

print(Inventory.Storage)
print(Inventory.Sold_itens)
