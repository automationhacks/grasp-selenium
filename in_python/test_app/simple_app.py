from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def init():
    return render_template('pop_up.html')

if __name__ == '__main__':
    app.run(debug=True)
