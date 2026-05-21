from flask import Flask, render_template, request, redirect
from flask import session, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import os
import io

from encryption import encrypt_file, decrypt_file

app = Flask(__name__)

app.config["SECRET_KEY"]="vault123"

app.config["SQLALCHEMY_DATABASE_URI"] = \
"sqlite:///vault.db"

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

UPLOAD="uploads"

os.makedirs(UPLOAD,exist_ok=True)


class User(db.Model):

    id=db.Column(
        db.Integer,
        primary_key=True
    )

    username=db.Column(
        db.String(100),
        unique=True
    )

    password=db.Column(
        db.String(255)
    )


class File(db.Model):

    id=db.Column(
        db.Integer,
        primary_key=True
    )

    filename=db.Column(
        db.String(200)
    )

    owner=db.Column(
        db.String(100)
    )


with app.app_context():
    db.create_all()


@app.route("/")
def home():

    if "user" not in session:
        return redirect("/login")

    files=File.query.filter_by(
        owner=session["user"]
    )

    return render_template(
        "dashboard.html",
        files=files
    )


@app.route(
"/register",
methods=["GET","POST"]
)

def register():

    error=None

    if request.method=="POST":

        username=request.form["username"]

        password=request.form["password"]

        existing=User.query.filter_by(
            username=username
        ).first()

        if existing:

            error="Username already exists"

            return render_template(
                "register.html",
                error=error
            )

        hashed=bcrypt.generate_password_hash(
            password
        ).decode()

        try:

            db.session.add(

                User(
                    username=username,
                    password=hashed
                )

            )

            db.session.commit()

            return redirect(
                "/login"
            )

        except Exception:

            db.session.rollback()

            error="Registration failed"

    return render_template(
        "register.html",
        error=error
    )


@app.route(
"/login",
methods=["GET","POST"]
)

def login():

    if request.method=="POST":

        username=request.form["username"]
        password=request.form["password"]

        user=User.query.filter_by(
            username=username
        ).first()

        if not user:
            return "User does not exist"

        if bcrypt.check_password_hash(
            user.password,
            password
        ):

            session["user"]=user.username

            return redirect("/")

        return "Wrong password"

    return render_template(
        "login.html"
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


@app.route(
"/upload",
methods=["POST"]
)

def upload():

    f=request.files["file"]

    encrypted=encrypt_file(
        f.read()
    )

    path=os.path.join(
        UPLOAD,
        f.filename+".enc"
    )

    open(
        path,
        "wb"
    ).write(
        encrypted
    )

    db.session.add(
        File(
            filename=f.filename,
            owner=session["user"]
        )
    )

    db.session.commit()

    return redirect("/")


@app.route(
"/download/<name>"
)

def download(name):

    path=os.path.join(
        UPLOAD,
        name+".enc"
    )

    decrypted=decrypt_file(
        open(
            path,
            "rb"
        ).read()
    )

    return send_file(
        io.BytesIO(
            decrypted
        ),

        download_name=name,

        as_attachment=True
    )


if __name__=="__main__":

    app.run(
        debug=True
    )