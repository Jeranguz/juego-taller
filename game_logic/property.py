class Property:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.owner = None

    def buy(self, player):
        if self.owner is None:
            self.owner = player
            player.money -= self.price