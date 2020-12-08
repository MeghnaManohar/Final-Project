from bmi import *
from data import *
import dash
import dash_table
import dash_table as dt
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])

# Gather Info from User
inputs = dbc.Card(
    [
        html.H5(children="Enter your Information:",
                style={'font-weight': 'bold'}
                ),
        dbc.FormGroup(
            [
                dbc.RadioItems(
                    options=[
                        {'label': 'Metric System (cm & kg)', 'value': "metric"},
                        {'label': 'Imperial System (in & lb)', 'value': "imperial"},
                    ],
                    id="system",
                    inline=True,
                    switch=True,
                ),
            ],
        ),
        dbc.FormGroup(
            [
                dbc.RadioItems(
                    options=[
                        {'label': 'Male', 'value': "m"},
                        {'label': 'Female', 'value': 'f'},
                    ],
                    id="sex",
                    inline=True,
                ),
            ],
        ),
        dbc.Form(
            [
                dbc.FormGroup(
                    [
                        dbc.Label("Height: "),
                        dbc.Input(id="height", placeholder='cms or inches', type='float', min=0)
                    ],
                    className='mr-3',
                ),
            ],
            inline=True,
        ),
        dbc.Form(
            [
                dbc.FormGroup(
                    [
                        dbc.Label("Weight: "),
                        dbc.Input(id="weight", placeholder='kgs or lbs', type='float', min=0),
                    ],
                    className='mr-3',
                ),
            ],
            inline=True,
        ),
        dbc.Form(
            [
                dbc.FormGroup(
                    [
                        dbc.Label("Age: "),
                        dbc.Input(id="age", placeholder="years", type='float', min=0),
                    ],
                    className='mr-3',
                ),
            ],
            inline=True,
        ),
        dcc.Dropdown(
            id="activity-dropdown",
            placeholder="Select Activity Level",
            options=[
                {'label': 'Baseline BMR', 'value': '0'},
                {'label': "Little to no exercise", 'value': '1'},
                {'label': "Light Exercise", 'value': '2'},
                {'label': "Moderate Exercise", 'value': '3'},
                {'label': "Heavy Exercise", 'value': '4'},
                {'label': "Very Heavy Exercise", 'value': '5'},
            ],
        ),
        dbc.Button(id='submit', n_clicks=0, children='Submit', color="success", )
    ],
    body=True
)

# BMI Chart
bmi_card = dbc.Card(
    [
        dbc.CardImg(src="https://files.prokerala.com/health/images/bmi-category.png"),
    ],
    body=True,
    style={"width": "25rem"},
)
# BMI and BMR Output Section
results = dbc.Card(
    [
        html.H5(children="Results:", style={'font-weight': 'bold'}),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("Your BMI:", color="info"),
                dbc.ListGroupItem(id='bmi-output')
            ],
            horizontal=True,
        ),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("To maintain your weight you need:", color="success"),
                dbc.ListGroupItem(id="maintain-output"),
                dbc.ListGroupItem("Kcal/day")
            ],
            horizontal=True,
        ),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("To lose 1 kg (2.2 lbs) per week you need:", color="secondary"),
                dbc.ListGroupItem(id="lose-output"),
                dbc.ListGroupItem("Kcal/day")
            ],
            horizontal=True,
        ),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("To gain 1 kg (2.2 lbs) per week you need:", color="danger"),
                dbc.ListGroupItem(id="gain-output"),
                dbc.ListGroupItem("Kcal/day")
            ],
            horizontal=True,
        ),
    ],
    body=True
)

# Exercise Table
exercise_card = dbc.Card(
    [
        dbc.Col(html.H5(children="Calories Burned from Common Exercises:",
                        style={'font-weight': 'bold'})
                ),
        dbc.Col(
            dash_table.DataTable(
                id='exercise-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                style_cell={'textAlign': 'left',
                            'margin-left': 'auto',
                            'margin-right': 'auto',
                            'padding-left': '20px'
                            },
                style_header={
                    'backgroundColor': ' pink',
                    'fontWeight': 'bold',
                    'color': 'white',
                },
                style_cell_conditional=[
                    {'if': {'column_id': 'Activity (1 hour)'},
                     'width': '30%'},
                ],
                filter_action="native",
                page_size=25,
                fixed_rows={'headers': True},
                style_table={'height': '350px'},
            )
        )
    ],
    body=True
)


# Energy Table
energy_card = dbc.Card(
    [
        dbc.Col(html.H5(children="Energy from Common Food Components:",
                        style={'font-weight': 'bold'})),
        dbc.Col(
            dash_table.DataTable(
                id='energy-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                style_cell={'textAlign': 'left',
                            'margin-left': 'auto',
                            'margin-right': 'auto',
                            'padding-left': '20px'
                            },
                style_header={
                    'backgroundColor': 'pink',
                    'fontWeight': 'bold',
                    'color': 'white',
                },
                style_cell_conditional=[
                    {'if': {'column_id': 'Food Components'},
                     'width': '30%'}
                ],
                fixed_rows={'headers': True},
                style_table={'height': '350px'},
            )
        )
    ],
    body=True
)

