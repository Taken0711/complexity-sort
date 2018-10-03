import csv

import argparse
import plotly.graph_objs as go
from plotly.offline import plot, iplot
import math
import numpy

parser = argparse.ArgumentParser()
parser.add_argument("--csv", help="The csv that needs to be plotted",
                    default='../test.csv')
args = parser.parse_args()


def read_csv(csv_file):
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        d = {key: [] for key in reader.fieldnames}
        rows = [row for row in reader]
        for key in reader.fieldnames:
            print(key)
            for row in rows:
                d[key].append(row[key])
        return d


df = read_csv(args.csv)
exponents = {}
for k in df:
    if k != "array size":
        xmap = list(map(int, df["array size"][8:]))
        x = numpy.log(numpy.asarray(xmap))
        ymap = list(map(float, df[k][8:]))
        y = numpy.log(numpy.asarray(ymap))
        cov = numpy.cov(x, y)
        exponents[k] = cov[1][0] / cov[0][0]
print(exponents)
traces = []
for k in df:
    if k != "array size":
        trace = go.Scatter(
            x=df['array size'], y=df[k],  # Data
            mode='lines+text', name=f"{k}",
            hoverinfo="y+text", hovertext=f"a={exponents[k]}")
        traces.append(trace)

layout = go.Layout(title='Simple Plot from csv data',
                   xaxis=dict(
                       type='log',
                       autorange=True
                   ),
                   yaxis=dict(
                       type='log',
                       autorange=True
                   ),
                   plot_bgcolor='rgb(230, 230,230)')
#
fig = go.Figure(data=traces, layout=layout)

# # Plot data in the notebook
plot(fig, filename='simple-plot-from-csv')
