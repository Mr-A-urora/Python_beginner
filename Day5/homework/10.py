# 扑克游戏连续发牌， 5个人，每人3张

deck = [f"{rank}{suit}" for suit in ['♠', '♥', '♦', '♣'] for rank in
        ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
num_players = 5
num_cards_per_player = 3
hands = {f"玩家{i+1}": [] for i in range(num_players)}

for round in range(num_cards_per_player):
    for player in hands:
        card = deck.pop(0)
        hands[player].append(card)

for player, cards in hands.items():
    print(f"{player} 的牌: {', '.join(cards)}")