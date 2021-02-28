import mysql.connector

def foodDBopen():
    cnx=mysql.connector.connect(host='turi.mysql.pythonanywhere-services.com',
                                user='turi',
                                password='Zita1324.',
                                database='turi$food')
    return cnx

def fdcDBopen():
    cnx=mysql.connector.connect(host='turi.mysql.pythonanywhere-services.com',
                                user='turi',
                                password='Zita1324.',
                                database='turi$fdc')
    return cnx