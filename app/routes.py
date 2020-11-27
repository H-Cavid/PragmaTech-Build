from flask import Flask, render_template, redirect, url_for
from app import app

@app.route("/")
def Home():
    return render_template("Home.html")#Home sehifesi

@app.route("/Home")
def Home1():
    return render_template("Home.html")#Home sehifesi


@app.route("/About")
def About():
   return render_template("About.html")#About Sehifesi

@app.route("/Contact")
def Contact():
   return render_template("Contact.html")#About Sehifesi