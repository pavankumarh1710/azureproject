from flask import Flask,render_template,request
import sqlite3 as sql
import pandas as pd
import numpy as np
application = app = Flask(__name__)
import os
import time
import redis
import pickle as pickle
import random
from sklearn.cluster import KMeans
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import pyplot as mpld3
from sklearn.cluster import KMeans
from scipy.spatial import distance

con = sql.connect("database.db")
rd = redis.StrictRedis(host='shakthi8112.redis.cache.windows.net', port=6380, db=0,password='ncP8NFImWyXmxKjo1MOVoAmJg7KRFX7511MbiSFHR9k=',ssl=True)

@app.route('/')
def home():
	return render_template('home.html')
  




if __name__ == '__main__':
   app.run()
