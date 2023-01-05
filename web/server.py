from random import randrange
from flask import Flask, render_template, request, redirect, render_template, session
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Grid, Line, Radar
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType
from pyecharts.charts import WordCloud
from pyecharts.charts import Funnel
from dao.mysql_dao import StoreMysqlPool
from pymysql.err import OperationalError
import platform
import settings

try:
    if "Ubuntu" in platform.platform():
        eb_supports = StoreMysqlPool(**settings.mysql_server)
    else:
        eb_supports = StoreMysqlPool(**settings.mysql_server_172)
except OperationalError:
    eb_supports = StoreMysqlPool(**settings.mysql_server)

app = Flask(__name__)

app.secret_key = 'QWERTYUIOP'  # 对用户信息加密


@app.route('/login', methods=['GET', "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'admin' and pwd == '123':
        session['user_info'] = user
        return redirect('/index')
    else:
        return render_template('login.html', msg='用户名或密码输入错误')


def pie_base():
    pie = Pie()
    sql = """
        SELECT
            data_price_interval,
            count( data_price_interval ) 
        FROM
            clean_jd_search_keyword 
        GROUP BY
            data_price_interval 
        ORDER BY
            data_price_interval
    """
    res = eb_supports.query(sql)
    pie.add("", res, center=["50%", "60%"])
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title="价格区\n间分布"),
        legend_opts=opts.LegendOpts(pos_left="15%"),
    )
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    return pie


def funnel_sort_ascending():
    sql = """
        SELECT
            `month`,
            count(`month`) as month_count
        FROM
            clean_jd_comment_product_page_comments_action 
        GROUP BY
            `month`
        ORDER BY `month_count` DESC
        limit 10
    """
    res = eb_supports.query(sql)
    funnel = Funnel()
    funnel.add(
        "月份销量",
        [list(z) for z in zip([item[0] + '月' for item in res], [item[1] for item in res])],
        sort_="ascending",
        label_opts=opts.LabelOpts(position="top")
    )
    funnel.set_global_opts(title_opts=opts.TitleOpts())
    return funnel


def boughnut_chart():
    sql = """
        SELECT
            score,
            count(score) as score_count
        FROM
            clean_jd_comment_product_page_comments_action 
        GROUP BY
            score
        ORDER BY 
            score DESC
    """
    res = eb_supports.query(sql)
    x_data = ['评分:' + str(item[0]) for item in res]
    y_data = [item[1] for item in res]
    pie = Pie()
    pie.add(
        series_name="评分分布",
        data_pair=[list(z) for z in zip(x_data, y_data)],
        radius=["40%", "90%"],
        center=["65%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    pie.set_global_opts(legend_opts=opts.LegendOpts(pos_left="legft", orient="vertical"))
    pie.set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ), )
    return pie


def word_cloud_diamond():
    words = [
        ("Sam S Club", 10000),
        ("Macys", 6181),
        ("Amy Schumer", 4386),
        ("Jurassic World", 4055),
        ("Charter Communications", 2467),
        ("Chick Fil A", 2244),
        ("Planet Fitness", 1868),
        ("Pitch Perfect", 1484),
        ("Express", 1112),
        ("Home", 865),
        ("Johnny Depp", 847),
        ("Lena Dunham", 582),
        ("Lewis Hamilton", 555),
        ("KXAN", 550),
        ("Mary Ellen Mark", 462),
        ("Farrah Abraham", 366),
        ("Rita Ora", 360),
        ("Serena Williams", 282),
        ("NCAA baseball tournament", 273),
        ("Point Break", 265),
    ]
    word_cloud = WordCloud()
    word_cloud.add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    word_cloud.set_global_opts(title_opts=opts.TitleOpts())
    return word_cloud


def bar_datazoom_slider():
    sql = """
        SELECT
            `month`,
            count(`month`) as month_count
        FROM
            clean_jd_comment_product_page_comments_action 
        GROUP BY
            `month`
        ORDER BY `month_count` DESC
    """
    res = eb_supports.query(sql)
    bar = Bar()
    bar.add_xaxis([item[0] + '月' for item in res])
    bar.add_yaxis("月份销量", [item[1] for item in res])
    bar.set_global_opts(
        title_opts=opts.TitleOpts(),
        datazoom_opts=opts.DataZoomOpts(),
    )
    grid = Grid()
    grid.add(bar, grid_opts=opts.GridOpts(pos_left="15%"))
    return grid


@app.route("/index")
@app.route("/")
def index():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    return render_template("index.html")


@app.route("/pie_chart")
def get_pie_chart():
    c = pie_base()
    return c.dump_options_with_quotes()


@app.route("/funnel_sort_ascending")
def get_funnel_sort_ascending():
    c = funnel_sort_ascending()
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


if __name__ == "__main__":
    app.run()
