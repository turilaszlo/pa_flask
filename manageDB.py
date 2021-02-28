import mysql.connector

def foodDBopen():
    cnx=mysql.connector.connect(host='turi.mysql.pythonanywhere-services.com',
                                user='turi',
                                password='xxxxxxxxxx',
                                database='turi$food')
    return cnx
