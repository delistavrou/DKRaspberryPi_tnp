import pygal  # First import pygal

bar_chart = pygal.Bar()                   # Then create a bar graph object
bar_chart.add('Graph', [1, 2, 3, 4])      # Add some values
bar_chart.render_to_file('bar_chart.svg') # Save the svg to a file