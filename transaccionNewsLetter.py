import pymysql 
from claseNewsLetter import NewsLetter

def conectar():
    try:
        conexion = pymysql.connect(host='localhost',user='root',password='',db='alter_frontistirio')
    except:
        print("Error en la conexión")
    return conexion

def insertar(registro):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO NEWSLETTER(email,nombre,apellido,telefono,estado) VALUES (%s,%s,%s,%s,TRUE);"
            cursor.execute(consulta,(registro.email,registro.nombre,registro.apellido,registro.fono))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()    

def updateFalse(email):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE NEWSLETTER SET ESTADO = FALSE WHERE EMAIL = %s;"
            cursor.execute(consulta,(email))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()   

def updateTrue(email):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE NEWSLETTER SET ESTADO = TRUE WHERE EMAIL = %s;"
            cursor.execute(consulta,(email))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()   