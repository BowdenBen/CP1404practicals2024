
from taxi import Taxi

class SilverServiceTaxi(Taxi):

    def __init__(self, fanciness, **kwargs):
        super().__init__(self, **kwargs)
        self.fanciness = fanciness
