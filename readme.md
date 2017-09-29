## Intro

A simple Pandas Data (draft version) Visualization module.

### Features
- Compatible with Python 2.X, hasn't been tested by Python 3.X.
- Only support up to three rows of headers so far.
- Support multiple group labels of one row.
- Support `Customizable` data displaying format.

## Usage 
###Sample:
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

###Result
Please access Microsoft One Drive <a href="https://1drv.ms/i/s!Ah0x1kN0ecCBgoQJuNMgXSttVdZdKQ">Sample Result</a> to see the result.


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