
from app import app
from flask import Flask, render_template, redirect, url_for,request
from config import mail_username, mail_password

@app.route("/")
def home():
    return render_template("/Home.html")

@app.route("/home")
def home1():
    return render_template("/Home.html")

@app.route("/about")
def about():
   return render_template("/About.html")

@app.route("/Contact" , methods=['GET', 'POST'])
def Contact():
    # if request.method == "POST":
    #     name= request.form.get('name')
    #     email= request.form.get('email')
    #     phone= request.form.get('phone')
    #     product=request.form.get('product')
    #     message = request.form.get('message')

    #     msg = message(subject=f"Mail from {name}", body=f"Name:{name}\n E-mail: {email}\nPhone:{phone}\n Product:{product}\n\n\n {message}",sender=mail_username,recipients=["cavid.hasanov2@bk.ru"])         mail.send(msg)         return redirect("/Contact", succes=True)     return render_template("Contact.html")#About Sehifesi
    return render_template("/contact.html")