# Display Calorie Counter container
counter = dbc.Card(
    [
        html.H2(children="Calorie Counter and Food Calculator", style={'font-weight': 'bold'}),

        html.Br(),

        dbc.FormGroup(
            [
                dbc.Label(html.H5("Search")),
                dcc.Dropdown(placeholder="e.g., apples, Sangria,...",
                             # value="Choose a destination city",
                             id="counter",
                             options=[{"label": col, "value": col} for col in foodData_df['Display_Name'].unique()],
                             ),
                dbc.FormText("Tip: do not include restaurant names "),

            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label(html.H5("Portion Type")),
                dcc.Dropdown(placeholder="e.g., apples, Sangria,...",
                             value="Choose portion type",
                             id="portion-type",
                             ),
            ]

        ),

        dbc.Button("Submit", id='submitC', n_clicks=0, color="success"),

        html.Br(),

        dbc.Button("Add New", id='submitN', n_clicks=0, color="primary")

    ],
    body=True
)

table = dbc.Card(
    [
        dbc.Col(html.H3("Calorie Components:")),

        dbc.Col(
            html.Div(
                id='calorie-table',
            )
        )
    ]
)

# App Layout
app.layout = dbc.Container(
    [
        # Title
        dbc.Row(
            dbc.Col(
                html.H2(children="Health App",
                        style={'font-weight': 'bold'})
            )
        ),

        html.Br(),
        # Inputs, BMI, BMR
        dbc.Row(
            [
                dbc.Col(inputs, md=4),
                dbc.Col(results, md=4),
                dbc.Col(bmi_card, md=4),
            ],
            align="right",
        ),

        html.Br(),

        # Exercise and Energy
        dbc.Row(
            [
                dbc.Col(exercise_card, md=6),
                dbc.Col(energy_card, md=6)
            ],
            align="left",
        ),
        html.Br(),

        # Food Stuff
        dbc.Row(
            [
                dbc.Col(counter),
            ],
        ),

        html.Br(),
        #Calorie table
        dbc.Row(
            [
                dbc.Col(table)
            ]
        ),

        html.Br(),
    ],
    id="main-container",
    style={"display": "flex", "flex-direction": "column"},
    fluid=True
)

#Layout for hidden display
# app.layout = dbc.Container(
#     [
#         dbc.Row(
#             dbc.Col(
#                 html.H2(children="Health App",
#                         style={'font-weight': 'bold'})
#             )
#         ),
#
#     ]
# )


##Backend
# Calc
@app.callback(
    [Output("bmi-output", "children"), Output("maintain-output", "children"), Output('lose-output', "children"),
     Output("gain-output", "children")],
    [Input('submit', 'n_clicks')],
    [State("height", "value"), State("weight", "value"), State("age", "value"),
     State("sex", "value"), State("activity-dropdown", "value"), State("system", "value")]
)
def compute(nclicks, height, weight, age, sex, activity, system):
    if (height == None or weight == None or age == None or sex == None or activity == None):
        return None, None, None, None
        # Use function from bmi.py to calculate values
    if system == "metric":
        return calculator(float(height), float(weight), float(age), str(sex), int(activity))
    elif system == "imperial":
        return calculator_imperial(float(height), float(weight), float(age), str(sex), int(activity))


# Second dropdown menu to selection portion type
@app.callback(
    dash.dependencies.Output("portion-type", "options"),
    Input(component_id='counter', component_property='value'),
)
def update_calorie_portion(search_value):
    x = foodData_df[foodData_df["Display_Name"] == search_value]
    return [{"label": col, "value": col} for col in x['Portion_Display_Name'].unique()]


@app.callback(
    Output("calorie-table", "children"),
    Input("submitC", "n_clicks"),
    [State("counter", "value"),
     State("portion-type", "value")]
)
def update_dataTable(nclicksC, food, portion):
    if nclicksC:
        food_df = foodData_df[foodData_df["Display_Name"] == food]
        food_df = food_df[food_df["Portion_Display_Name"] == portion]
        food_df = food_df.loc[:, (food_df != 0).any(axis=0)]
        data = food_df.to_dict('records')
        columns = [{"name": i, "id": i, } for i in food_df.columns]

        return dt.DataTable(data=data, columns=columns,
                            style_cell = {'textAlign': 'left',
                                          'margin-left': 'auto',
                                          'margin-right': 'auto',
                                          'padding-left': '20px'
                                          },
                            style_header = {'backgroundColor': 'pink',
                                            'fontWeight': 'bold',
                                                'color': 'white',
                                            },
                            style_table={'overflowX': 'scroll'}

        )



if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
