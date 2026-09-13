from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user

from .forms import LoginForm
from models.usuario import Usuario


auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates"
)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        usuario = Usuario.query.filter_by(
            username=form.username.data
        ).first()

        if usuario and usuario.verificar_password(form.password.data):
            login_user(usuario)
            return redirect(url_for("dashboard.inicio"))

        flash("Los datos ingresados son incorrectos.", "danger")

    return render_template("auth/login.html", form=form)

@auth.route("/logout")
def logout():
    logout_user()

    return redirect(url_for("auth.login"))