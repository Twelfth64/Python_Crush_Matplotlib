from plotly.graph_objs import Bar, Layout
from plotly import offline

from Matplotlib_example.die import Die


die_1 = Die(6)
die_2 = Die(6)

results = [die_1.roll()*die_2.roll() for roll_num in range(1000)]

max_result = die_1.num_sides + die_2.num_sides

frequencies = [results.count(value) for value in range(2, max_result + 1)]

x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and D10 50000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

