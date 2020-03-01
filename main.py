from flask import Flask,render_template,request
import os


@app.route('/')
def home():
	print("Hello")

if __name__ == '__main__':
    app.run()
