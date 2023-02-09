from computer import*
class ResaleShop:
    # What attributes will it need?
    inventory: list


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
    
    def buy(self, c:Computer):
        self.inventory.append(c)

    def sell(self, c:Computer):
        if c in self.inventory:
            self.inventory.remove(c)
        else: print("Computer is not in inventory. It cannot be sold")

    def price_change(self,c:Computer):
        if c in self.inventory:
            self.inventory.append(c([6]))
        else: print("Computer is not in inventory. Price cannot be updated")

        

    # What methods will you need?
def main():
    myStore = ResaleShop()
    c = Computer("Mac Pro", "M2", 64, 128, 72, 2022, 1399)
    myStore.buy(c)
    myStore.sell(c)
    myStore.price_change(c)
main()
