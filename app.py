from flask import Flask, render_template, request, redirect, url_for, session, flash


app = Flask (__name__)
app.secret_key = 'secreto de amor' 


USUARIOS_SIMULADOS = {
    "admin": "123456", 
    "invitado": "password",
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/ace")
def ace():
    return render_template("ace.html")

@app.route("/vei")
def vei():
    return render_template("vei.html")

@app.route("/mun")
def mun():
    return render_template("mun.html")



@app.route("/ani")
def ani():
    """Ruta protegida que requiere sesión activa."""
    if 'usuario_logueado' not in session:

        flash(' Debes iniciar sesión para acceder a "Animales Exóticos".', 'warning')
        return redirect(url_for('inici'))
    return render_template("ani.html")




@app.route("/inici", methods=["GET", "POST"])
def inici():
    """Maneja el formulario de inicio de sesión (Punto 1 y 4)."""

    if 'usuario_logueado' in session:
        return redirect(url_for('index'))

    if request.method == "POST":
        usuario = request.form.get("usuario")
        clave = request.form.get("clave")

        if usuario in USUARIOS_SIMULADOS and USUARIOS_SIMULADOS[usuario] == clave:
            session['usuario_logueado'] = usuario
            flash(f' ¡Bienvenido, {usuario}! Sesión activa.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuario o Clave incorrectos. Inténtalo de nuevo.', 'danger')

    return render_template("inici.html")




@app.route("/cerrar_sesion")
def cerrar_sesion():
    """Cierra la sesión activa."""

    session.pop('usuario_logueado', None)
    flash(' Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
