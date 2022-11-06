from flask import Flask, request, render_template, url_for
from flask_restful import Api,resource
import numpy as np
import array

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def index_post():
    dt = float(request.form['dt'])
    t1 = int(request.form['t1'])
    t2 = int(request.form['t2'])
    t = np.arange(t1,t2,dt) 
    f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
    f_clean = f
    f = f + 2.5*np.random.randn(len(t)) 

    n = len(t)
    fhat = np.fft.fft(f,n)
    PSD = fhat * np.conj(fhat)/n
    freq = (1/(dt*n)) * np.arange(n)
    L = np.arange(1,np.floor(n/2),dtype='int')

    indices = PSD > 100
    PSDclean = PSD * indices
    fhat = indices * fhat
    ffilt = np.fft.ifft(fhat)

    data = { 'time': t, 'f': f }

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)