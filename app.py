from quart import Quart, render_template, url_for, redirect, session, request
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
import sys, os

load_dotenv()
secret = os.getenv("SECRET_KEY")
if not secret:
    sys.exit()


app = Quart(__name__)
app.secret_key(secret)

USERS = { "admin": generate_password_hash("1234") }


@app.route('/', methods=["GET"])
async def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return await render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
async def login():
    if 'user' in session:
        return redirect(url_for('index'))
    if request.method == "POST":
        form      = await request.form
        username  = form['username']
        password  = form['password']
        user_hash = USERS.get(username)
        
        if not user_hash or not check_password_hash(user_hash, password):
            return await render_template('login.html', error = "Invalid username or password"), 401
        
        session['user'] = username
        
        return redirect(url_for('index'))
    return await render_template('login.html')

@app.route('/logout')
async def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)