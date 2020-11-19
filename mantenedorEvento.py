import pymysql 
from claseEvento import Evento

def conectar():
    try:
        conexion = pymysql.connect(host='localhost',user='root',password='',db='alter_frontistirio')
    except:
        print("Error en la conexión")
    return conexion

def insertar(evento):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO evento (evento_id,nombre_evento,fecha_evento,hora_evento) VALUES (%s,%s,%s,%s);"
            cursor.execute(consulta,(evento.evento_id,evento.nombre_evento,evento.fecha_evento,evento.hora_evento))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()    

def consultar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM evento;") 
            auxEvento = cursor.fetchall()
            for ev in auxEvento:
                print(ev)
        return auxEvento
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("ocurrió un error al insertar ", ex)
    conexion.close()

# # def buscar(auxIdCat):
# #     conexion = conectar()
# #     try:
# #         with conexion.cursor() as cursor:
# #             consulta = "SELECT * FROM categoria_evento WHERE id_categoria = %s;"
# #             cursor.execute(consulta,(auxIdCat))
# #             auxCategoria = cursor.fetchall()
# #             for cat in auxCategoria:
# #                 print(cat)
# #             return auxCategoria
# #     except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
# #         print("ocurrió un error al insertar ", ex)
# #     conexion.close()

def actualizar(evento):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE evento SET nombre_evento = %s, fecha_evento = %s, hora_evento = %s WHERE evento_id = %s;"
            cursor.execute(consulta,(evento.nombre_evento,evento.fecha_evento,evento.hora_evento,evento.evento_id))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("ocurrió un error al actualizar ", ex)
    conexion.close()

def eliminar(idEvento):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM evento WHERE evento_id = %s;"
            cursor.execute(consulta,(idEvento))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("ocurrió un error al actualizar ", ex)
    conexion.close()