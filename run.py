from app import app #default flask-in ilk setrini cagiriram
from app import routes#default flask-in routlarini cagiriram
from admin import routes#admin panelin route-di route-da /admin/ var
if __name__ == "__main__":#default flask-in run kodunu yaziram
    app.run(debug=True)