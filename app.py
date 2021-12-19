from flask import Flask, request, render_template, flash
import pickle


app = Flask(__name__)
app.secret_key = "apkofriowjfkf"

@app.route("/home")
def index():
    return render_template("index.html")
    

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

        #load model
        model = pickle.load(open('model.pkl','rb'))
        
        #predictions
        result = model.predict([[p,g,b,s,i,bmi,db,age]])

        #output
        if result[0] == 1:
            flash("Patient Suffers from Diabetes")
        else:
            flash("Patient Is Normal")

        return render_template("index.html")
    
    
    
