from flask import Flask, render_template, request

app = Flask(__name__)
print("name =", __name__ )

@app.route("/coinflip")


import random

def coin_flip():
    coin = ['heads', 'tails']
    result = str(random.choice(coin))
    return result


def game():
    p1_money = 50
    n = int(input('How many rounds do you want to play?'))
    print('You have $50')
    cpu_money = 50

    for i in range(0, n):
        if i <= n:

            flip = coin_flip()
            bet = int(input('Place your bet:'))
            p1_guess = input('Heads or tails?')
            print('You bet $' + str(bet),'this round')

            if p1_guess == flip:
                p1_money += bet
                cpu_money -= bet
            else:
                cpu_money += bet
                p1_money -= bet
            print('The coin landed on ' +flip,'\n')
            print('You have $'+ str(p1_money) +' left')
            print('The CPU has $'+ str(cpu_money))

            if cpu_money <= 0:
                    print('You win!, CPU has no money.')
                    break
            elif p1_money <= 0:
                    print('You lose. You have no money.')
                    break
            print('--------------')
