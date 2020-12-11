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
                columns=[{"name": i, "id": i, "deletable": True,} for i in df.columns],
                data=df.to_dict('records'),
                style_cell = {
                            'margin-left': 'auto',
                            'margin-right': 'auto',
                            'padding-left': '20px',
                            'whiteSpace': 'normal',
                            'height': 'auto',
                            },
                style_header = {
                            'textAlign' : 'center',
                            'backgroundColor': ' pink',
                            'fontWeight': 'bold',
                            'color': 'white',
                            },
                style_data = {
                            'textAlign' : 'left',
                            },
                style_cell_conditional=[
                              {'if': {'column_id': 'Activity (1 hour)'},
                              'width': '30%'}
                              ],
                filter_action = "native",
                sort_action="native",
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
                              'padding-left': '20px',
                              'whiteSpace': 'normal',
                              'height': 'auto',
                              },
                style_header = {
                                'backgroundColor': 'green',
                                'fontWeight': 'bold',
                                'color': 'white',
                                },
                style_cell_conditional=[
                             {'if': {'column_id':'Food Components'},
                              'width': '30%'}
                             ],
                sort_action="native",
                fixed_rows={'headers': True},
                style_table={'height': '350px'},
            )
        )
    ],
    body=True
)
