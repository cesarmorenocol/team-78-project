import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

class HomePage():
    
    home_info = html.Div(
        [
            html.H2("About the Project", className='k2-title'),
            html.P(
                "General information about the client and the project",
                className='gen-info',
            ),
            html.Hr(className="my-2")
        ],
        className='col-md-12'
    )

    content = html.Div(
        [
            dbc.Row(home_info),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [

                                html.P("K2 Ingeniería, is a Colombian company, established in 1999, that integrates "+
                                       "experience in different areas of environmental, civil, mechanical, electronic "+
                                       "and systems engineering to offer a broad portfolio of consulting, monitoring "+
                                       "and technology integration. K2 Ingeniería, has specialized in the environmental "+
                                       "area, sector in the one that develops outstanding projects nationwide."),

                                html.P("Noise is an important variable that affects city planning, "+
                                       "wild life, and human health. K2 has many stations which are "+
                                       "used to measure noise and in some cases other environmental variables. "),

                                html.P("At this moment K2  is interested in understanding and  predicting noise \
                                based on that information. "),
                            ]
                        ),
                        className='col-md-6'
                    ),
                    dbc.Col(
                        html.Div(
                            [
                                html.P("The monitoring of environmental variables in real time (noise, meteorology,\
                                        air quality, water, etc.) from automatic stations or even from specific \
                                        campaigns usually generates a high volume of data that is normally difficult \
                                        to consult and is rarely used more beyond what is strictly required."),

                                html.Div(
                                    [
                                        #html.Img(src=app.get_asset_url("noise.png"), height="180px", className="center"),
                                        html.Div(className='noise')
                                    ], style={'textAlign': 'center'}
                                ),
                            ]
                        ),
                        className='col-md-6'
                    )
                ], className='k2-team-container'
            )
        ],
        className='container'
    )
