#!/usr/bin/env python
# coding: Utf-8

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():

    # dictionnaire de données
    data = {'user': 'yliès', 'machine': 'MacBook'}

    # affichage du template
    return render_template('index.html', title='Home page', data=data)


if __name__ == '__main__':
    app.run()
