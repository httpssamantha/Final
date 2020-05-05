"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import thequiz
app = Flask(__name__)
import copy
import time
import random


global state
state = {'spoints': 0,
		'opoints': 0,
		'jrpoints': 0,
		'hpoints':0,
		'pfirst_card':0,
		'psecond_card':0,
		'pthird_card':0,
		'pfourth_card':0,
		'pfifth_card':0,
		'dfirst_card':0,
		'dsecond_card':0,
		'dthird_card':0,
		'dfourth_card':0,
		'dfifth_card':0,
		'total':0,
		'total2':0,
		'total3':0,
		'total4':0,
		'blackjack': False,
		'player_wins': False,
		'dealer_wins': False,
		'player_total': 0,
		'dealer_total': 0,
		'dealer_total2':0,
		'dealer_total3':0,
		'push': False}

@app.route('/')
@app.route('/main')
def main():
	return render_template("main.html")
@app.route('/about')
def about():
	return render_template("about.html")
@app.route('/bios')
def team_bios():
	return render_template('bios.HTML')
@app.route('/quiz')
def quiz():
	return render_template('patquiz.html')
@app.route('/dealer')
def dealer():
	return render_template('dealerh.html')

@app.route('/game')
def play_blackjack():
	global state
	state['pfirst_card'] ==  0
	state['psecond_card'] == 0
	state['total'] == 0
	state['blackjack'] == False
	state['player_wins'] == False
	state['dealer_wins'] == False
	state['player_total'] == 0
	state['push'] == False
	state['pfirst_card'] = random.randint(1,11)
	state['psecond_card'] = random.randint(1,10)
	state['total'] = state['pfirst_card']+state['psecond_card']
	state['player_total'] = state['total']
	if state['total'] < 21:
		state['pthird_card'] = random.randint(1,11)
		state['total2']=state['total'] + state['pthird_card']
		state['player_total'] = state['total2']
	if state['total2'] < 21:
		state['pfourth_card'] = random.randint(1,11)
		state['total3']=state['total2'] + state['pfourth_card']
		state['player_total'] = state['total3']
	if state['total2'] >21:
		state['player_total'] = state['total']
	if state['total3'] < 21:
		state['pfifth_card'] = random.randint(1,11)
		state['total4']=state['total3'] + state['pfifth_card']
		state['player_total'] = state['total4']
	if state['total3'] >21:
		state['player_total'] = state['total2']
	if state['total4'] < 21:
		return render_template('blgame.html', state=state)
	if state['total4'] >21:
		state['player_total'] = state['total3']

	return render_template('blgame.html', state=state)


@app.route('/wager',methods=['GET','POST'])
def wager():
	global state
	if request.method == 'GET':
		return play_blackjack()
	elif request.method == 'POST':
		return first()
@app.route('/first')
def first():
	global state
	state['dfirst_card'] = 0
	state['dsecond_card'] = 0
	state['dthird_card'] = 0
	state['dfourth_card'] = 0
	state['dfifth_card'] = 0
	state['dealer_total'] = 0
	state['dfirst_card'] = random.randint(1,11)
	state['dsecond_card'] = random.randint(1,10)
	state['dealer_total'] = state['dfirst_card']+state['dsecond_card']
	state['dealer_total2']=0
	state['dealer_total3'] = 0
	if state['dealer_total'] <= 16:
		state['dthird_card'] = random.randint(1,11)
		state['dealer_total']=state['dealer_total'] + state['dthird_card']
	if state['dealer_total'] <= 16:
		state['dfourth_card'] = random.randint(1,11)
		state['dealer_total']=state['dealer_total'] + state['dfourth_card']
	if state['dealer_total'] <= 16:
		state['dfifth_card'] = random.randint(1,11)
		state['dealer_total']=state['dealer_total'] + state['dfifth_card']
	if state['dealer_total']>=16:
		return render_template('dealerh.html', state=state)
	return render_template('dealerh.html', state=state)

@app.route('/second',methods=['GET','POST'])
def second():
	global state
	if request.method == 'GET':
		return first()
	elif request.method == 'POST':
		return play_blackjack()

@app.route('/lose',methods=['GET','POST'])
def lose():
	global state
	if request.method == 'POST':
		return render_template('LosePage.html', state=state)

@app.route('/start')
def start():
	global state
	state['spoints'] == 0
	state['opoints'] == 0
	state['jrpoints'] == 0
	state['hpoints'] == 0
	return render_template("patquiz.html",state=state)

@app.route('/play',methods=['GET','POST'])
def play_hangman():
	global state
	if request.method == 'GET':
		return start()


	elif request.method == 'POST':
		one = request.form['answer1']
		two = request.form['answer2']
		three = request.form['answer3']
		four = request.form['answer4']
		five = request.form['answer5']
		six = request.form['answer6']
	if one == "black":
		state['hpoints'] +=1
		state['opoints'] +=1
	if one == "white":
		state['jrpoints'] += 1
		state['spoints'] += 1
	print(state)
	if two == "leader":
		state['spoints'] += 1
	if two == "hardworker":
		state['opoints'] +=1
	if two == "fearless":
		state['jrpoints'] += 1
	if two == "unique":
		state['hpoints'] += 1
	print(state)
	if three == "aaa":
		state['spoints'] += 1
	if three == "bbb":
		state['hpoints'] += 1
	if three == "ccc":
		state['jrpoints'] += 1
	if three == "ddd":
		state['opoints'] += 1
	print(state)
	if four == "stream":
		state['opoints'] += 1
	if four == "hut":
		state['hpoints'] += 1
	if four == "mount":
		state['jrpoints'] += 1
	if four == "path":
		state['spoints'] += 1
	print(state)
	if five == "defense":
		state['spoints'] +=1
	if five == "herb":
		state['hpoints'] += 1
	if five == "quid":
		state['jrpoints'] += 1
	if five == "divin":
		state['opoints'] += 1
	print(state)
	if six == "disc":
		state['opoints'] += 1
	if six == "protec":
		state['spoints'] += 1
	if six == "create":
		state['hpoints'] += 1
	if six == "achi":
		state['jrpoints'] += 1
	print(state)
	if state['spoints']>state['opoints'] and state['spoints']>state['jrpoints'] and state['spoints']>state['hpoints']:
		return render_template('patsstag.html',state=state)
	elif state['opoints']>state['spoints'] and state['opoints']>state['jrpoints'] and state['opoints']>state['hpoints']:
		return render_template('patotter.html', state=state)
	elif state['jrpoints']>state['spoints'] and state['jrpoints']>state['spoints'] and state['jrpoints']>state['hpoints']:
		return render_template('patjack.html', state=state)
	elif state['hpoints']>state['spoints'] and state['hpoints']>state['jrpoints'] and state['hpoints']>state['spoints']:
		return render_template('pathare.html', state=state)
	else:
		print("You are not ready to have a Patronus now. Thank you for taking the time to go on this journey.")



	return render_template('patresults.html',state=state)


import random

global state
state = {'player_cash':50,
        'CPU_cash':50,
        'total_bet':0,
        'player_wins': False,
        'CPU_wins': False,
        'flip': False}

@app.route('/coinflip')

def toss():
    coin = ['heads', 'tails']
    result = str(random.choice(coin))
    return result
   
def game():
    global state
    state['P1 Money'] = 50
    state['CPU_money'] = 50
    state['rounds'] == int(input('How many rounds do you want to play?'))

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

	
	if __name__ == '__main__':
	app.run('127.0.0.1',port=3000)

