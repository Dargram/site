from quart import Blueprint, render_template, redirect, session, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash
auth_bp = Blueprint("auth", __name__)

USERS = { "admin": generate_password_hash("1234") }

@auth_bp.route('/login', methods=["GET", "POST"])
async def login():
    if 'user' in session:
        return redirect(url_for('main.index'))
    if request.method == "POST":
        form      = await request.form
        username  = form['username']
        password  = form['password']
        user_hash = USERS.get(username)
        
        if not user_hash or not check_password_hash(user_hash, password):
            return await render_template('login.html', error = "Invalid username or password"), 401
        
        session['user'] = username
        
        return redirect(url_for('main.index'))
    return await render_template('login.html')


@auth_bp.route('/logout')
async def logout():
    session.clear()
    return redirect(url_for('auth.login'))