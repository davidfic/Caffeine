from flask import Flask
from flask.ext.debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.update(
    DEBUG_TB_ENABLED=True,
    SECRET_KEY="BLAH"

    )
# app = Flask('Caffeine')
from app import views

# def debug():
# 	assert current_app.debug == False
toolbar = DebugToolbarExtension(app)
def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)


app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string