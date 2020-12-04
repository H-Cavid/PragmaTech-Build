from app import app
from app import routes
from admin import routes
from flask_mail import Mail, Message
from config import mail_username, mail_password


app.config["MAIL_SERVER"]="smtp-mail.outlook.com"
app.config["MAIL_PORT"]=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False
app.config['MAIL_USERNAME']=mail_username
app.config['Mail_PASSWORD']=mail_password


mail=Mail(app)



if __name__ == "__main__":
    app.run(debug=True)