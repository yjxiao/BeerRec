# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import os, csv
import pandas as pd

app = Flask(__name__)
app.config.update(dict(DEBUG=True))
DATAFILE = os.path.join(os.path.dirname(__file__), 'static/data/beers_for_rec.csv')

@app.route('/')
def home():
    beers = []
    with open(DATAFILE, 'rb') as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            beers.append(row[0].decode('utf8'))
    beers.sort()
    return render_template('index.html', beers=beers)

@app.route('/<beername>')
def beer_rec(beername):
    beers = pd.read_csv(DATAFILE, index_col='beerName')
    cluster = beers[beers.index == beername.encode('utf8')].cluster[0]
    recommendation = beers[beers.cluster == cluster].sort(columns = 'reviewOverall', ascending = False)
    recommendation = recommendation.drop(beername.encode('utf8'))[['beerStyle', 'beerABV']][:5]
    recommendation['beerName'] = recommendation.index
    recommendation.beerName = recommendation.beerName.apply(lambda x: x.decode('utf8'))
    return render_template('beer.html', beer=beername, recommends=recommendation.to_dict(orient='record'))

if __name__ == '__main__':
    app.run()
