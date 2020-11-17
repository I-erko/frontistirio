import pymysql 
from claseCategoria import Categoria

def conectar():
    try:
        conexion = pymysql.connect(host='localhost',user='root',password='',db='frontistiriodb')
    except:
        print("Error en la conexión")
    return conexion

def insertar(categoria):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO categoria_evento (cat_evento,icono) VALUES (%s,%s);"
            cursor.execute(consulta,(categoria.cat_evento, categoria.icono))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()    

def consultar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM categoria_evento;") 
            auxCategoria = cursor.fetchall()
            for cat in auxCategoria:
                print(cat)
        return auxCategoria
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("ocurrió un error al insertar ", ex)
    conexion.close()

def buscar(auxIdCat):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM categoria_evento WHERE id_categoria = %s;"
            cursor.execute(consulta,(auxIdCat))
            auxCategoria = cursor.fetchall()
            for cat in auxCategoria:
                print(cat)
            return auxCategoria
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("ocurrió un error al insertar ", ex)
    conexion.close()

def actualizar(categoria):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE categoria_evento SET cat_evento = %s,icono = %s WHERE id_categoria = %s;"
            cursor.execute(consulta,(categoria.cat_evento,categoria.icono,categoria.id_cat))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("ocurrió un error al actualizar ", ex)
    conexion.close()

def eliminar(auxIdCat):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM categoria_evento WHERE id_categoria = %s;"
            cursor.execute(consulta,(auxIdCat))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("ocurrió un error al actualizar ", ex)
    conexion.close()