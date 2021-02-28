from flask import Flask, render_template, request, redirect, url_for
from foods import foodSelector
from fdc import fdcSelector

app = Flask(__name__,
            static_url_path='',
            static_folder='bootstrap/',
            template_folder='templates/')



@app.route('/lturi')
def home():
    return render_template('home.html')

@app.route('/')
def ideateka():
    return render_template('ideateka.html')

@app.route('/food')
def food():
    itemNo=5
    calMax=1000
    cvitMin=50
    requestedCvit=3000

    foodDict=foodSelector(itemNo,calMax,cvitMin)

    runX=0
    foodDict=foodSelector(itemNo,calMax,cvitMin)

    while True:
        foodDict.get("totCvits")<requestedCvit
        runX=runX+1
        foodDict=foodSelector(itemNo,calMax,cvitMin)
        #return render_template('food-wait.html',runX=str(runX))
        if foodDict.get("totCvits")>=(requestedCvit):
            return render_template('food.html',foodDict=foodDict,itemNo=itemNo,runX=str(runX))

@app.route('/fdc/<int:itemNo>/<int:Kcal>/<int:cvit>/<minmaxKcal>/<minmaxCvit>')
def fdc(itemNo,Kcal,cvit,minmaxKcal,minmaxCvit):
    return render_template('fdc.html',fdcDict=fdcSelector(Kcal,itemNo,cvit,minmaxKcal,minmaxCvit),itemNo=itemNo,Kcal=Kcal,cvit=cvit,minmaxKcal=minmaxKcal,minmaxCvit=minmaxCvit)

@app.route('/fdc_in',methods=['GET','POST'])
def fdc_in():
    if request.method == 'POST':
        item=request.form['itemInput']
        Kcal=request.form['KcalInput']
        minmaxKcal=request.form['minmaxKcalInput']
        cvit=request.form['cvitInput']
        minmaxCvit=request.form['minmaxCvitInput']
        return redirect(url_for('fdc',Kcal=Kcal,itemNo=item,cvit=cvit,minmaxKcal=minmaxKcal,minmaxCvit=minmaxCvit))

    return render_template('fdc_in.html')

app.config["DEBUG"] = True
