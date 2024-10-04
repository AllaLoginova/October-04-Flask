from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, world!<p>"

notes_list = [
    {'id': 1, 'text': 'Заметка 1'},
    {'id': 2, 'text': 'Надо купить хлеб'},
]

@app.route("/notes")
def notes():
    return render_template('notes.html', notes=notes_list)


#  flask --app web_site run => терминал

