from flask import Flask, request, render_template, flash
import pickle


app = Flask(__name__)
app.secret_key = "apkofriowjfkf"

@app.route("/")
def index():
    return render_template('index.html')
    

@app.route("/output",methods=["POST","GET"])

def output():
    if request.method == 'POST':
        p = request.form['pregnancy']
        p = int(p)
        
        g = request.form['glucose']
        g = int(g)
        
        b = request.form['bp']
        b = int(b)
        
        s = request.form['skin']
        s = int(s)
        
        i = request.form['insulin']
        i = int(i)
        
        bmi = request.form['bmi']
        bmi = float(bmi)
        
        db = request.form['pedigree']
        db = float(db)
        
        age = request.form['age']
        age = int(age)


        try:
            prediction = predictor(p,g,b,s,i,bmi,db,age)
            return render_template('output.html',prediction=prediction)

        except ValueError:
            return "Please Enter Valid Values"



def predictor(p,g,b,s,i,bmi,db,age):
    
    #load model
    model = pickle.load(open('model.pkl','rb'))

    #predictions
    result = model.predict([[p,g,b,s,i,bmi,db,age]])

    #output
    if result[0] == 1:
        pred = 'Patient Suffers from Diabetes'
    else:
        pred = 'Patient Is Normal'

    return pred

    

    
    
    
    
    
