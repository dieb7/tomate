from flask import Flask


app = Flask(__name__)


# to avoid circular dependency issue with flask imports
from app import routes
