from flask import Flask,render_template,request
application = app = Flask(__name__)
import os


@app.route('/')
def home():
	return render_template('home.html')
  



if __name__ == '__main__':
   app.run()
