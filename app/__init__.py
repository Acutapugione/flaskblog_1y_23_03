from flask import Flask
from db import up 

app = Flask(__name__)


from . import routes