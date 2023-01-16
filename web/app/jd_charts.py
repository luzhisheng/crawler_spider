from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Grid
from pyecharts.globals import SymbolType
from pyecharts.charts import WordCloud
from base import eb_supports


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


def bar_reversal_axis():
    sql = """
        SELECT
            shop_name,
            sum(count_comments_id) as sum_count_comments_id
        FROM
            (
            SELECT
                product_id_search,
                shop_name,
                count_comments_id
            FROM
                clean_jd_search_keyword z
            RIGHT JOIN ( SELECT product_id, count( `comments_id` ) AS count_comments_id FROM clean_jd_comment_product_page_comments_action GROUP BY product_id ) x ON x.product_id = z.product_id_search
            ) AS t
        GROUP BY
            shop_name
        ORDER BY
            sum_count_comments_id DESC
        limit 10
    """
    res = eb_supports.query(sql)
    bar = Bar()
    bar.add_xaxis([item[0].replace('旗舰店', '').replace('官方', '') for item in res])
    bar.add_yaxis("店铺销量前10", [item[1] for item in res])
    bar.reversal_axis()
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
    bar.set_global_opts(title_opts=opts.TitleOpts())
    grid = Grid()
    grid.add(bar, grid_opts=opts.GridOpts(pos_left="40%"))
    return grid


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
    sql = """
        SELECT
            cut,
            COUNT( cut ) AS count_cut 
        FROM
            clean_jd_comment_cuts 
        GROUP BY
            cut 
        ORDER BY
            count_cut DESC
        LIMIT 50;
    """
    res = eb_supports.query(sql)
    word_cloud = WordCloud()
    word_cloud.add("", res, word_size_range=[5, 100], shape=SymbolType.DIAMOND)
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
