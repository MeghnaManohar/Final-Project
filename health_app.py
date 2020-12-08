from bmi import *
from bmi2 import *
import dash
import dash_table
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from calorie import *
from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])


#Gather Loan Info from User
inputs = dbc.Card(
    [
        html.H5(children = "Enter your Information:"),
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
                        dbc.Label("Height"),
                        dbc.Input(id="height", placeholder='cm', type='number', min = 0)
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
                        dbc.Label("Weight"),
                        dbc.Input(id="weight", placeholder='kg', type='number', min = 0),
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
                        dbc.Label("Age"),
                        dbc.Input(id = "age", placeholder = "years", type = 'number', min = 0),
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
        html.H5(children = "BMI Range Chart:"),
        dbc.CardImg(src="data:image/png;base64,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", bottom=True),
    ],
 body=True
)



#Results Section 
results = dbc.Card(
    [
        html.H5(children = "Results:"),
        dbc.FormGroup(
            [
                    dbc.Label("Your BMI:"),
                    html.Div(id="output"),    
                    dbc.Label("To maintain your weight you need:"),
                    html.Div(id="output0"),
                    dbc.Label("To lose 1 kg per week you need:"),
                    html.Div(id="output1"),
                    dbc.Label("To gain 1 kg per week you need:"),
                    html.Div(id="output2")
            ],
        )
    ],
    body=True
)

#Display Calorie Counter container
counter = dbc.Card(
    [
        html.H5(children="Calorie Counter and Food Calculator"),

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
                html.H2(children = "Health App")
            )
        ),
        #BMI
        dbc.Row(
            [
                dbc.Col(inputs, md=4),
                dbc.Col(results, md = 4),
            ],
            align="left",
        ),
        html.Br(),

        dbc.Row (
            dbc.Col(bmi_card, md =4),
        ),
        html.Br(),

        dbc.Row(
            dbc.Col(counter),
            dbc.Col(table)
        )
    ],
    id="main-container",
    style={"display": "flex", "flex-direction": "column"},
    fluid=True
)

#Backend 
@app.callback(
    [Output("output", "children"), Output("output0", "children"), Output('output1', "children"), Output("output2", "children")],
    [Input('submit', 'n_clicks')],
    [State("height", "value"), State("weight", "value"), State("age", "value"),
     State("sex", "value"), State("activity-dropdown", "value")]
)

def compute(nclicks, height, weight, age, sex, activity):
    if (height ==None or weight ==None or age ==None or sex==None or activity == None):
        return None, None, None, None 
    bmi = bmr = bmr_lose = bmr_gain = 0
    print(nclicks)
    print(height)
    print(weight)
    print(age)
    print(sex)
    print(activity)
    #Use function from bmi.py to calculate values
    calculator()
    height = height
    weight = weight
    age = age
    sex = sex
    activity = activity
    return bmi, bmr, bmr_lose, bmr_gain




if __name__ == '__main__':
    app.run_server(debug=True, use_reloader = False)
