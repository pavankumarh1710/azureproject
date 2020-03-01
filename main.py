from flask import Flask,render_template,request
import os

application = app = Flask(__name__)

@app.route('/')
def home():
	print("hello")
  

if __name__ == '__main__':
   app.run()
