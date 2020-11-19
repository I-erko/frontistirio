import mantenedorCategoria
import mantenedorEvento
import mantenedorInvitado
import mantenedorAdmin
import claseCategoria
import claseEvento
import claseInvitado
import claseAdmin
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# ////////////////// MAIN ROUTES //////////////////


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registro")
def registro():
    return render_template("registro.html")


@app.route("/invitados")
def invitados():
    return render_template("invitados.html")


@app.route("/conferencia")
def conferencia():
    return render_template("conferencia.html")


@app.route("/calendario")
def calendario():
    return render_template("calendario.html")


# ////////////////// ADMINISTRATOR ROUTES //////////////////

# LOGIN
@app.route("/login")
def login():
    return render_template("login.html")


# EVENTO
# region


@app.route("/listaEvento")
def listaEvento():
    datos = mantenedorEvento.consultar()
    return render_template("lista-evento.html", eventos=datos)


@app.route("/crearEvento")
def crearEvento():
    return render_template("crear-evento.html")


@app.route("/editarEvento/<int:idEvento>/<string:nombreEv>/<string:fechaEv>/<string:horaEv>")
def editarEvento(idEvento,nombreEv,fechaEv,horaEv):
    return render_template("editar-evento.html", idEv=idEvento, nameEvento=nombreEv, fecEvento=fechaEv, horaEvento=horaEv)


# endregion

# CATEGORÍA
# region


@app.route("/listaCategoria")
def listaCategoria():
    datos = mantenedorCategoria.consultar()
    return render_template("lista-categoria.html", categorias=datos)


@app.route("/crearCategoria")
def crearCategoria():
    return render_template("crear-categoria.html")


@app.route("/editarCategoria/<int:id_cat>/<string:nombre>/<string:icono>")
def editarCategoria(id_cat, nombre, icono):
    return render_template(
        "editar-categoria.html", idCat=id_cat, nombreCat=nombre, iconoCat=icono
    )


# endregion

# INVITADO
# region


@app.route("/listaInvitado")
def listaInvitado():
    datos = mantenedorInvitado.consultar()
    return render_template("lista-invitado.html", invitados=datos)


@app.route("/crearInvitado")
def crearInvitado():
    return render_template("crear-invitado.html")


@app.route(
    "/editarInvitado/<int:id_Inv>/<string:name_Inv>/<string:ape_Inv>/<string:desc_Inv>/<string:url_Img>"
)
def editarInvitado(id_Inv, name_Inv, ape_Inv, desc_Inv, url_Img):
    return render_template(
        "editar-invitado.html",
        idInv=id_Inv,
        nameInv=name_Inv,
        apeInv=ape_Inv,
        descInv=desc_Inv,
        urlImg=url_Img,
    )


# endregion

# ADMIN
# region


@app.route("/listaAdmin")
def listaAdmin():
    datos = mantenedorAdmin.consultar()
    return render_template("lista-admin.html", administradores=datos)


@app.route("/crearAdmin")
def crearAdmin():
    return render_template("crear-admin.html")


@app.route(
    "/editarAdmin/<int:idAdmin>/<string:userAdmin>/<string:nameAdmin>/<string:passAdmin>"
)
def editarAdmin(idAdmin, userAdmin, nameAdmin, passAdmin):
    return render_template(
        "editar-admin.html",
        id_admin=idAdmin,
        user_admin=userAdmin,
        name_admin=nameAdmin,
        pass_admin=passAdmin
    )


# endregion

# ////////////////// MAINTENANCE ROUTES //////////////////

# --------CATEGORY MAINTAINER
# region
# INSERTAR
@app.route("/insertar_categoria", methods=["POST"])
def insertar_categoria():
    if request.method == "POST":
        try:
            auxBotonInsertar = request.form["btoInsertar"]
            if auxBotonInsertar == "Insertar":
                auxIdCat = ""
                auxNombreCategoria = request.form["txtCategoria"]
                auxIcono = request.form["txticono"]
                auxCategoria = claseCategoria.Categoria(
                    auxIdCat, auxNombreCategoria, auxIcono
                )
                mantenedorCategoria.insertar(auxCategoria)
                print("datos guardados")
                # flash('datos guardados')
        except:
            print("datos No guardados")
        return redirect(url_for("listaCategoria"))


