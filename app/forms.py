from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class StringForm(Form): 
	textinput = StringField('textinput', validators=[DataRequired()], render_kw={"placeholder": "Write some text here"})