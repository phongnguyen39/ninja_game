from flask import Flask, render_template, redirect, request, session
import random
import datetime
app = Flask(__name__)
app.secret_key='secret_key'

#HomePage
@app.route('/')
def index():
    session['total_gold'] = 0
    session['progress_notes'] = "Ready to play?"
    return render_template('index.html')

#get totals from session score
@app.route('/game_inplay', methods=['post'])
def game_inplay():

    session['input'] = request.form['input']
    if 'farm' in session['input']:
        gold = round(random.random()*20+10)

    if 'cave' in session['input']:
        gold = round(random.random()*10+5)

    if 'estate' in session['input']:
        gold = round(random.random()*5+2)
    
    if 'casino' in session['input']:
        gold = round(random.random()*100-50)
     
#Session data passed to HTML
    date_time = datetime.datetime.now()
    date_time = date_time.strftime("%m/%d %I:%M")
    industry = session['input']
    session['total_gold'] += gold
    # gold = session['total_gold']
    
    print('*'*20,session.items())

#Progress notes
    session['progress_notes'] += f'<br>{date_time} - GOLD: {gold} - {industry}<br>'     
    return redirect('/game_play')

#Redirecting
@app.route('/game_play')
def gameplay():
    return render_template('game_inplay.html', total_gold = session['total_gold'], progress_notes = session['progress_notes']
    )

#Clear Session
@app.route('/reset', methods=['post'])
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)
