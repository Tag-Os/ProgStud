import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

def f(x):
    x = np.asarray(x)
    result = np.zeros_like(x)
    mask1 = (x >= 0) & (x <= 1)
    result[mask1] = -np.cos(np.exp(x[mask1]))
    mask2 = (x > 1) & (x <= 2)
    result[mask2] = np.log(2 * x[mask2] + np.sin(x[mask2] ** 2))
    return result

def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

x = np.linspace(0, 2, 1000)
y = f(x)

x0 = 1.5
y0 = f(x0)
f_prime_x0 = derivative(f, x0)

x_tangent = np.linspace(x0 - 0.5, x0 + 0.5, 100)
y_tangent = f_prime_x0 * (x_tangent - x0) + y0

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x, y=y,
    mode='lines',
    name='f(x)',
    line=dict(color='blue', width=2)
))

fig.add_trace(go.Scatter(
    x=x_tangent, y=y_tangent,
    mode='lines',
    name='Касательная в точке x = 1.5',
    line=dict(color='red', width=2, dash='dash')
))

fig.add_trace(go.Scatter(
    x=[x0], y=[y0],
    mode='markers',
    name=f'Точка касания ({x0:.2f}, {y0:.2f})',
    marker=dict(color='green', size=10, symbol='circle')
))

fig.update_layout(
    title='График функции f(x) и касательная в точке x = 1.5',
    xaxis_title='x',
    yaxis_title='f(x)',
    width=800,
    height=600,
    hovermode='closest'
)

pio.write_html(fig, 'interactive_graph.html')
print("Файл сохранён как interactive_graph.html")

fig.show()