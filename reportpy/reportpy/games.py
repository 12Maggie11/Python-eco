class Player:
    def __init__(self, name, strategies):
        self.name = name 
        self.strategies = strategies
        self.played_strategy = None
    def play(self, played_strategy):
        self.played_strategy = played_strategy

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2 
    def payoff(self):
        strategy1 = self.player1.played_strategy
        strategy2 = self.player2.played_strategy
        
        if strategy1 not in self.player1.strategies:
            raise ValueError("Invalid strategy")
        elif strategy2 not in self.player2.strategies:
            raise ValueError("Invalid strategy")
        elif strategy1 > strategy2:
            result = ((20 - strategy1), (-strategy2))
            return result
        elif strategy1 < strategy2:
            result = ((-strategy1), (20 - strategy2))
            return result
        elif strategy1 == strategy2:
            result = ((10 - strategy1), (10 - strategy2))
            return result
        else:
            return "Error"
        
player1_strategies = list(range(11)) # [0,1,2,3,4,5,6,7,8,9,10]
player2_strategies = list(range(11)) # [0,1,2,3,4,5,6,7,8,9,10]

player1 = Player(None, player1_strategies)
player2 = Player(None, player2_strategies)

game = Game(player1, player2)

data = []
def append():
    values_to_append = [player1.name, player2.name, player1.played_strategy, player2.played_strategy, *game.payoff()]
    data.append(values_to_append)
    return data