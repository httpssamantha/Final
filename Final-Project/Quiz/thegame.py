"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import blackjack
app = Flask(__name__)
import random
import time


global state
state = {'first_card':0,
        'second_card':0,
        'total':0,
        'blackjack': False,
        'player_wins': False,
        'dealer_wins': False,
        'player_total': 0,
        'dealer_total': 0,
        'push': False
}
@app.route('/')
@app.route('/main')
def main():
	return render_template("main.html")
@app.route('/bios')
def team_bios():
	return render_template('bios.HTML')
@app.route('/game')
def game():
	return render_template('blgame.html')
def quiz():
	return render_template('patquiz.html')
@app.route('/start')
def start():
	global state
	return render_template("blgame.html",state=state)

@app.route('/play',methods=['GET','POST'])
def play_hangman():
	global state
	if request.method == 'GET':
		return start()

	elif request.method == 'POST':
		one = request.form['answer1']


	return render_template('blgame.html',state=state)




if __name__ == '__main__':
	app.run('127.0.0.1',port=3000)
