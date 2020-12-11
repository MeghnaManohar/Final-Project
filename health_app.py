# Import all the necessary packages needed
from bmi import *
import dash
import dash_table
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State


#Set the theme
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


#######################################################################################################################
# LAYOUT DESIGN

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#dbf3ff",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "22rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H1("The MP Health App", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Overview", href="/page-1", id="page-1-link"),
                dbc.NavLink("BMI Calculator", href="/page-2", id="page-2-link"),
                dbc.NavLink("Calorie Calculator", href="/page-3", id="page-3-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
#######################################################################################################################

#Build BMI Chart
bmi_card = dbc.Card(
    [
        dbc.CardImg(src = "https://files.prokerala.com/health/images/bmi-category.png"),
    ],
 body=True,
 style={"width": "40rem"},
)


#######################################################################################################################

# Build the results which will be displayed
results = html.Div(
    [
        dbc.ListGroup(
            [
                dbc.ListGroupItem("Your BMI:", color = "info"),
                dbc.ListGroupItem(id ='bmi-output'),
            ],
            horizontal=True,
            className="mb-2",
        ),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("To maintain your weight you need:", color="success"),
                dbc.ListGroupItem(id="maintain-output"),
                dbc.ListGroupItem("Kcal/day")
            ],
            horizontal=True,
            className="mb-2",
        ),

        dbc.ListGroup(
            [
                dbc.ListGroupItem("To lose .45 kg (1 lb) per week you need:", color = "primary" ),
                dbc.ListGroupItem(id="lose-output"),
                dbc.ListGroupItem("Kcal/day")
            ],
            horizontal= True,
            className="mb-2",
        ),

        dbc.ListGroup(
            [
                dbc.ListGroupItem("To gain .45 kg (1 lb) per week you need:", color = "danger"),
                dbc.ListGroupItem(id="gain-output"),
                dbc.ListGroupItem("Kcal/day")
            ],
            horizontal= True,
            className="mb-2",
        ),

    ]
)

#######################################################################################################################
#Build activity level
activity_level = dbc.FormGroup(
    [
        dbc.Label("Activity Level", html_for="activity-dropdown", width=2),
        dbc.Col(
            [
                dcc.Dropdown(
                    id="activity-dropdown",
                    placeholder="Select Activity Level",
                    style={"min-width": "250px"},
                    options=[
                        {'label': 'Baseline BMR', 'value': '0'},
                        {'label': "Sedentary", 'value': '1'},
                        {'label': "Lightly Active", 'value': '2'},
                        {'label': "Moderately Active", 'value': '3'},
                        {'label': "Very Active", 'value': '4'},
                        {'label': "Extra Active", 'value': '5'},
                    ],
                ),
            ],

            width=10,
        ),
    ],
    row=True,
)

#Build the age input
age = dbc.FormGroup(
    [
        dbc.Label("Age", html_for="age", width=2),
        dbc.Col(
            dbc.Input(id="age", placeholder="years", type='float', min=0),

            width=10,
        ),
    ],
    row=True,
)

# Build the weight input
weight = dbc.FormGroup(
    [
        dbc.Label("Weight", html_for="weight", width=2),
        dbc.Col(
            [
                dbc.Input(id="weight", placeholder='-', type='float', min=0),
            ],
            width = 6,
        ),
        dbc.Col(
            [
                dcc.Dropdown(
                    id="weight-dropdown",
                    placeholder="kg",
                    style={"min-width": "100px"},
                    options=[
                        {'label': 'kg', 'value': 'metric'},
                        {'label': 'lbs', 'value': 'imperial'},
                    ],
                ),
            ],

            width=4,
        ),
    ],
    row=True,
)


# Build the height input
height = dbc.FormGroup(
    [
        dbc.Label("Height", html_for="height", width=2),
        dbc.Col(
            [
                dbc.Input(id="height", placeholder='-', type='float', min = 0),
            ],
            width = 6,
        ),
        dbc.Col(
            [
                dcc.Dropdown(
                    id = "height-dropdown",
                    placeholder = "cm",
                    style={"min-width": "100px"},
                    options=[
                        {'label': 'cm', 'value': 'metric'},
                        {'label': 'inch', 'value': 'imperial'},
                        ],
                ),
            ],

            width=4,
        ),
    ],
    row=True,
)

