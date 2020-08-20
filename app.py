import os
import pathlib

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output

APP_PATH = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(os.path.join(APP_PATH, os.path.join("final_data", "_raw_dataset.csv")))

df['from_date'] = pd.to_datetime(df['from_date'])
df['crawl_date'] = pd.to_datetime(df['crawl_date'])
df['days_in_advance'] = (df['from_date'] - df['crawl_date']).dt.days

df = df[df.to_city == 'MAA']
df.sort_values(['crawl_date', 'from_date'], ascending = [True, True], inplace = True)
df = df[df.days_in_advance == 30]
df = df[~df.airline_name.isna()]

airlines = df['airline_name'].unique().tolist()
to_cities = df['to_city'].unique().tolist()
days_in_advance = df['days_in_advance'].unique().tolist()

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True


def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list

app.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='four columns div-user-controls',
                             children=[
                                 html.H1('Gute Reise'),
                                 html.H4('Historical flight prices between Munich and Chennai, Kolkata, Mumbai, Delhi and Bengaluru'),
                                 html.Div(
                                     className='div-for-dropdown',
                                     children=[
                                         dcc.RadioItems(id='stockselector', options=get_options(df['airline_name'].unique()),
                                                      style={'backgroundColor': '#1E1E1E'},
                                                      className='stockselector'
                                                      ),
                                     ],
                                     style={'color': '#1E1E1E'})
                                ]
                             ),
                    html.Div(className='eight columns div-for-charts bg-grey',
                             children=[
                                 dcc.Graph(id='timeseries', config={'displayModeBar': False}, animate=True)
                             ])
                    ])
        ])

@app.callback(Output('timeseries', 'figure'),
              [Input('stockselector', 'value')])
def update_graph(selected_dropdown_value):
    trace1 = []
    df_sub = df
    for stock in selected_dropdown_value:
        trace1.append(go.Scatter(x=df_sub[df_sub['airline_name'] == stock]['crawl_date'],
                                 y=df_sub[df_sub['airline_name'] == stock]['ticket_price'],
                                 mode='lines',
                                 opacity=0.7,
                                 name=stock,
                                 textposition='bottom center'))
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Price Trends', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub.crawl_date.min(), df_sub.crawl_date.max()]},
              ),

              }

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)