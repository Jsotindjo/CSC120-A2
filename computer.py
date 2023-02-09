class Computer:
    # This class assigns each part of the computer as a string or an integer.
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # The code below assigns each part of the computer with itself
    def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price  
        

    # This explains how to print the details of the computer
    def print_details(self):
        print(self.description)
        print(self.processor_type)
        print(self.hard_drive_capacity)
        print(self.memory)
        print(self.operating_system)
        print(self.year_made)
        print(self.price)

def main():
    c = Computer("Mac Pro", "M2", 64, 128, 72, 2022, 1399)
    c.print_details()

main()