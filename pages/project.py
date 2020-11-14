import dash
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from model.maps import MapAnalysis
from model.time_series import TimeSeriesAnalysis
from model.data_access import DataAccess

class ProjectPage():
    
    # Hourly and daily analysis on maps
    maps = MapAnalysis()
    # time series analysis
    time_series = TimeSeriesAnalysis()
    
    # Some variables for handling graphs:
    variable = 'Leq'
    medida = 'Valor_mean'
    cai = "CAI 20 de Julio"
    
    # Analysis Page
    project_info = html.Div(
        [
            html.H2("Noise analysis", className='k2-title'),
            html.P(
                "In this view you will find analysis for the information provided for noise in \
                different locations of Bogotá, Colombia",
                className='gen-info',
            ),
            html.Hr(className="my-2")
        ],
        className='col-md-12'
    )
    
    tab_maps = html.Div(
        [
            html.Div(
                [
                    "Noise changes during the day in Bogotá",
                ],
                className='card-header'
            ),
            html.Div(
                [
                    html.P("Use the sliders to explore how the average noise changes during the day in Bogotá. \
                        You can Zoom-In and Zoom-out", className='gen-info'),
                    html.Div([dcc.Graph(figure=maps.get_hourly_map())], id="graph-map-1", className="fullscreen-div"),
                ], className="card-body",
            ),
            html.Div(html.Button('Full screen', id='map-btn-1', className="fullscreen btn btn-secondary"), 
                     className='d-block text-right card-footer'),
            html.Div(
                [
                    "Noise changes during the week in Bogotá",
                ],
                className='card-header card-header-no-top'
            ),
            html.Div(
                [
                    html.P(
                        "Use the sliders to explore how the average noise changes during the day in Bogotá. \
                        You can Zoom-In and Zoom-out ",
                        className='gen-info'),
                    html.Div([dcc.Graph(figure = maps.get_dayly_map())], id="graph-map-2", className="fullscreen-div"),
                    
                ], className="card-body"
            ),
            html.Div(html.Button('Full screen', id='map-btn-2', className="fullscreen btn btn-secondary"), 
                     className='d-block text-right card-footer')
        ],
        className='card'
    )

    tab_time_series = html.Div(
        [
            html.Div(
                [
                    "Noise for the last 15 Days",
                    html.Div(
                        [
                            html.Span("Select your station", className='pane-right-text'),
                            dcc.Dropdown(id="stations-selector", options=[{"label":x,"value":x} 
                                                               for x in time_series.stations], value='CAI 20 de Julio')
                        ],
                        className='btn-actions-pane-right'
                    )
                ],
                className='card-header'
            ),
            html.Div(
                [
                    html.P("Below you can see the different measurements of Noise for the last 15 days of data. \
                            Each line represents one of the different measures of noise",
                           className='gen-info'),
                    html.Div(
                        [
                           html.H5(id='selected-station'),
                           html.Div([dcc.Graph(id="time-series-15days")]),
                        ], className='container'
                    ),
                ], className="card-body"
            ),
            html.Div(
                [
                    "Evolution of Leq over time. Leq is the most common way to measure noise",
                ],
                className='card-header card-header-no-top'
            ),
            html.Div(
                [
                    html.P(
                        "Use the slider below the graph to select a time range. You can also use \
                        the buttons above the graph",
                        className='gen-info'),
                    html.Div(html.Div([dcc.Graph(id="time-series-figure")]), className='container'),
                    
                ], className="card-body"
            ),
            html.Div(
                [
                    "Distribution of noise during the day for each station",
                ],
                className='card-header card-header-no-top'
            ),
            html.Div(
                [
                    html.P(
                        "Here you can find information about different sensors located in the City. \
                        Use the dropdown to select a sensor of interest.",
                        className='gen-info'),
                    html.Div(html.Div([dcc.Graph(id='time-series-bar')]), className='container'),
                    
                ], className="card-body"
            ),
        ],
        className='card'
    )

    tab_predictions = html.Div(
        [
            html.Div(
                [
                    "Other graph",
                    html.Div(
                        [
                            html.Span("Select your station", className='pane-right-text'),
                            dcc.Dropdown(id="stations-predictions", options=[{"label":x,"value":x} 
                                                               for x in time_series.stations], value='CAI 20 de Julio')
                        ],
                        className='btn-actions-pane-right'
                    )
                ],
                className='card-header'
            ),
            html.Div(
                [
                    html.P("Feature still under construction...", className="gen-info"),
                ],
                className="card-body mt-3"
            ),
            html.Div(html.Button('Click here', className="btn btn-secondary"), 
                     className='d-block text-right card-footer')
        ],
        className='card'
    )
    
    tabs = dbc.Tabs(
        [
            dbc.Tab(tab_maps, label = " Maps "),
            dbc.Tab(tab_time_series, label = " Time series analysis "),
            dbc.Tab(tab_predictions, label=" Predictions "),
        ]
    )
    
    content = html.Div(
        [
            dbc.Row(project_info),
            dbc.Row(
                [
                    html.Div(tabs, className='k2-tabs-width')
                ],
                className='col-md-12 k2-team-container'
            )
        ],
        className='container'
    )
