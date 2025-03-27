from flask import Flask
from views import main
from models import db
from flask_migrate import Migrate
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///project.db"
db.init_app(app)
migrate=Migrate(app,db)
app.register_blueprint(main)

if __name__=="__main__":
    app.run(debug=True)

