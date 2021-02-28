from manageDB import fdcDBopen

def fdcSelector(Kcal,item,cvit,minmaxKcal,minmaxCvit):


    idList=[]
    foodList=[]
    caloriesList=[]
    cvitList=[]
    sugarList=[]

    cnx=fdcDBopen()
    cursor=cnx.cursor()

#the views should exist
    '''
    viewKcal= """CREATE OR REPLACE VIEW kcal
        AS SELECT
        food_nutrient_filtered2.fdc_id,
        food_nutrient_filtered2.description AS 'Food',
        food_nutrient_filtered2.amount AS 'Kcal'
        FROM food_nutrient_filtered2
        INNER JOIN nutrient ON nutrient.id=food_nutrient_filtered2.nutrient_id
        WHERE food_nutrient_filtered2.nutrient_id=1008"""


    viewCvit= """CREATE OR REPLACE
        VIEW cvit AS
        SELECT kcal.*,
        food_nutrient_filtered2.amount AS 'Cvit'
        FROM kcal
        LEFT JOIN food_nutrient_filtered2
        USING (fdc_id)
        WHERE food_nutrient_filtered2.nutrient_id=1162"""

    viewSugar="""CREATE OR REPLACE
        VIEW sugar AS
        SELECT
        cvit.fdc_id,
        cvit.Food,
        FORMAT (cvit.Kcal,0) AS 'Kcal',
        FORMAT (cvit.Cvit,1) AS 'Cvit',
        FORMAT (food_nutrient_filtered2.amount,2) AS 'Sugar'
        FROM cvit
        LEFT JOIN food_nutrient_filtered2
        USING (fdc_id)
        WHERE food_nutrient_filtered2.nutrient_id=2000"""
    '''
    q1="SELECT * FROM sugar WHERE Kcal"
    q1b="SELECT COUNT(*) FROM sugar WHERE Kcal"
    if str(minmaxKcal)=="min":
        q2=">"
    else:
        q2="<"
    q3=str(Kcal)
    q4=" AND Cvit"
    if str(minmaxCvit)=="min":
        q5=">"
    else:
        q5="<"
    q6=str(cvit)
    q7=" ORDER BY RAND() LIMIT "
    q8=str(item)

    queryCount=q1b+q2+q3+q4+q5+q6
    queryShow=q1+q2+q3+q4+q5+q6+q7+q8


#only needed if the views do not exist
    #cursor.execute(viewKcal)
    #cursor.execute(viewCvit)
    #cursor.execute(viewSugar)
############
    cursor.execute(queryCount)
    rows=cursor.fetchone()
    cursor.execute(queryShow)


    for (fdc_id,Food, Kcal,Cvit,Sugar) in cursor:
        idList.append(fdc_id)
        foodList.append(Food)
        caloriesList.append(Kcal)
        cvitList.append(Cvit)
        sugarList.append(Sugar)


    cursor.close()
    cnx.close()

    tableDict={'IDs':idList,
            'Foods':foodList,
            'Cals':caloriesList,
            'Cvit':cvitList,
            'Sugar':sugarList,
            'rowNo':rows[0]}

    return tableDict

#only for testing
fdcDict=fdcSelector(200,6,200,"maxKcal","minCvit")
print("IDs: ",fdcDict['IDs'])
print("Foods: ",fdcDict['Foods'])
print("Cals: ",fdcDict['Cals'])
print("Cvit: ",fdcDict['Cvit'])
print("sugar: ",fdcDict['Sugar'])
print("ROWS: ", fdcDict['rowNo'])
