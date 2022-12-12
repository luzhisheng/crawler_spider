# 定时刷新的核心在于 HTML 的 setInterval 方法。

from random import randrange
from flask import Flask, render_template
from pyecharts import options as opts
from pyecharts.charts import Bar


app = Flask(__name__, static_folder="templates", template_folder='../templates')


def bar_base() -> Bar:
    bar = Bar()
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
    bar.add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    return bar


@app.route("/")
def index():
    return render_template("/8index.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    app.run()
