from computer import*
class ResaleShop:
    # This lets the program know that the inventory will be a list
    inventory: list


    # This assigns the inventory of the ResaleShop to itself
    def __init__(self):
        self.inventory = []
    # Takes the inventory and adds an element to the end of the list demonstrating a purchase
    def buy(self, c:Computer):
        self.inventory.append(c)
    # Takes the inventory and takes away an element to the list, demonstrating selling a computer
    def sell(self, c:Computer,):
        if c in self.inventory:
            self.inventory.remove(c)
        else: 
            print("Computer is not in inventory. It cannot be sold")
    # Takes the inventory and changes its price. If not, prints out a message.
    def price_change(self,c:Computer):
        if c in self.inventory:
            self.inventory.pop(c(6))
            print(self.inventory.append(c(1299)))
        else: 
            print("Computer is not in inventory. Price cannot be updated")


        
    # What methods will you need?
def main():
    myStore = ResaleShop()
    c = Computer("Mac Pro", "M2", 64, 128, 72, 2022, 1399)
    myStore.buy(c)
    myStore.sell(c)
    myStore.price_change(c)
main()
