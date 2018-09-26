from flask import Flask, render_template, url_for
app = Flask(__name__)

translations = [
    {
        'en_UK': 'Hello',
        'es_ES': 'Holla',
        'status': 'requested'
    },
    {
        'en_UK': 'How you doing?',
        'es_ES': 'Como estas?',
        'status': 'pending'
    },
    {
        'en_UK': 'How',
        'es_ES': 'Como',
        'status': 'translated'
    }
]

@app.route("/")
def index():
    return render_template("index.html", translations=translations)

if __name__ == '__main__':
    app.run(debug=True)