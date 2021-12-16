from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
if __name__ == "__main__":
    app.run()


app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

from application.models.tables import User

@login_manager.user_loader
def load_user(user_id):
    return User.get_id

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from application.controllers import controller
from application.models import tables, forms
