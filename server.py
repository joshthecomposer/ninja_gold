from flask import Flask, render_template, redirect, session, request
import datetime
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'log' not in session and 'goal' not in session:
        session['log'] = [f'<p class="text-black">Game started at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>']
        session['goal'] = 500
        session['tries'] = 0
        session['loss'] = 20
        session['gold'] = 0
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    arg1 = int(request.form.get('input_one'))
    arg2 = int(request.form.get('input_two'))
    random_number = random.randint(arg1, arg2)
    print(arg1, arg2)
    print(random_number)
    session['gold'] += random_number
    if random_number < 0:
        session['log'].insert(0, f'<p class="text-danger">Took away {random_number} gold at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>')
    else: 
        session['log'].insert(0, f'<p class="text-success">Added {random_number} gold at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>')
    session['tries'] += 1
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)