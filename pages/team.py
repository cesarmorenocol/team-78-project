import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Team Page
class TeamPage():
    team_info = html.Div(
        [
            html.H2("Meet the Team", className='k2-title'),
            html.P(
                "We are Team #78 from Data Science 4 All: Colombia - 3rd edition ",
                className='gen-info',
            ),
            html.Hr(className="my-2")
        ],
        className='col-md-12'
    )

    content = html.Div(
        [
            dbc.Row(team_info),
            dbc.Row([
                html.Div([
                    html.Div(className='profile-image bd-placeholder-img rounded-circle profile-mario'),
                    html.H2("Mario Alejandro Benítez", className='k2-title'),
                    html.P("Mechanics Engineer  - MSc Mechanics Engineering", className='k2-profile')
                    ],
                    className='col-md-4 text-center'
                ),
                html.Div([
                    html.Div(className='profile-image bd-placeholder-img rounded-circle profile-hernan'),
                    html.H2("Hernán David Torres", className='k2-title'),
                    html.P("Statistic - Licensed at German Philology", className='k2-profile')
                    ],
                    className='col-md-4 text-center'
                ),
                html.Div([
                    html.Div(className='profile-image bd-placeholder-img rounded-circle profile-adriana'),
                    html.H2("Luz Adriana Moyano", className='k2-title'),
                    html.P("Telematics Engineer", className='k2-profile')
                    ],
                    className='col-md-4 text-center'
                ),
            ], className='k2-team-container'),
            dbc.Row([
                html.Div([
                    html.Div(className='profile-image bd-placeholder-img rounded-circle profile-david'),
                    html.H2("David Pinzon Marroquin", className='k2-title'),
                    html.P("Industrial Engineer - MSc Operations Research", className='k2-profile')
                    ],
                    className='col-md-4 text-center'
                ),
                html.Div([
                    html.Div(className='profile-image bd-placeholder-img rounded-circle profile-fidel'),
                    html.H2("Fidel Olarte", className='k2-title'),
                    html.P("Industrial Engineer - MSc Industrial Engineering Candidate", className='k2-profile')
                    ],
                    className='col-md-4 text-center'
                ),
                html.Div([
                    html.Div(className='profile-image bd-placeholder-img rounded-circle profile-cesar'),
                    html.H2("Cesar Augusto Moreno", className='k2-title'),
                    html.P("Automation Engineer - MSc Business & Information Technologies", className='k2-profile')
                    ],
                    className='col-md-4 text-center'
                ),
            ]),
        ],
        className='container'
    )