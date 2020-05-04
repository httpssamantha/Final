import random
def new_card():
    for x in range(1):
        return random.randint(1,11)
#random.randint(1,11)
def player():
    print("Your Turn")
    total = 0
    blackjack = False
    first_card = new_card()
    second_card = new_card()
    total = first_card + second_card

    print("Cards: " + str(first_card) + "," + str(second_card))
    print("Your Total: " + str(total))
    if total is 21:
        blackjack = True

    while total < 21:
        option = input('Type "Stay" to stay or "Hit" to hit')
        if option == 'Stay' or option == 'stay':
            break
        first_card = new_card()
        print("\nDraw: " + str(first_card))
        total += first_card
        print("Your Total: " + str(total))
    return total, blackjack

def dealer():
    print("\nDealer's Turn")
    total = 0
    first_card = new_card()
    second_card = new_card()
    total = first_card + second_card

    print("Cards: " + str(first_card) + "," + str(second_card))
    print("Dealer's Total: " + str(total))

    while total <=16:
        print("The Dealer is under 16, he has to take another hit!")
        first_card = new_card()
        print("\nDraw: " + str(first_card))
        total += first_card
        print("Dealer's Total: " + str(total))
    return total
def main():

    player_total , blackjack = player()
    player_wins = False
    dealer_wins = False
    push = False
    if blackjack:
        print("You got Black Jack! Congradutlations!")
        player_wins = True
    if player_total > 21:
        print("Bust!")
        dealer_wins = True

    elif player_wins is False or dealer_wins is False:
        dealer_total = dealer()
        if dealer_total > 21:
            print("Bust!")
            player_wins = True
        elif player_total > dealer_total:
            player_wins = True
        elif player_total == dealer_total:
            push = True
        else:
            dealer_wins = True


    if player_wins:
        print("You Win!")
    elif dealer_wins:
        print("You Lose!")
    if push:
        print("Push, its a draw!")
#main()
