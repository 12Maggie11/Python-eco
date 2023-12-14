player1 = input("Player 1 請輸入數字 0~10: ")
player2 = input("Player 2 請輸入數字 0~10: ")
player1=int(player1)
player2=int(player2)

if player1 and player2 not in range(0,11):
    print("請輸入數字 0~10")
elif player1 == player2:
    result = ((20/2) - player1, (20/2) - player2)
    print("In a tie,", "payoff equals", result)
elif player1 > player2:
    result = ((20 - player1), (-player2))
    print("Player 1 WIN,", "payoff equals", result)
elif player1 < player2:
    result = ((-player1), (20 - player2))
    print("Player 2 WIN,", "payoff equals", result)
else:
    print("請輸入數字 0~10")

