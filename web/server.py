from flask import Flask, request, redirect, render_template, session, make_response, jsonify, url_for
from flask_login import LoginManager, current_user
from flask_login import logout_user, login_user, login_required
from app.user import User, get_user, create_user
from app.jd_charts import pie_base, boughnut_chart, bar_reversal_axis, word_cloud_diamond, bar_datazoom_slider
from form.signup_form import SignupForm
from form.login_form import LoginForm
from base import eb_supports


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


@app.route("/pie_chart")
def get_pie_chart():
    c = pie_base()
    return c.dump_options_with_quotes()


@app.route("/bar_reversal_axis")
def get_bar_reversal_axis():
    c = bar_reversal_axis()
    return c.dump_options_with_quotes()


@app.route("/boughnut_chart")
def get_boughnut_chart():
    c = boughnut_chart()
    return c.dump_options_with_quotes()


@app.route("/word_cloud_diamond")
def get_lword_cloud_diamond():
    c = word_cloud_diamond()
    return c.dump_options_with_quotes()


@app.route("/bar_datazoom_slider")
def get_bar_datazoom_slider():
    c = bar_datazoom_slider()
    return c.dump_options_with_quotes()


@app.route("/monitor_store")
def get_monitor_store():
    sql = """
        SELECT
            count(*) as count_shop_name
        FROM
            ( SELECT shop_name FROM clean_jd_search_keyword GROUP BY shop_name ) AS t
    """
    res_count_shop_name = eb_supports.query(sql)

    sql = """
        SELECT
            count(*) AS count_comments_id
        FROM
            ( SELECT comments_id FROM clean_jd_comment_product_page_comments_action GROUP BY comments_id ) AS t
    """
    res_count_comments_id = eb_supports.query(sql)

    sql = """
        SELECT
            count(*) AS count_product_id
        FROM
            ( SELECT product_id FROM clean_jd_comment_product_page_comments_action GROUP BY product_id ) AS t
    """
    res_count_product_id = eb_supports.query(sql)

    sql = """
        SELECT
            sum(data_price) as sum_data_price
        FROM
            clean_jd_search_keyword z
            RIGHT JOIN clean_jd_comment_product_page_comments_action x ON x.product_id = z.product_id_search
    """
    res_sum_data_price = eb_supports.query(sql)

    data = {
        'count_shop_name': res_count_shop_name[0][0],
        'count_comments_id': res_count_comments_id[0][0],
        'count_product_id': res_count_product_id[0][0],
        'sum_data_price': res_sum_data_price[0][0],
    }
    resp = make_response(jsonify(data))
    resp.status = "200"
    resp.headers["ContentType"] = "application/json"
    return resp


@app.route("/product_sales")
def get_product_sales():
    sql = """
        SELECT
            product_color,
            data_price,
            sum(count_comments_id) as sum_count_comments_id,
            data_price * sum(count_comments_id) as total_sales,
            shop_name
        FROM
            (
            SELECT
                product_color,
                data_price,
                count_comments_id,
                product_id_search,
                shop_name 
            FROM
                clean_jd_search_keyword z
            RIGHT JOIN ( SELECT product_id, count( comments_id ) AS count_comments_id, product_color FROM clean_jd_comment_product_page_comments_action GROUP BY product_id ) x ON x.product_id = z.product_id_search 
            ) t
        WHERE
            product_color != ''
        GROUP BY
            shop_name
        ORDER BY
            total_sales desc
        LIMIT 6
    """
    res_product_sales = eb_supports.query(sql)
    list_dict = []
    for product_sales in res_product_sales:
        data = {
            'product_color': product_sales[0],
            'data_price': product_sales[1],
            'count_comments_id': product_sales[2],
            'product_id_search': product_sales[3],
            'shop_name': product_sales[4],
        }
        list_dict.append(data)
    resp = make_response(jsonify(list_dict))
    resp.status = "200"
    resp.headers["ContentType"] = "application/json"
    return resp


if __name__ == "__main__":
    app.run()
