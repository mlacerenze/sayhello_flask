from flask import Flask, render_template, request, flash 

app = Flask(__name__)
app.secret_key = 'mysecretkeykeysecretmy'

@app.route('/')
def hello():
  flash("What's your name?")
  return render_template('index.html')

@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
  flash(str(request.form['name_input']))
  return render_template('welcome.html')

if __name__ == '__main__':
  app.run(debug=True)