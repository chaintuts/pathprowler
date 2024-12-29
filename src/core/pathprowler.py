# This file contains code for a path traversal vulnerability
# The mock app transforms data from threat database CSVs to HTML tables
#
# Author: Josh McIntyre
#
import flask
from flask import request
import jinja2
import json

# App constants
APP_NAME = "pathprowler"
ROUTE_THREAT_DATABASE = "/threatdata"

RES_DIR="res/"
TEMPLATE_DIR="templates/"

DATA_MALWARE_DATABASE = "malwaredatabase.csv"
DATA_VULNERABILITY_DATABASE = "vulndatabase.json"
TEMPLATE_THREAT_DATABASE = "threat_template.html"

ERR_MSG = "No threat database found with that filename"

EXT_CSV = ".csv"
EXT_JSON = ".json"

# Create the main application
app = flask.Flask(APP_NAME)

def render_data(datafile, template):

    # Init
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

    # Generate
    template = environment.get_template(template)
    
    try:
        path = f"{RES_DIR}{datafile}"
        
        if path.endswith(EXT_CSV):
            with open(path) as f:
                data = f.readlines()
        elif path.endswith(EXT_JSON):
            with open(path) as f:
                data = json.load(f)
        else:
            with open(path) as f:
                data = f.readlines()

        template_html = template.render(filename=datafile, threats=data)
    except FileNotFoundError:
        return ERR_MSG

    return template_html
        
# Define application routes
@app.route(ROUTE_THREAT_DATABASE)
def threat_database():
    
    filename = request.args.get("filename")
    if not filename:
        filename = DATA_MALWARE_DATABASE

    return render_data(filename, TEMPLATE_THREAT_DATABASE)
    
