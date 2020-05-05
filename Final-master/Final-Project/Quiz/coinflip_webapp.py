from flask import Flask, render_template, request

import random

global state
state = {'player_cash':50,
        'CPU_cash':50,
        'total_bet':0,
        'player_wins': False,
        'CPU_wins': False,
        'flip': False}

@app.route('/toss')
def toss():
    state['result'] = str(random.choice(coin))
    state['heads', 'tails'] == state['result'] 
    return render_template('jk.html', state=state)

@app.route('/coinflip')
def game():
    global state
    state['P1 Money'] = 50
    state['CPU_money'] = 50
    state['rounds'] == int(input('How many rounds do you want to play?'))

    for i in range(0, n):
        if i <= n:
            state['flip'] = toss()
            state['bet'] == int(input('Place your bet:'))
            state['P1_guess'] == input('Heads or tails?')
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
if __name__ == '__main__':
	app.run('127.0.0.1',port=3000)
