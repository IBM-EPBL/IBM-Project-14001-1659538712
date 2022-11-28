from flask import Flask, render_template
from flask import request
from predictor import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        if request.method == 'POST':
            l=[]
            l.append(float(request.form['id']))
            l.append(float(request.form['cycle']))
            l.append(float(request.form['set1']))
            l.append(float(request.form['set2']))
            l.append(float(request.form['set3']))
            l.append(float(request.form['s1']))
            l.append(float(request.form['s2']))
            l.append(float(request.form['s3']))
            l.append(float(request.form['s4']))
            l.append(float(request.form['s5']))
            l.append(float(request.form['s6']))
            l.append(float(request.form['s7']))
            l.append(float(request.form['s8']))
            l.append(float(request.form['s9']))
            l.append(float(request.form['s10']))
            l.append(float(request.form['s11']))
            l.append(float(request.form['s12']))
            l.append(float(request.form['s13']))
            l.append(float(request.form['s14']))
            l.append(float(request.form['s15']))
            l.append(float(request.form['s16']))
            l.append(float(request.form['s17']))
            l.append(float(request.form['s18']))
            l.append(float(request.form['s19']))
            l.append(float(request.form['s20']))
            l.append(float(request.form['s21']))
            print(l)
            if predict(l):
                return render_template('result.html',data="problem")
            else:
                return render_template('result.html',data="normal")
    except:
        return render_template('result.html',data="error")