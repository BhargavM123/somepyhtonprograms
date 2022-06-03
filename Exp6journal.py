class Cont:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


cont1 = Cont("bhargav", 1010)
cont2 = Cont("mahajan", 1011)

cont1.display()

cont2.display()
