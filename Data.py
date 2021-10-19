import pandas as p
import csv
from pandas.core import groupby
import plotly.graph_objects as go

fileName = p.read_csv('StudentData.csv')

data= fileName.loc[fileName['student_id']=='TRL_xsl']

grouping=data.groupby('level')['attempt'].mean()

graph=go.Figure(go.Bar(
    x=data.groupby('level')['attempt'].mean(),
    y=['Level 1','Level 2','Level 3','Level 4'],
    orientation='h'
))

print(grouping)

graph.show()
