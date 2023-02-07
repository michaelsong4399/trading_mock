from maker_taker_base import Taker, Maker, Side, Market, test
from typing import Type


class CindyEmilyYihongMaker(Maker):
    side_map = {Side.buy: 1, Side.sell: -1, Side.notrade: 0}

    def __init__(self) -> None:
        self.round = 0
        self.bounds = (75, 1, 85, 1)
        

    def get_market(self, round: int) -> Market():
        # self.round = round
        self.round = round
        return Market(self.bounds[0], self.bounds[1], self.bounds[2], self.bounds[3])
        


    def update_trade(self, side: Type[Side]) -> None:
        if self.round == 0:
            if side == Side.buy:
                self.bounds = (85,1,95,1)
            else:
                self.bounds = (65,1,75,1)
        elif self.round == 1:
            if self.bounds[0] == 85:
                if side == Side.buy:
                    self.bounds = (90,1000,100,1000)
                else:
                    self.bounds = (80,1000,90,1000)

            else:
                if side == Side.buy:
                    self.bounds = (70,1000,80,1000)
                else:
                    self.bounds = (30,1,40,1)

        return