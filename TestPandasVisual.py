from PandasVisual import PandasVisual, StringFormatter, FloatFormatter
import pandas as pd
import numpy as np
#Test Case
if __name__ == '__main__':
    raw_data = {
        'id': ['A1', 'A2', 'A3', 'A4', 'A5'],
        'first_name': ['Tina', 'Jake', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Mill', 'Jacobson', "Jacobson", 'Mill', 'Mill'], 
        'department': ['HW', 'HW', "HW", 'SW', 'SW'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [423163, 245778, 31345234, 57978, 6234512],
        'postTestScore': [25000, 94000, 57, 62, 70]}
    df = pd.DataFrame(raw_data, columns = ['id', 'first_name', 'last_name', 'department', 'age', 'preTestScore', 'postTestScore'])

    #first table
    pv1 = PandasVisual(df, 'Test Pandas Visual 1')
    pv1.setColumnFormat( {0: StringFormatter('{0}'), 1: StringFormatter('{0}'), 2: FloatFormatter('{:.2%}'), 3:FloatFormatter('{:,.0f}'), 4:FloatFormatter('{:.2%}')} )

    #second table
    df_summary =  df.groupby(['last_name', 'department']).agg({'age': 'sum', 'preTestScore': 'mean','postTestScore': 'sum'})
    pv2 = PandasVisual(df_summary, 'Test Pandas Visual 2')
    pv2.setColumnFormat( {0: StringFormatter('{0}'), 1: StringFormatter('{:.2%}'), 2: FloatFormatter('{:,.0f}') } )

    #third table
    #df_pivot = df.pivot(index=['first_name','id'], columns='department', values='age')
    df_pivot = pd.pivot_table(df, values = ['age', 'preTestScore'], index=['first_name','last_name'], columns = 'department')
    df_pivot = df_pivot.fillna(0)
    pv3 = PandasVisual(df_pivot, 'Test Pandas Visual 3')
    pv3.setColumnFormat( {0: StringFormatter('{0}') } )

    with open('test_pandas_visual.html', 'wb') as file_object:
        file_object.write('')
    with open('test_pandas_visual.html', 'wb') as file_object:
        file_object.write(pv1.to_html() + pv2.to_html() + pv3.to_html())