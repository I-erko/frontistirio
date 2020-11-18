import pymysql 
from claseAdmin import Admin

def conectar():
    try:
        conexion = pymysql.connect(host='localhost',user='root',password='',db='frontistiriodb')
    except:
        print("Error en la conexión")
    return conexion

def insertar(admin):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO admin (usuario,nombre,password) VALUES (%s,%s,%s);"
            cursor.execute(consulta,(admin.usuario, admin.nombre, admin.password))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()    

def consultar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM admin;") 
            auxAdmin = cursor.fetchall()
            for adm in auxAdmin:
                print(adm)
        return auxAdmin
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

def actualizar(admin):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE admin SET usuario = %s, nombre = %s, password = %s  WHERE id_admin = %s;"
            cursor.execute(consulta,(admin.usuario,admin.nombre,admin.password,admin.id_admin))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("ocurrió un error al actualizar ", ex)
    conexion.close()

# def eliminar(auxIdCat):
#     conexion = conectar()
#     try:
#         with conexion.cursor() as cursor:
#             consulta = "DELETE FROM categoria_evento WHERE id_categoria = %s;"
#             cursor.execute(consulta,(auxIdCat))
#         conexion.commit()
#     except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
#         print("ocurrió un error al actualizar ", ex)
#     conexion.close()