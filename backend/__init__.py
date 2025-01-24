from flask import Flask

app = Flask(__name__, template_folder='../templates', static_folder='../static')

from backend import routes  # Import routes after app initialization