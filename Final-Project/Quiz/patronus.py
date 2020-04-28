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
		'first_card':0,
		'second_card':0,
		'total':0,
		'blackjack': False,
		'player_wins': False,
		'dealer_wins': False,
		'player_total': 0,
		'dealer_total': 0,
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
@app.route('/game')
def game():
	global state
	state['first_card'] ==  0
	state['second_card'] == 0
	state['total'] == 0
	state['blackjack'] == False
	state['player_wins'] == False
	state['dealer_wins'] == False
	state['player_total'] == 0
	state['dealer_total'] == 0
	state['push'] == False
	state['first_card'] = random.randint(1,11)
	state['second_card'] = random.randint(1,11)
	print(state)
	state['total'] = state['first_card']+state['second_card']
	return render_template("blgame.html", state=state)

@app.route('/wager', methods=['GET','POST'])
def wager():
	global state
	if request.method == 'GET':
		return begin()
	elif request.method == 'POST':
		verdict = request.form['stayorhit']
		if verdict == "stay" or verdict == "Stay":
			print("stay")
		if verdict == "hit" or verdict == "Hit":
			print("hit")
		print("hello")
		while state['total'] < 21:
			return render_template("blgame.html", state=state)
		if state['total'] == 21:
			print("congrats")
			print(state)
		return render_template("patquiz.html", state=state)


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
		print("Your patronus is a Stag")
		print("Traditionally seen as ‘King of the Forest’, the stag is the protector of the other animals.")
	elif state['opoints']>state['spoints'] and state['opoints']>state['jrpoints'] and state['opoints']>state['hpoints']:
		print("Your patronus is an Otter")
		print("An otter represents 'that which is hidden, unknown but necessary within the personality.'")
	elif state['jrpoints']>state['spoints'] and state['jrpoints']>state['spoints'] and state['jrpoints']>state['hpoints']:
		print("Your patronus is a Jack Russel Terrier")
		print("Jack Russels represent loyalty and blind fearlessness.")
	elif state['hpoints']>state['spoints'] and state['hpoints']>state['jrpoints'] and state['hpoints']>state['spoints']:
		print("Your patronus is a Hare")
		print("Hares represent being carefree and thoughts beyond imagination.")
	else:
		print("You are not ready to have a Patronus now. Thank you for taking the time to go on this journey.")



	return render_template('patresults.html',state=state)




if __name__ == '__main__':
	app.run('127.0.0.1',port=3000)
