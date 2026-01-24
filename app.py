from quart import Quart
from main.routes import main_bp
from auth.routes import auth_bp
from config import secret
app = Quart(__name__)
app.secret_key = secret

app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(debug=True)