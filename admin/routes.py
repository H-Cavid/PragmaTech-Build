from flask import render_template
from app import app

@app.route("/admin/")
def index():
   return render_template("Layout.html")

