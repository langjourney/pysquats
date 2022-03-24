num_cards = 8
total_squats = []

for card in range(num_cards):
    card_num = card + 1
    if card_num == 1:
        total_squats.append(num_cards)
        total_squats.append(card_num)
    else:
        total_squats.append((card_num * 2) - 1)

total_squats = sum(total_squats)
print(total_squats)
