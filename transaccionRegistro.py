import pymysql 
from claseRegistro import Registro

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
            consulta = "INSERT INTO ASISTENTES (email,nombre,apellido,pase_vier,pase_dosdias,pase_completo,camisa, etiquetas,regalo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(consulta,(registro.email,registro.nombre,registro.apellido,registro.paseV,registro.paseDD,registro.paseC,registro.camisa,registro.etiqueta,registro.regalo))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()    
