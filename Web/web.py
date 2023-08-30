csv = open('input.csv','r',encoding='utf-8')
file = csv.read()
row_list = [file


with open('html.html','wb') as html:
    string = '''<!DOCTYPE html>
<html>
<head>
<title>Rubik's Solving Contest</title>
</head>
<body>

<h1>Rubik's Solving Contest</h1>
<table>
'''
    for row in file:
        row_list = [r for r in row.split(',')]
        
        string += '''<tr>
        ''' 
        if 'STT' == row_list:
            for i in row_list:
                string += '''<th>''' + str(i) + '''</th>
                '''
        else: 
            for i in row_list:
                string += '''<td>''' + str(i) + '''</td>
                '''
        string += '''</tr>
        '''
    string += '''</body>
</html>'''

    html.write(string.encode('utf8'))