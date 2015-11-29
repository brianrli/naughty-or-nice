from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class UserForm(Form):
	email = TextField('email', validators = [Required()])

class EditUserForm(Form):
	name = TextField('name',validators = [Required()])
	email = TextField('email',validators = [Required()])