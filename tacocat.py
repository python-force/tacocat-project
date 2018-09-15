from flask import Flask, g, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

import forms
import models

# DEBUG = True
# PORT = 8000
# HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'sd7sa76v8*&%7asf7656#dsjksadjwaalcma.caskascjhavs'

app.run(debug=True, port=8000, host='0.0.0.0')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


@app.route('/')
def index():
    return render_template('index.html')