import json

json_object = {}

def addto_style(key, value):
    json_object = read_style()
    json_object[key] = value
    write_style(json_object)

def read_style():
    with open('styles/stylesheets.json', 'r') as readfile:
        obj = json.loads(readfile.read())
    return obj

def write_style(obj):
    with open('styles/stylesheets.json', 'w') as writefile:
        writefile.write(json.dumps(obj, indent=2))

stylesheet = '''
        image: url(:/images/resources/stop.png);
        background-color: #2b2d2e;
        border-radius: 18px;
'''

addto_style('stop_style', stylesheet)