#Build the sex input
sex = dbc.FormGroup(
    [
        dbc.Label("Sex", html_for="sex", width=2),
        dbc.Col(
            dbc.RadioItems(
                id="sex",
                options=[
                    {"label": "Male", "value": "m"},
                    {"label": "Female", "value": "f"},
                ],
            ),
            width=10,
        ),
    ],
    row=True,
)

#Build Inputs
inputs = dbc.Form(
    [
        sex, height, weight, age, activity_level,
    ],
)
#######################################################################################################################

#Tab-2 Content
tab2_BMI_content = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.H2("The BMI Calculator"),
            ),
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                html.H5("Enter your information", style={'font-weight': 'bold'}),
            )
        ),

        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            inputs,
                            dbc.Button(id='submit', n_clicks=0, children='Submit', color="success"),
                        ]

                    )
                ),
            ]
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                html.H5("Results", style={'font-weight': 'bold'}),
            )
        ),

        dbc.Row(
            dbc.Col(
                dbc.Card(
                    results
                )
            )
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                html.H5("BMI Chart", style={'font-weight': 'bold'}),
            )
        ),

        dbc.Row(
            dbc.Col(
                bmi_card
            )
        ),

    ]
)

#######################################################################################################################
#Tab-1 Content
tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P(
                "The MP Health App helps users live a healthier lifestyle! After obtaining information, "
                "Our app outputs the user's BMI, BMR, and suggests daily calories depending on whether you want to "
                "maintain/lose/gain weight. Learn about common exercises and create your own daily menu!"
                ),
            html.P(
                "How to Use: Just input your sex, weight, height, age, and activity levels (in metric system or in the "
                "imperial system) and the MP Health App will calculate your Body Mass Index (BMI) which you can crosscheck "
                "with the BMI Range Chart. We'll also calculate your Basal Metabloic Rate (BMR) "
                "which helps determine how many calories you should have daily. We've also included "
                "common exercises to help you figure out how to burn calories. "
                "Finally, in our last tab, you can search of food database and build a menu, noting "
                "the calories associated with the food. "
                ),
            html.P( 
                "Notes: Your BMR is calculated using the revised Harris-Benedict Equation.",
                
                className="card-text",
            ),
        ]
    )
)


#Tab-1 Content
tab1_overview_content = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H2("The BMI and Calorie Counter"),
            ),
        ),

        html.Br(),

        dbc.Row(
            dbc.Col(
                tab1_content
            )
        ),
    ]
)

#######################################################################################################################


# Content style for each page
content = html.Div(id="page-content", style=CONTENT_STYLE)

# Build Page layout
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return tab1_overview_content
    elif pathname == "/page-2":
        return tab2_BMI_content
    elif pathname == "/page-3":
        return html.P("Oh cool, this is page 3!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
#######################################################################################################################
##Backend
#Test
@pytest.mark.parametrize('height, weight, age, sex, activity, h_system, w_system',
                         [
                             (180, 60, 22,'m', 2, 'metric', 'metric'),
                             (60.1, 118.9, 'f',22, 3, 'imperial', 'imperial'),
                         ])
#Calculator
@app.callback(
    [Output("bmi-output", "children"),
     Output("maintain-output", "children"),
     Output('lose-output', "children"),
     Output("gain-output", "children")],

    [Input('submit', 'n_clicks')],

    [State("height", "value"), State("weight", "value"), State("age", "value"),
     State("sex", "value"), State("activity-dropdown", "value"),
     State("height-dropdown", "value"),
     State("weight-dropdown", "value")]
)

def compute(nclicks, height, weight, age, sex, activity, h_system, w_system):
    if (height == None or weight ==None or age ==None or sex==None or activity == None):
        return None, None, None, None
    #Use function from bmi.py to calculate values
    return calculator(float(height), float(weight), float(age), str(sex), int(activity), str(h_system), str(w_system))


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader = False)