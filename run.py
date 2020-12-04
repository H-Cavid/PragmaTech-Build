#default flask-in ilk setrini cagiriram
# from app import routes#default flask-in routlarini cagiriram
# from admin import routes#admin panelin route-di route-da /admin/ var
from flask_mail import Mail, Message
from config import mail_username, mail_password
from flask import Flask

app=Flask(__name__)

app.config["MAIL_SERVER"]="smtp-mail.outlook.com"
app.config["MAIL_PORT"]=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False
app.config['MAIL_USERNAME']=mail_username
app.config['Mail_PASSWORD']=mail_password


mail=Mail(app)

@app.route("/")
def About():
   return 'render_template("About.html")#About Sehifesi'

if __name__ == "__main__":#default flask-in run kodunu yaziram
    app.run(debug=True)