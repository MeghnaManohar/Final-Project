from bmi import *
import dash
import dash_table
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])

#Gather Info from User
inputs = dbc.Card(
    [
        html.H5(children = "Enter your Information:",
                style={'font-weight': 'bold'}
                ),
        dbc.FormGroup(
            [
                dbc.RadioItems(
                    options=[
                        {'label': 'Metric System (cm & kg)', 'value': "metric"},
                        {'label': 'Imperial System (in & lb)', 'value': "imperial"},
                    ],
                    id= "system", 
                    inline = True,
                    switch = True,
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
                    id= "sex", 
                    inline = True,
                ),
            ],
        ),
        dbc.Form(
            [
                dbc.FormGroup(
                    [
                        dbc.Label("Height: "),
                        dbc.Input(id="height", placeholder='cms or inches', type='float', min = 0)
                    ],
                    className = 'mr-3',
                ),
            ],
            inline = True,
        ),
        dbc.Form(
            [
                dbc.FormGroup(
                    [
                        dbc.Label("Weight: "),
                        dbc.Input(id="weight", placeholder='kgs or lbs', type='float', min = 0),
                    ],
                    className = 'mr-3',
                ),
            ],
            inline = True,
        ),
        dbc.Form(
            [
                dbc.FormGroup(
                    [
                        dbc.Label("Age: "),
                        dbc.Input(id = "age", placeholder = "years", type = 'float', min = 0),
                    ],
                    className = 'mr-3',
                ),  
            ],
            inline = True,
        ),
        dcc.Dropdown(
            id = "activity-dropdown",
            placeholder = "Select Activity Level",
            options=[
                {'label': 'Baseline BMR', 'value': '0'},
                {'label': "Little to no exercise", 'value': '1'},
                {'label':"Light Exercise", 'value': '2'},
                {'label':"Moderate Exercise", 'value': '3'},
                {'label':"Heavy Exercise", 'value': '4'},
                {'label':"Very Heavy Exercise", 'value': '5'},
                ],
            ), 
        dbc.Button(id='submit', n_clicks=0, children='Submit', color = "success",)
    ],
   body=True
)

#BMI Chart
bmi_card = dbc.Card(
    [
        dbc.CardImg(src = "https://files.prokerala.com/health/images/bmi-category.png"),
    ],
 body=True,
 style={"width": "25rem"},
)
#BMI and BMR Output Section
results = dbc.Card(
    [
        html.H5(children = "Results:", style={'font-weight': 'bold'}),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("Your BMI:", color = "info"),
                dbc.ListGroupItem(id ='bmi-output')
            ],
            horizontal=True,
        ),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("To maintain your weight you need:", color = "success"),
                dbc.ListGroupItem(id="maintain-output"),
                dbc.ListGroupItem("Kcal/day")
            ],
            horizontal= True,
        ),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("To lose 1 kg (2.2 lbs) per week you need:", color = "secondary" ),
                dbc.ListGroupItem(id="lose-output"),
                dbc.ListGroupItem("Kcal/day")
            ],
            horizontal= True,
        ),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("To gain 1 kg (2.2 lbs) per week you need:", color = "danger"),
                dbc.ListGroupItem(id="gain-output"),
                dbc.ListGroupItem("Kcal/day")
            ],
            horizontal= True,
        ),
    ],
    body=True
)
#Data for Exercise Table 
df = pd.read_csv('exercise_data.csv')
#Exercise Table
exercise_card = dbc.Card(
    [
        dbc.Col(html.H5(children = "Calories Burned from Common Exercises:", 
                        style={'font-weight': 'bold'})
                ),
        dbc.Col(
            dash_table.DataTable(
                id='exercise-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                style_cell = {'textAlign' : 'left',
                              'margin-left': 'auto',
                              'margin-right': 'auto',
                              'padding-left': '20px'
                              },
                style_header = {
                                'backgroundColor': ' pink',
                                'fontWeight': 'bold',
                                'color': 'white',
                                },
                style_cell_conditional=[
                     {'if': {'column_id': 'Activity (1 hour)'},
                      'width': '30%'},
                ],
                filter_action = "native",
                page_size = 25,
                fixed_rows={'headers': True},
                style_table={'height': '350px'},
            )
        )
    ],
    body=True
)

#Data for Energy Table 
df = pd.read_csv('energy_data.csv')
#Energy Table
energy_card = dbc.Card(
    [
        dbc.Col(html.H5(children = "Energy from Common Food Components:", 
                        style={'font-weight': 'bold'})),
        dbc.Col(
            dash_table.DataTable(
                id='energy-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                style_cell = {'textAlign' : 'left',
                              'margin-left': 'auto',
                              'margin-right': 'auto',
                              'padding-left': '20px'
                              },
                style_header = {
                                'backgroundColor': 'pink',
                                'fontWeight': 'bold',
                                'color': 'white',
                                },
                style_cell_conditional=[
                     {'if': {'column_id':'Food Components'},
                      'width': '30%'}
                     ],
                fixed_rows={'headers': True},
                style_table={'height': '350px'},
            )
        )
    ],
    body=True
)

#Data for table
foodData_df = pd.read_csv('Food_Display_Table.csv')
#Display Calorie Counter container
counter = dbc.Card(
    [
        html.H5(children="Calorie Counter and Food Calculator", style={'font-weight': 'bold'}),

        html.Br(),

        dbc.FormGroup(
            [
                dbc.Label(html.H3("Search")),
                    dcc.Dropdown(placeholder="e.g., apples, Sangria,...",
                                 value="Choose a destination city",
                                 id="counter",
                                 options=[{"label": col, "value": col} for col in foodData_df['Display_Name'].unique()],
                                 ),
                dbc.FormText("Tip: do not include restaurant names "),

                dbc.Table()
            ]
        ),
        dbc.Button("Submit", id='submitC', n_clicks=0, color="success", )
    ],
    body=True
)

table = dbc.Table(id = "tableC", striped=True, bordered=True, hover=True)
#App Layout
app.layout = dbc.Container(
    [
        #Title
        dbc.Row(
            dbc.Col(
                html.H2(children = "Health App",
                        style={'font-weight': 'bold'})
            )
        ), 
        #Inputs, BMI, BMR
        dbc.Row(
            [
                dbc.Col(inputs, md=4),
                dbc.Col(results, md = 4),
                dbc.Col(bmi_card, md =4),     
            ],
            align= "right",
        ),
        #Exercise and Energy
        dbc.Row(
            [
                dbc.Col(exercise_card, md = 6),
                dbc.Col(energy_card, md = 6)
            ],
            align = "left",  
        ),
        #Food Stuff
        dbc.Row(
            [
            dbc.Col(counter),
            dbc.Col(table)
            ],
        )
    ],
    id="main-container",
    style={"display": "flex", "flex-direction": "column"},
    fluid=True
)

##Backend 
#Calc
@app.callback(
    [Output("bmi-output", "children"), Output("maintain-output", "children"), Output('lose-output', "children"), Output("gain-output", "children")],
    [Input('submit', 'n_clicks')],
    [State("height", "value"), State("weight", "value"), State("age", "value"),
      State("sex", "value"), State("activity-dropdown", "value"), State("system", "value")]
)

def compute(nclicks, height, weight, age, sex, activity, system):
    if (height ==None or weight ==None or age ==None or sex==None or activity == None):
        return None, None, None, None 
    #Use function from bmi.py to calculate values 
    if system ==  "metric":
        return calculator(float(height), float(weight), float(age), str(sex), int(activity))
    elif system == "imperial":
        return calculator_imperial(float(height), float(weight), float(age), str(sex), int(activity))
 
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader = False)
