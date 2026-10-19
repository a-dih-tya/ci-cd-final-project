
from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

Talisman(
    app,
    force_https=False,
    content_security_policy=None
)
