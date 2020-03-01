from flask import Flask,render_template,request

application = app = Flask(__name__)

@app.route('/')
def home():
	print("hello")
  

if __name__ == '__main__':
   app.run()
