from django.shortcuts import render
from django.views import View

from plotly.offline import plot
from plotly.graph_objects import Scatter

class IndexView(View):
    def get(self, request, *args, **kwargs):
        x_data = [0, 1, 2, 3]
        y_data = [x**2 for x in x_data]

        scatter_object = Scatter(
            x=x_data, y=y_data, mode='lines', name='test', opacity=0.8,
            marker_color='green')

        scatter_chart = plot(
            [scatter_object], output_type='div', include_plotlyjs=False,
            show_link=False, link_text="")

        return render(request, 'charts/index.html', {
            'scatter_chart': scatter_chart
        })
