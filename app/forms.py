from wtforms import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
    open_id = TextField('openid', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)

