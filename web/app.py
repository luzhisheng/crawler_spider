from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, current_user
from flask_login import logout_user, login_user, login_required
from app.user import User, get_user, create_user
from form.signup_form import SignupForm
from form.login_form import LoginForm


app = Flask(__name__)  # 创建 Flask 应用
app.secret_key = 'abc'  # 设置表单交互密钥
login_manager = LoginManager()  # 实例化登录管理对象
login_manager.init_app(app)  # 初始化应用
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'  # 设置用户登录视图函数 endpoint


@login_manager.user_loader  # 定义获取登录用户的方法
def load_user(user_id):
    return User.get(user_id)


@app.route('/signup', methods=('GET', 'POST'))  # 注册
def signup():
    form = SignupForm()
    emsg = None
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data

        user_info = get_user(user_name)  # 用用户名获取用户信息
        if user_info is None:
            create_user(user_name, password)  # 如果不存在则创建用户
            return redirect(url_for("login"))  # 创建后跳转到登录页
        else:
            emsg = "用户名已存在"  # 如果用户已存在则给出错误提示
    return render_template('signup.html', form=form, emsg=emsg)


@app.route('/login', methods=('GET', 'POST'))  # 登录
def login():
    form = LoginForm()
    emsg = None
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_info = get_user(user_name)
        if user_info is None:
            emsg = "用户名或密码密码有误"
        else:
            user = User(user_info)
            if user.verify_password(password):
                login_user(user)
                return redirect(request.args.get('next') or url_for('index'))
            else:
                emsg = "用户名或密码密码有误"
    return render_template('login.html', form=form, emsg=emsg)


@app.route('/')  # 首页
@login_required  # 需要登录才能访问
def index():
    return render_template('index.html', username=current_user.username)


@app.route('/logout')  # 登出
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
