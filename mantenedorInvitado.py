import pymysql 
from claseInvitado import Invitado

def conectar():
    try:
        conexion = pymysql.connect(host='localhost',user='root',password='',db='frontistirio')
    except:
        print("Error en la conexión")
    return conexion

def insertar(invitado):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO invitado (nombre_invitado,apellido_invitado,descripcion,url_imagen) VALUES (%s,%s,%s,%s);"
            cursor.execute(consulta,(invitado.nombre_invitado,invitado.apellido_invitado,invitado.descripcion,invitado.url_imagen))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()    

def consultar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM invitado;") 
            auxInvitado = cursor.fetchall()
            for inv in auxInvitado:
                print(inv)
        return auxInvitado
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("ocurrió un error al insertar ", ex)
    conexion.close()

# def buscar(auxIdCat):
#     conexion = conectar()
#     try:
#         with conexion.cursor() as cursor:
#             consulta = "SELECT * FROM categoria_evento WHERE id_categoria = %s;"
#             cursor.execute(consulta,(auxIdCat))
#             auxCategoria = cursor.fetchall()
#             for cat in auxCategoria:
#                 print(cat)
#             return auxCategoria
#     except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
#         print("ocurrió un error al insertar ", ex)
#     conexion.close()

def actualizar(invitado):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE invitado SET nombre_invitado = %s, apellido_invitado = %s, descripcion = %s, url_imagen = %s WHERE id_invitado = %s;"
            cursor.execute(consulta,(invitado.nombre_invitado,invitado.apellido_invitado,invitado.descripcion,invitado.url_imagen,invitado.id_invitado))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("ocurrió un error al actualizar ", ex)
    conexion.close()

def eliminar(auxIdCat):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM invitado WHERE id_invitado = %s;"
            cursor.execute(consulta,(auxIdCat))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("ocurrió un error al actualizar ", ex)
    conexion.close()