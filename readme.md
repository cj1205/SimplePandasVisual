## Intro

A simple Pandas Data (draft version) Visualization module.

### Features
- Compatible with Python 2.X, hasn't been tested by Python 3.X.
- Only support up to three rows of headers so far.
- Support multiple group labels of one row.
- Support `Customizable` data displaying format.

## Usage 
####Sample:
```
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
```
####Result
<div style="display:inline-block;">
<h2>Test Pandas Visual 1</h2><table border="1" style="border-collapse: collapse;width: 100%;"><tr><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">None</th><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">id</th><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">first_name</th><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">last_name</th><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">department</th><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">age</th><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">preTestScore</th><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">postTestScore</th></tr><tr><th style="background-color: #FFED97;color: blue;text-align: center;padding: 8px;">0</th><td style="background-color: white;text-align: left;padding: 8px;">A1</td><td style="background-color: white;text-align: left;padding: 8px;">Tina</td><td style="background-color: white;text-align: left;padding: 8px;">Mill</td><td style="background-color: white;text-align: left;padding: 8px;">HW</td><td style="background-color: white;text-align: left;padding: 8px;">4200.00%</td><td style="background-color: white;text-align: left;padding: 8px;">423163</td><td style="background-color: white;text-align: left;padding: 8px;">25000</td></tr><tr style="background-color: #f2f2f2"><th style="background-color: #D3FF93;color: blue;text-align: center;padding: 8px;">1</th><td style="background-color: white;text-align: left;padding: 8px;">A2</td><td style="background-color: white;text-align: left;padding: 8px;">Jake</td><td style="background-color: white;text-align: left;padding: 8px;">Jacobson</td><td style="background-color: white;text-align: left;padding: 8px;">HW</td><td style="background-color: white;text-align: left;padding: 8px;">5200.00%</td><td style="background-color: white;text-align: left;padding: 8px;">245778</td><td style="background-color: white;text-align: left;padding: 8px;">94000</td></tr><tr><th style="background-color: #B3D9D9;color: blue;text-align: center;padding: 8px;">2</th><td style="background-color: white;text-align: left;padding: 8px;">A3</td><td style="background-color: white;text-align: left;padding: 8px;">Tina</td><td style="background-color: white;text-align: left;padding: 8px;">Jacobson</td><td style="background-color: white;text-align: left;padding: 8px;">HW</td><td style="background-color: white;text-align: left;padding: 8px;">3600.00%</td><td style="background-color: white;text-align: left;padding: 8px;">31345234</td><td style="background-color: white;text-align: left;padding: 8px;">57</td></tr><tr style="background-color: #f2f2f2"><th style="background-color: #FFED97;color: blue;text-align: center;padding: 8px;">3</th><td style="background-color: white;text-align: left;padding: 8px;">A4</td><td style="background-color: white;text-align: left;padding: 8px;">Jake</td><td style="background-color: white;text-align: left;padding: 8px;">Mill</td><td style="background-color: white;text-align: left;padding: 8px;">SW</td><td style="background-color: white;text-align: left;padding: 8px;">2400.00%</td><td style="background-color: white;text-align: left;padding: 8px;">57978</td><td style="background-color: white;text-align: left;padding: 8px;">62</td></tr><tr><th style="background-color: #D3FF93;color: blue;text-align: center;padding: 8px;">4</th><td style="background-color: white;text-align: left;padding: 8px;">A5</td><td style="background-color: white;text-align: left;padding: 8px;">Amy</td><td style="background-color: white;text-align: left;padding: 8px;">Mill</td><td style="background-color: white;text-align: left;padding: 8px;">SW</td><td style="background-color: white;text-align: left;padding: 8px;">7300.00%</td><td style="background-color: white;text-align: left;padding: 8px;">6234512</td><td style="background-color: white;text-align: left;padding: 8px;">70</td></tr></table><h2>Test Pandas Visual 2</h2><table border="1" style="border-collapse: collapse;width: 100%;"><tr><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">last_name</th><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">department</th><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">age</th><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">postTestScore</th><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">preTestScore</th></tr><tr><th style="background-color: #FFED97;color: blue;text-align: center;padding: 8px;">Jacobson</th><th style="background-color: #c0d16e;color: blue;text-align: center;padding: 8px;">HW</th><td style="background-color: white;text-align: left;padding: 8px;">88</td><td style="background-color: white;text-align: left;padding: 8px;">9405700.00%</td><td style="background-color: white;text-align: left;padding: 8px;">15,795,506</td></tr><tr style="background-color: #f2f2f2"><th style="background-color: #D3FF93;color: blue;text-align: center;padding: 8px;">Mill</th><th style="background-color: #c0d16e;color: blue;text-align: center;padding: 8px;">HW</th><td style="background-color: white;text-align: left;padding: 8px;">42</td><td style="background-color: white;text-align: left;padding: 8px;">2500000.00%</td><td style="background-color: white;text-align: left;padding: 8px;">423,163</td></tr><tr><th style="background-color: #D3FF93;color: blue;text-align: center;padding: 8px;">Mill</th><th style="background-color: #6ba377;color: blue;text-align: center;padding: 8px;">SW</th><td style="background-color: white;text-align: left;padding: 8px;">97</td><td style="background-color: white;text-align: left;padding: 8px;">13200.00%</td><td style="background-color: white;text-align: left;padding: 8px;">3,146,245</td></tr></table><h2>Test Pandas Visual 3</h2><table border="1" style="border-collapse: collapse;width: 100%;"><tr><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;" rowspan="2">first_name</th><th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;" rowspan="2">last_name</th><th style="background-color: #b54641;color: black;text-align: center;padding: 8px;" colspan="2">age</th><th style="background-color: #bc56b9;color: black;text-align: center;padding: 8px;" colspan="2">preTestScore</th></tr><tr><th style="background-color: #3ddb99;color: black;text-align: center;padding: 8px;" colspan="1">HW</th><th style="background-color: #66ba9c;color: black;text-align: center;padding: 8px;" colspan="1">SW</th><th style="background-color: #3ddb99;color: black;text-align: center;padding: 8px;" colspan="1">HW</th><th style="background-color: #66ba9c;color: black;text-align: center;padding: 8px;" colspan="1">SW</th></tr><tr><th style="background-color: #FFED97;color: blue;text-align: center;padding: 8px;">Amy</th><th style="background-color: #c8d32e;color: blue;text-align: center;padding: 8px;">Mill</th><td style="background-color: white;text-align: left;padding: 8px;">0.0</td><td style="background-color: white;text-align: left;padding: 8px;">73.0</td><td style="background-color: white;text-align: left;padding: 8px;">0.0</td><td style="background-color: white;text-align: left;padding: 8px;">6234512.0</td></tr><tr style="background-color: #f2f2f2"><th style="background-color: #D3FF93;color: blue;text-align: center;padding: 8px;">Jake</th><th style="background-color: #e0d2ef;color: blue;text-align: center;padding: 8px;">Jacobson</th><td style="background-color: white;text-align: left;padding: 8px;">52.0</td><td style="background-color: white;text-align: left;padding: 8px;">0.0</td><td style="background-color: white;text-align: left;padding: 8px;">245778.0</td><td style="background-color: white;text-align: left;padding: 8px;">0.0</td></tr><tr><th style="background-color: #D3FF93;color: blue;text-align: center;padding: 8px;">Jake</th><th style="background-color: #c8d32e;color: blue;text-align: center;padding: 8px;">Mill</th><td style="background-color: white;text-align: left;padding: 8px;">0.0</td><td style="background-color: white;text-align: left;padding: 8px;">24.0</td><td style="background-color: white;text-align: left;padding: 8px;">0.0</td><td style="background-color: white;text-align: left;padding: 8px;">57978.0</td></tr><tr style="background-color: #f2f2f2"><th style="background-color: #B3D9D9;color: blue;text-align: center;padding: 8px;">Tina</th><th style="background-color: #e0d2ef;color: blue;text-align: center;padding: 8px;">Jacobson</th><td style="background-color: white;text-align: left;padding: 8px;">36.0</td><td style="background-color: white;text-align: left;padding: 8px;">0.0</td><td style="background-color: white;text-align: left;padding: 8px;">31345234.0</td><td style="background-color: white;text-align: left;padding: 8px;">0.0</td></tr><tr><th style="background-color: #B3D9D9;color: blue;text-align: center;padding: 8px;">Tina</th><th style="background-color: #c8d32e;color: blue;text-align: center;padding: 8px;">Mill</th><td style="background-color: white;text-align: left;padding: 8px;">42.0</td><td style="background-color: white;text-align: left;padding: 8px;">0.0</td><td style="background-color: white;text-align: left;padding: 8px;">423163.0</td><td style="background-color: white;text-align: left;padding: 8px;">0.0</td></tr></table>
</div>
## Licence
The MIT License (MIT)

Copyright (c) 2016 mamboer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.