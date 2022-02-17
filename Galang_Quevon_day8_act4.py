class House:
    def __init__(self, floorsize,noOfFloors, noOfDoors):
        self.floorsize1 = floorsize
        self.noOffloors1 = noOfFloors
        self.noOfDoors1 = noOfDoors

    def switchOn(self):
        self.lightOpen()
        self.ovenOpen()

    def lightOpen(self):
        print('Open Lights')

    def ovenOpen(self):
        print('Open Oven')

class TownHouse(House):
    def __init__(self, floorsize,noOfFloors, noOfDoors):
        super().__init__(floorsize, noOfFloors, noOfDoors)

    def TownHouseProperties(self):
        print()
        print('House Floor Size: ',self.floorsize1)
        print('House No. of Floors: ',self.noOffloors1)
        print('House No. of Doors: ',self.noOfDoors1)

townhouse = TownHouse(143, 2, 4)
townhouse.TownHouseProperties()
townhouse.switchOn()

townhouse1 = TownHouse(50, 1, 2)
townhouse1.TownHouseProperties()
townhouse1.switchOn()

townhouse2 = TownHouse(70, 3, 6)
townhouse2.TownHouseProperties()
townhouse2.switchOn()