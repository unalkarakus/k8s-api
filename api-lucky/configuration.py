import json
import os
path = os.environ.get('CONFIG_PATH')

if path is None or path == "":
    path = "config.json"
    
with open(path, 'r') as f:
    config = json.load(f)