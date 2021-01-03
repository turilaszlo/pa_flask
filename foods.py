from manageDB import foodDBopen

def foodSelector(itemNo,calMax,cvitMin):

    totalCvit=0
    totalCalories=0
    FoodList=[]
    SizeList=[]
    CaloriesList=[]
    CvitList=[]

    cnx=foodDBopen()
    cursor=cnx.cursor()

    selectFood="CREATE OR REPLACE VIEW healthyView (Food, Size, Calories, Cvit) AS SELECT Food, ServingSize, Calories, VitC FROM foods WHERE VitC >"+str(cvitMin)+" AND Calories <"+str(calMax)+" ORDER BY RAND() LIMIT "+str(itemNo)
    cursor.execute(selectFood)
    allHealthy="SELECT Food, Size, Calories, Cvit FROM healthyView"
    cursor.execute(allHealthy)

    for (Food, Size, Calories, Cvit) in cursor:
        FoodList.append(Food)
        SizeList.append(Size)
        CaloriesList.append(Calories)
        totalCalories=totalCalories+Calories
        CvitList.append(Cvit)
        totalCvit=totalCvit+Cvit

    cursor.close()
    cnx.close()

    tableDict={'Foods':FoodList,
            'Sizes':SizeList,
            'Cals':CaloriesList,
            'Cvits':CvitList,
            'totCals':totalCalories,
            'totCvits':totalCvit}

    return tableDict



# EZ CSAK AZ INTERAKTIV VERZIOHOZ KELL
#itemNo=input("hany tetelbol all a menu? ")
#calNo=input("egy tetel MAX hany kaloria? ")
#cvitNo=input("egy tetel MIN hany c-vitamin?: ")
#requestedCvit=input("osszesen mennyi c-vitamin a menuben? ")
#
#runX=1
#foodDict=foodSelector(itemNo,calMax,cvitMin)
#
#while True:
#    foodDict.get("totCvits")<int(requestedCvit)
#    runX=runX+1
#    foodDict=foodSelector(itemNo,calMax,cvitMin)
#    print("runX: " + str(runX)+ "// totalCvit: " + str(foodDict.get("totCvits")))
#    if foodDict.get("totCvits")>=int(requestedCvit):
#        print("::::::::::::")
#        print("megvan: ",foodDict)
#        break
