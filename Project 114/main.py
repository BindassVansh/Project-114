from numpy.core.fromnumeric import shape
import pandas as pd
import plotly.express as pe
import numpy as np

yvalue = []

df = pd.read_csv('main.csv')
grescore = df['GREScore'].tolist()
chance = df['Chance'].tolist()

grescore_array = np.array(grescore)
chance_array = np.array(chance)

m, c = np.polyfit(grescore_array, chance_array, 1)
print(m, c)

for x in grescore:
    y = m * x + c
    yvalue.append(y)

graph = pe.scatter(x=grescore, y=chance)
graph.update_layout(shapes=[dict(type="line", y0=min(
    yvalue), y1=max(yvalue), x0=min(grescore), x1=max(grescore))])
graph.show()