# ELIMINAR
@app.route("/eliminar_categoria/<int:id_cat>")
def eliminar_categoria(id_cat):
    if request.method == "GET":
        try:
            mantenedorCategoria.eliminar(id_cat)
            print("datos Eliminados")
            # flash('datos Eliminados')
        except:
            print("datos No Eliminados")
            # flash('datos No Eliminados')
        return redirect(url_for("listaCategoria"))


# ACTUALIZAR
@app.route("/actualizar_categoria/<int:id_cat>", methods=["POST"])
def actualizar_categoria(id_cat):
    if request.method == "POST":
        try:
            auxBotonActualizar = request.form["btoActualizar"]

            if auxBotonActualizar == "Actualizar":
                auxIdCat = id_cat
                auxNombreCat = request.form["txtCategoria"]
                auxIcono = request.form["txticono"]
                auxCategoria = mantenedorCategoria.Categoria(
                    auxIdCat, auxNombreCat, auxIcono
                )
                mantenedorCategoria.actualizar(auxCategoria)
                print("datos Actualizados")
                # flash('datos Actualizados')
        except:
            print("datos No Actualizados")
            # flash('datos No Actualizados')
        return redirect(url_for("listaCategoria"))


# endregion

# --------GUEST MAINTAINER
# region

# INSERTAR
@app.route("/insertar_invitado", methods=["POST"])
def insertar_invitado():
    if request.method == "POST":
        try:
            auxBotonInsertar = request.form["btoInsertar"]
            if auxBotonInsertar == "Insertar":
                auxIdInvitado = ""
                auxNombre = request.form["txtNombre"]
                auxApellido = request.form["txtApellido"]
                auxDescripcion = request.form["txtDescripcion"]

                auxUrlImg = request.files["txtUrl"]
                newAuxUrlImg = (
                    str(uuid.uuid1()) + os.path.splitext(auxUrlImg.filename)[1]
                )
                auxUrlImg.save(os.path.join("static/images", newAuxUrlImg))

                auxInvitado = claseInvitado.Invitado(
                    auxIdInvitado, auxNombre, auxApellido, auxDescripcion, newAuxUrlImg
                )
                mantenedorInvitado.insertar(auxInvitado)
                print("datos guardados")
                # flash('datos guardados')
        except:
            print("datos No guardados")
        return redirect(url_for("listaInvitado"))


# ELIMINAR
@app.route("/eliminar_invitado/<int:id_inv>")
def eliminar_invitado(id_inv):
    if request.method == "GET":
        try:
            mantenedorInvitado.eliminar(id_inv)
            print("datos Eliminados")
            # flash('datos Eliminados')
        except:
            print("datos No Eliminados")
            # flash('datos No Eliminados')
        return redirect(url_for("listaInvitado"))


# ACTUALIZAR
@app.route("/actualizar_invitado/<int:id_inv>", methods=["POST"])
def actualizar_invitado(id_inv):
    if request.method == "POST":
        try:
            auxBotonActualizar = request.form["btoActualizar"]

            if auxBotonActualizar == "Actualizar":
                auxIdInv = id_inv
                auxNombreInv = request.form["txtNombre"]
                auxApellidoInv = request.form["txtApellido"]
                auxDescripcionInv = request.form["txtDescripcion"]

                auxUrlImg = request.files["txtUrl"]
                newAuxUrlImg = (
                    str(uuid.uuid1()) + os.path.splitext(auxUrlImg.filename)[1]
                )
                auxUrlImg.save(os.path.join("static/images", newAuxUrlImg))

                auxInvitado = claseInvitado.Invitado(
                    auxIdInv,
                    auxNombreInv,
                    auxApellidoInv,
                    auxDescripcionInv,
                    newAuxUrlImg,
                )
                mantenedorInvitado.actualizar(auxInvitado)
                print("datos Actualizados")
                # flash('datos Actualizados')
        except:
            print("datos No Actualizados")
            # flash('datos No Actualizados')
        return redirect(url_for("listaInvitado"))


# endregion

# ADMINISTRATORS' MAINTAINER
# region

