from flask import Flask, url_for
from flask import render_template
from flask import request
import sqlite3

# virtualenv env # создание вирт. окружение

# source env/bin/activate

# pip install Flask

app = Flask(__name__)

@app.route('/')
def index():
    rules = """ Тут был большой текст
    """

    return render_template('index.html', appname = "Hello! This is index page", content = rules )
# return '<html><body><h1>Hello! This is index page</h1></body></html>'

# @app.route('/command/<id>')
def command(id):
    return f'running command with {id}'

app.add_url_rule('/command/<id>', 'command', command)
    
# /add/message" id="newmessageform" method="POST" ->

# > @app.route('/add/<type>', methods=['POST'])
@app.route('/add/message', methods=['POST'])
def add_message():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    print(request.form['username'])
    print(request.form['msgtxt'])
    cur.execute('INSERT INTO messages VALUES ("{}", "{}")'.format(
                                                            request.form['username'],
                                                            request.form['msgtxt']
                                                                                   ))
    connection.commit()
    connection.close()

    return 'adding message'

#@app.route('/add/user/<username>', methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run()

