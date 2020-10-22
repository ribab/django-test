from django.shortcuts import render

import plotly.offline as opy
import plotly.graph_objs as go

def index(request):

    trace = go.Figure(
                data=[
                    go.Bar(
                        name="Original",
                        x=[1,2,3,4],
                        y=[1,2,3,4],
                        offsetgroup=0,
                    ),
                ],
                layout=go.Layout(
                    title="Bar Chart",
                    yaxis_title="y axis values"
                )
            )

    bar_div = opy.plot(trace, auto_open=False, output_type='div')

    context = {}
    context['bar_div'] = bar_div

    return render(request, 'index.html', context)

