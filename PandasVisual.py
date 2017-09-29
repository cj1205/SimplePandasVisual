import pandas as pd
import numpy as np
import re
import locale
import abc

class Formatter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def toString(self, *args, **kwargs):
        pass

class FloatFormatter(Formatter):
    __metaclass__ = abc.ABCMeta
    def __init__(self, formula):
        self.formula = formula
    def toString(self, value):
        dst = ''
        try:
            value = float(value)
            dst = self.formula.format(value)
        except:
            dst = '{0}'.format(str(value))
        return dst

class StringFormatter(Formatter):
    __metaclass__ = abc.ABCMeta
    def __init__(self, formula):
        self.formula = formula
    def toString(self, value):
        return self.formula.format(value)

class PandasVisual(object):
    def __init__(self, df, title):
        self.title = title
        self.html = ""
        self.df = df
        self.label_color = ['#FFED97','#D3FF93','#B3D9D9']
        self.sec_label_color = ['#4CAF50','#938235','#f24f6a','#c8d32e','#c0d16e','#e0d2ef','#6ba377']
        self.header_bgd_color = ['#3ddb99','#66ba9c','#baa266','#4cb57d','#59b785','#c19c78','#3dbbdb','#2ba1bf','#c1ac78','#118ead','#66ba8d']
        self.category_bgd_color = ['#b54641','#bc56b9','#6575c6']
        self.default_format = StringFormatter('{0}')
    def setColumnFormat(self, columns):
        self.col_format = columns

    def isSingleIndex( self, index):
        return not isinstance( index, pd.MultiIndex)

    def to_html_for_ExtraRow(self, extra_rows, extra_row_format):
        extra_row_html = ""
        if extra_rows and len(extra_rows)>0:
            row_format = extra_row_format if extra_row_format else self.default_format
            for item in extra_rows:
                extra_row_html += """<th style="background-color: #841738;color: white;text-align: center;padding: 8px;">"""+str(item['HEADER'])+"</th>"
                for cell in item['DATA']:
                    format_value = cell if isinstance(cell,str) else row_format.format( cell)
                    extra_row_html += """<td style="text-align: left;padding: 8px;"><span style="color: red;font-weight:bold;">"""+ str(format_value)+"</span></td>"
                extra_row_html +="</tr>"
        return extra_row_html

    def to_html_for_SingleIndex(self, df, extra_rows, color_dict,extra_row_format):
        html_output = ""
        indexs = df.index
        columns = df.columns
        dataset = df.values
        header = df.index.names + list(df)
        header_html = ""
        if self.isSingleIndex( self.df.columns):
            header_html = "<tr>"
            for item in header:
                header_html += """<th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">"""+str(item)+"</th>"
            header_html += "</tr>"
        else:
            level_count = len(df.columns.levels)
            header_html = "<tr>"
            for item in df.index.names:
                header_html += """<th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;" rowspan="{0}">{1}</th>""".format( level_count, str(item))
            label_html = ""
            label_index_i = 0
            label_index_j = 0
            curr_index_count = 0
            first_line_label = df.columns.labels[label_index_i]
            label_count = len(df.columns.labels[label_index_i])
            while label_index_j < label_count:
                if (label_index_j+1<label_count) and first_line_label[label_index_j] == first_line_label[label_index_j+1]:
                    curr_index_count+=1
                else:
                    label_html +="""<th style="background-color: {2};color: black;text-align: center;padding: 8px;" colspan="{0}">{1}</th>""".format( curr_index_count+1, str(df.columns.levels[label_index_i][first_line_label[label_index_j]]), self.category_bgd_color[first_line_label[label_index_j]%3])
                    curr_index_count = 0
                label_index_j+=1
            header_html += label_html+"</tr>"
            label_index_i += 1
            while label_index_i<len(df.columns.labels):
                label_html = ""
                label_index_j = 0
                curr_index_count = 0
                line_label = df.columns.labels[label_index_i]
                label_count = len(line_label)
                while label_index_j < label_count:
                    if (label_index_j+1<label_count) and line_label[label_index_j] == line_label[label_index_j+1]:
                        curr_index_count+=1
                    else:
                        label_html +="""<th style="background-color: {2};color: black;text-align: center;padding: 8px;" colspan="{0}">{1}</th>""".format( curr_index_count+1, str(df.columns.levels[label_index_i][line_label[label_index_j]]), self.header_bgd_color[line_label[label_index_j]%11])
                        curr_index_count = 0
                    label_index_j+=1
                header_html += "<tr>"+label_html+"</tr>"
                label_index_i+=1
        body_html = ""
        for row_index in range(0, len(dataset) ):
            first_color_index = ""
            body_html += "<tr>" if row_index%2==0 else """<tr style="background-color: #f2f2f2">"""
            body_html +="""<th style="background-color: {0};color: blue;text-align: center;padding: 8px;">""".format( self.label_color[row_index%3])+"{0}".format(indexs[row_index]) +"</th>"
            first_color_index = indexs[row_index]
            for value_index in range(0, len(dataset[row_index]) ):
                formatter = self.col_format[value_index] if value_index in self.col_format else self.default_format
                format_value = formatter.toString(dataset[row_index][value_index])
                second_color_index = header[value_index+1]
                color_value = 'white'
                if color_dict and len(color_dict)>0:
                    color_value = color_dict[first_color_index+'*'+second_color_index] if first_color_index+'*'+second_color_index in color_dict else 'white'
                body_html +="""<td style="background-color: {0};text-align: left;padding: 8px;">""".format( color_value)+ str(format_value)+"</td>"
            body_html +="</tr>"
        extra_row_html=""
        if extra_rows and len(extra_rows)>0:
            extra_row_html = self.to_html_for_ExtraRow( extra_rows, extra_row_format)
        rtl_html = """<h2>{0}</h2><table border="1" style="border-collapse: collapse;width: 100%;">""".format( self.title)+header_html+body_html+extra_row_html+"</table>"
        return rtl_html

    def to_html_for_MultipleIndex(self, df, extra_rows, color_dict, extra_row_format):
        html_output = ""
        indexs = df.index
        columns = df.columns
        dataset = df.values
        label_dict = {}
        header = df.index.names + list(df)
        header_html = ""
        if self.isSingleIndex( self.df.columns):
            header_html = "<tr>"
            for item in header:
                header_html += """<th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;">"""+str(item)+"</th>"
            header_html += "</tr>"
        else:
            level_count = len(df.columns.levels)
            header_html = "<tr>"
            for item in df.index.names:
                header_html += """<th style="background-color: ORANGE;color: black;text-align: center;padding: 8px;" rowspan="{0}">{1}</th>""".format( level_count, str(item))
            label_html = ""
            label_index_i = 0
            label_index_j = 0
            curr_index_count = 0
            first_line_label = df.columns.labels[label_index_i]
            label_count = len(df.columns.labels[label_index_i])
            while label_index_j < label_count:
                if (label_index_j+1<label_count) and first_line_label[label_index_j] == first_line_label[label_index_j+1]:
                    curr_index_count+=1
                else:
                    label_html +="""<th style="background-color: {2};color: black;text-align: center;padding: 8px;" colspan="{0}">{1}</th>""".format( curr_index_count+1, str(df.columns.levels[label_index_i][first_line_label[label_index_j]]), self.category_bgd_color[first_line_label[label_index_j]%3])
                    curr_index_count = 0
                label_index_j+=1
            header_html += label_html+"</tr>"
            label_index_i += 1
            while label_index_i<len(df.columns.labels):
                label_html = ""
                curr_index_count = 0
                label_index_j = 0
                line_label = df.columns.labels[label_index_i]
                label_count = len(line_label)
                while label_index_j < label_count:
                    if (label_index_j+1<label_count) and line_label[label_index_j] == line_label[label_index_j+1]:
                        curr_index_count+=1
                    else:
                        label_html +="""<th style="background-color: {2};color: black;text-align: center;padding: 8px;" colspan="{0}">{1}</th>""".format( curr_index_count+1, str(df.columns.levels[label_index_i][line_label[label_index_j]]), self.header_bgd_color[line_label[label_index_j]%11])
                        curr_index_count = 0
                    label_index_j+=1
                header_html += "<tr>"+label_html+"</tr>"
                label_index_i+=1
        body_html = ""
        label_index_len = len(indexs.labels)
        header_pattern = re.compile(r'[0-9]{2}-[\w\s]+', re.I)
        for row_index in range(0, len(dataset) ):
            first_color_index = ""
            body_html += "<tr>" if row_index%2==0 else """<tr style="background-color: #f2f2f2">"""
            body_html +="""<th style="background-color: {0};color: blue;text-align: center;padding: 8px;">""".format( self.label_color[ indexs.labels[0][row_index]%3])+ "{0}".format( indexs.levels[0][indexs.labels[0][row_index]])+"</th>"
            first_color_index += indexs.levels[0][indexs.labels[0][row_index]]+"*"
            if label_index_len>1:
                for label_index in range(1, label_index_len):
                    index_label_value=indexs.levels[label_index][indexs.labels[label_index][row_index]]
                    if header_pattern.match( index_label_value):
                        index_label_value = index_label_value[3:]
                    body_html +="""<th style="background-color: {0};color: blue;text-align: center;padding: 8px;">""".format( self.sec_label_color[ hash(indexs.levels[1][indexs.labels[1][row_index]])%7])+ index_label_value+"</th>"
                    first_color_index += indexs.levels[label_index][indexs.labels[label_index][row_index]]+"*"
            for value_index in range(0, len(dataset[row_index]) ):
                formatter = self.col_format[value_index] if value_index in self.col_format else self.default_format
                format_value = formatter.toString(dataset[row_index][value_index])
                second_color_index = header[value_index+label_index_len]
                color_value = 'white'
                if color_dict and len(color_dict)>0:
                    color_value = color_dict[first_color_index+second_color_index] if first_color_index+second_color_index in color_dict else 'white'
                body_html +="""<td style="background-color: {0};text-align: left;padding: 8px;">""".format(color_value)+ str(format_value)+"</td>"
            body_html +="</tr>"
        extra_row_html=""
        if extra_rows and len(extra_rows)>0:
            extra_row_html = self.to_html_for_ExtraRow( extra_rows, extra_row_format)
        rtl_html = """<h2>{0}</h2><table border="1" style="border-collapse: collapse;width: 100%;">""".format( self.title)+header_html+body_html+extra_row_html+"</table>"
        return rtl_html

    def to_html( self, extra_rows=[], color_dict=None, extra_row_format='{:,.0f}'):
        if self.isSingleIndex( self.df.index):
            self.html = self.to_html_for_SingleIndex( self.df, extra_rows, color_dict,extra_row_format)
        else:
            self.html =self.to_html_for_MultipleIndex( self.df, extra_rows, color_dict,extra_row_format)
        return self.html


if __name__ == '__main__':
    raw_data = {'first_name': ['Tina', 'Jake', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', "Jacobson", 'Milner', 'Milner'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [423163, 245778, 31345234, 57978, 6234512],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
    df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
    pv = PandasVisual(df, 'Test Pandas Visual')
    pv.setColumnFormat( {0: StringFormatter('{0}'),1: StringFormatter('{0}'), 2: FloatFormatter('{:.2%}'), 3:FloatFormatter('{:,.0f}'), 4:FloatFormatter('{:.2%}'), 5:FloatFormatter('{:.2%}')} )
    with open('test_pandas_visual.html', 'wb') as file_object:
        file_object.write('')
    with open('test_pandas_visual.html', 'wb') as file_object:
        file_object.write(pv.to_html())