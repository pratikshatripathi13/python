class OnlinePlatform:
    def __init__(self, platform):
        self.platform = platform

    def show_platform(self):
        print("Platform:", self.platform)


class Buyer(OnlinePlatform):
    def __init__(self, platform):
        OnlinePlatform.__init__(self, platform)

    def buy(self):
        print("Buying products")


class Seller(OnlinePlatform):
    def __init__(self, platform):
        OnlinePlatform.__init__(self, platform)

    def sell(self):
        print("Selling products")


class MarketplaceUser(Buyer, Seller):
    def __init__(self, platform):
        Buyer.__init__(self, platform)
        Seller.__init__(self, platform)

    def trade(self):
        self.show_platform()
        self.buy()
        self.sell()


u = MarketplaceUser("ShopZone")
u.trade()
