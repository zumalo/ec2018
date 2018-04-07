import pygal

def create_chart(list, chart_name):
    horizontalbar_chart = pygal.HorizontalBar()
    horizontalbar_chart.title = chart_name
    for element in list:
        horizontalbar_chart.add(element[0], element[1])
    horizontalbar_chart.render_to_file('{}_chart.svg'.format(chart_name))

