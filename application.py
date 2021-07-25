import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash
import pandas as pd

app = dash.Dash(__name__, title = 'Lagos Housing')

df = pd.read_csv('model_app_data.csv')
med_price = pd.DataFrame(df.groupby('location')['price'].median())
med_price.reset_index(inplace = True)
import json
with open('lagos_Cities.geojson', 'r') as f:
    file = json.load(f)

def max_price(area, beds):
    return df[(df['property_area'] == area) & (df['bed'] == beds)]['price'].max()

def median_price(area, beds):
    return df[(df['property_area'] == area) & (df['bed'] == beds)]['price'].median()

def min_price(area, beds):
    return df[(df['property_area'] == area) & (df['bed'] == beds)]['price'].min()

def min_location_price(location, beds):
    return df[(df['location'] == location) & (df['bed'] == beds)]['price'].min()

def med_location_price(location, beds):
    return df[(df['location'] == location) & (df['bed'] == beds)]['price'].median()

def max_location_price(location, beds):
    return df[(df['location'] == location) & (df['bed'] == beds)]['price'].max()

def choropleth_map():
    fig = px.choropleth_mapbox(med_price, geojson=file, locations='location', color='price',
                           color_continuous_scale="Viridis",
                           range_color=(500000, 3500000),
                           mapbox_style="carto-positron", zoom=10, center = {"lat": 6.561678835878642, "lon": 3.323086126993425},
                           opacity=0.5, labels = {'Price': 'Location_Median_Price'}
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()


app.layout = html.Main([
                html.Div([
                    html.H3(
                        'CHARTS',
                        className = 'chart-title'
                    ),
                    html.Div([
                        dcc.Graph(id = 'choropleth-map', figure = choropleth_map())
                    ], className = 'graph-container')
                ], id = 'main-bar'),
                html.Div([
                    html.H3(
                        'LAGOS STATE HOUSE PRICE ESTIMATE',
                        className = 'project-title'
                    ),
                    html.Form([
                        html.Div([
                            html.Label(
                                'Property Location',
                                className = 'location'
                            ),
                            dcc.Dropdown(
                                id = 'Locations',
                                options = [
                                    {'label':'Gbagada', 'value':'gbagada'},
                                    {'label':'Ajah', 'value':'ajah'},
                                    {'label':'Yaba', 'value':'yaba'},
                                    {'label':'Surulere', 'value':'surulere'},
                                    {'label':'Ikeja', 'value':'ikeja'},
                                    {'label':'Ikorodu', 'value':'ikorodu'},
                                    {'label':'Lekki-Phase-1', 'value':'lekki'}
                                ],
                                value = 'Ajah'
                            )
                        ], className = 'form-group'),
                        html.Div([
                            html.Label(
                                'Property Specific Area',
                                className = 'area'
                            ),
                            dcc.Input(
                                id = 'my area',
                                type = 'text',
                                value = 'abijo',
                                placeholder = 'Abijo'
                            )
                        ], className = 'form-group'),
                        html.Div([
                            html.Label(
                                'Bedrooms',
                                className = 'beds'
                            ),
                            dcc.Dropdown(
                            id = 'bedrooms',
                            options = [
                                {'label':'1', 'value':1},
                                {'label': '2', 'value':2},
                                {'label': '3', 'value':3},
                                {'label': '4', 'value':4}
                            ],
                            value = 1
                            )
                        ], className = 'form-group')
                    ], className = 'my-form'),
                    html.Div([
                        html.Div([
                            html.H3(
                                children = '2000000',
                                id = 'minimum-price'
                            ),
                            html.P(
                                children = 'Minimum Price in Ajah',
                                id = 'minimum-description'
                            )
                        ], className = 'location-tab'),
                        html.Div([
                            html.H3(
                                children = '2000000',
                                id = 'median-price'
                            ),
                            html.P(
                                children = 'Median Price in Ajah',
                                id = 'median-description'
                            )
                        ], className = 'location-tab'),
                        html.Div([
                            html.H3(
                                children = '2000000',
                                id = 'maximum-price'
                            ),
                            html.P(
                                children = 'Maximum Price in Ajah',
                                id = 'maximum-description'
                            )
                        ], className = 'location-tab')
                    ], className = 'location-summary'),
                    html.Div([
                        html.Div([
                            html.H3(
                                children = '2000000',
                                id = 'min-price'
                            ),
                            html.P(
                                children = 'Minimum Price in Abijo',
                                id = 'min-description'
                            )
                        ], className = 'location-tab'),
                        html.Div([
                            html.H3(
                                children = '2000000',
                                id = 'med-price'
                            ),
                            html.P(
                                children = 'Median Price in Abijo',
                                id = 'med-description'
                            )
                        ], className = 'location-tab'),
                        html.Div([
                            html.H3(
                                children = '2000000',
                                id = 'max-price'
                            ),
                            html.P(
                                children = 'Maximum Price in Abijo',
                                id = 'max-description'
                            )
                        ], className = 'location-tab')
                    ], className = 'location-summary')
                ], id = 'side-bar')
], id = 'body')

@app.callback(
    Output(component_id = 'minimum-price', component_property = 'children'),
    Output(component_id = 'median-price', component_property = 'children'),
    Output(component_id = 'maximum-price', component_property = 'children'),
    Output(component_id = 'min-price', component_property = 'children'),
    Output(component_id = 'med-price', component_property = 'children'),
    Output(component_id = 'max-price', component_property = 'children'),
    Output(component_id = 'minimum-description', component_property = 'children'),
    Output(component_id = 'median-description', component_property = 'children'),
    Output(component_id = 'maximum-description', component_property = 'children'),
    Output(component_id = 'min-description', component_property = 'children'),
    Output(component_id = 'med-description', component_property = 'children'),
    Output(component_id = 'max-description', component_property = 'children'),
    Output(component_id = 'choropleth-map', component_property = 'figure'),
    Input(component_id = 'Locations', component_property = 'value'),
    Input(component_id = 'my area', component_property = 'value'),
    Input(component_id = 'bedrooms', component_property = 'value')
)

def update_output_div(location, area, beds):
    location = location.lower()
    return min_location_price(location, beds), med_location_price(location, beds), max_location_price(location, beds), min_price(area, beds), median_price(area, beds), max_price(area, beds), 'Minimum price in {}'.format(location), 'Median price in {}'.format(location), 'Maximum price in {}'.format(location), 'Minimum price in {}'.format(area), 'Median price in {}'.format(area), 'Maximum price in {}'.format(area), choropleth_map()



if __name__ == '__main__':
    app.run_server(debug=True)
