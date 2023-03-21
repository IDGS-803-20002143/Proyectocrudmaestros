from Maestros import maestros
from Alumnos import alumnos
from flask import Flask, render_template
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db, Alumnos, Maestros




app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
crsf = CSRFProtect()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.errorhandler(404)
def no_encontrada(e):
    return render_template("404.html"),404

app.register_blueprint(alumnos)
app.register_blueprint(maestros)

if __name__ =="__main__":
    crsf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)