def payoff(self):
        strategy1 = self.player1.played_strategy
        strategy2 = self.player2.played_strategy
        if self.player1.played_strategy not in self.player1.strategies:
            raise ValueError("Invalid strategy")
        elif self.player2.played_strategy not in self.player2.strategies:
            raise ValueError("Invalid strategy")
        elif self.player1.played_strategy > self.player2.played_strategy:
            result = ((20 - self.player1.played_strategy), (-self.player2.played_strategy))
            return result
        elif self.player1.played_strategy < self.player2.played_strategy:
            result = ((-self.player1.played_strategy), (20 - self.player2.played_strategy))
            return result
        elif self.player1.played_strategy == self.player2.played_strategy:
            result = ((10 - self.player1.played_strategy), (10 - self.player2.played_strategy))
            return result
        else:
            return "Error"
        
def payoff(player1, player2):
    if player1 not in range(0,11):
        raise ValueError("Invalid strategy")
    elif player2 not in range(0,11):
        raise ValueError("Invalid strategy")
    elif player1 > player2:
        result = ((20 - player1), (-player2))
        return result
    elif player1 < player2:
        result = ((-player1), (20 - player2))
        return result
    elif player1 == player2:
        result = ((20/2) - player1, (20/2) - player2)
        return result
    else:
        return "Error"
    
payoff(5,10)