# INSERTAR
@app.route("/insertar_admin", methods=["POST"])
def insertar_admin():
    if request.method == "POST":
        try:
            auxBotonInsertar = request.form["btoInsertar"]
            if auxBotonInsertar == "Insertar":
                auxIdAdmin = ""
                auxUsuario = request.form["txtUsuario"]
                auxNombre = request.form["txtNombre"]
                auxPassword = request.form["txtPassword"]

                # auxUrlImg = request.files["txtUrl"]
                # newAuxUrlImg = (str(uuid.uuid1()) + os.path.splitext(auxUrlImg.filename)[1])
                # auxUrlImg.save(os.path.join("static/images", newAuxUrlImg))

                auxAdmin = claseAdmin.Admin(
                    auxIdAdmin, auxUsuario, auxNombre, auxPassword
                )
                mantenedorAdmin.insertar(auxAdmin)
                print("datos guardados")
                # flash('datos guardados')
        except:
            print("datos No guardados")
        return redirect(url_for("listaAdmin"))


# ACTUALIZAR
@app.route("/actualizar_admin/<int:idAdmin>", methods=["POST"])
def actualizar_admin(idAdmin):
    if request.method == "POST":
        try:
            auxBotonActualizar = request.form["btoActualizar"]

            if auxBotonActualizar == "Actualizar":
                auxIdAdm = idAdmin
                auxUserAdm = request.form["txtUsuario"]
                auxNombreAdm = request.form["txtNombre"]
                auxPassAdm = request.form["txtPassword"]

                # auxUrlImg = request.files["txtUrl"]
                # newAuxUrlImg = (
                #     str(uuid.uuid1()) + os.path.splitext(auxUrlImg.filename)[1]
                # )
                # auxUrlImg.save(os.path.join("static/images", newAuxUrlImg))

                auxAdmin = claseAdmin.Admin(
                    auxIdAdm, auxUserAdm, auxNombreAdm, auxPassAdm
                )
                mantenedorAdmin.actualizar(auxAdmin)
                print("datos Actualizados")
                # flash('datos Actualizados')
        except:
            print("datos No Actualizados")
            # flash('datos No Actualizados')
        return redirect(url_for("listaAdmin"))


# ELIMINAR
@app.route("/eliminar_admin/<int:idAdmin>")
def eliminar_admin(idAdmin):
    if request.method == "GET":
        try:
            mantenedorAdmin.eliminar(idAdmin)
            print("datos Eliminados")
            # flash('datos Eliminados')
        except:
            print("datos No Eliminados")
            # flash('datos No Eliminados')
        return redirect(url_for("listaAdmin"))


# endregion

# --------EVENT MAINTAINER
# INSERTAR
@app.route("/insertar_evento", methods=["POST"])
def insertar_evento():
    if request.method == "POST":
        try:
            auxBotonInsertar = request.form["btoInsertar"]
            if auxBotonInsertar == "Insertar":
                auxIdEvento = ""
                auxTitulo = request.form["txtTitulo"]
                auxFecha = request.form["txtFecha"]
                auxHora = request.form["txtHora"]
                auxEvento = claseEvento.Evento(auxIdEvento,auxTitulo,auxFecha,auxHora)
                mantenedorEvento.insertar(auxEvento)
                print("datos guardados")
                # flash('datos guardados')
        except:
            print("datos No guardados")
        return redirect(url_for("listaEvento"))


# ACTUALIZAR
@app.route("/actualizar_evento/<int:idEvento>", methods=["POST"])
def actualizar_evento(idEvento):
    if request.method == "POST":
        try:
            auxBotonActualizar = request.form["btoActualizar"]

            if auxBotonActualizar == "Actualizar":
                auxIdEvento = idEvento
                auxTitulo = request.form["txtTitulo"]
                auxFecha = request.form["txtFecha"]
                auxHora = request.form["txtHora"]
                auxEvento = claseEvento.Evento(
                    auxIdEvento, auxTitulo, auxFecha, auxHora
                )
                mantenedorEvento.actualizar(auxEvento)
                print("datos Actualizados")
                # flash('datos Actualizados')
        except:
            print("datos No Actualizados")
            # flash('datos No Actualizados')
        return redirect(url_for("listaEvento"))


# ELIMINAR
@app.route("/eliminar_evento/<int:idEvento>")
def eliminar_evento(idEvento):
    if request.method == "GET":
        try:
            mantenedorEvento.eliminar(idEvento)
            print("datos Eliminados")
            # flash('datos Eliminados')
        except:
            print("datos No Eliminados")
            # flash('datos No Eliminados')
        return redirect(url_for("listaEvento"))

if __name__ == "__main__":
    app.run(port=3000, debug=True)
