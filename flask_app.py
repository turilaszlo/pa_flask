from flask import Flask, render_template
from foods import foodSelector

app = Flask(__name__,
            static_url_path='',
            static_folder='bootstrap/',
            template_folder='templates/')

@app.route('/')
def home():
    return render_template('home.html')

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


app.config["DEBUG"] = True
