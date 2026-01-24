from quart import Blueprint, render_template, redirect, url_for, session
main_bp = Blueprint("main", __name__)

@main_bp.route('/', methods=["GET"])
async def index():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    return await render_template('index.html')