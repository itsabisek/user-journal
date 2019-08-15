from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from user_journal.models import User, Journal
from user_journal import bcrypt


class RegForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], id="regName")
    reg_username = StringField('Username', validators=[Length(min=2, max=16), DataRequired()], id="regUsername")
    reg_password = PasswordField('Password', validators=[Length(min=6), DataRequired()], id="regPassword")
    submit = SubmitField('Register')

    def validate_input(self, username):
        user = User.query.filter_by(username=username).first()
        if not user:
            return True
        return False


class LoginForm(FlaskForm):
    login_username = StringField('Username', validators=[DataRequired()],  _name='loginUsername',id="loginUsername")
    login_password = PasswordField('Password', validators=[DataRequired()],  _name='loginPassword',id="loginPassword")
    submit = SubmitField('Log In')
