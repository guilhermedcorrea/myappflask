from flask_wtf import FlaskForm
from wtforms.fields import PasswordField,StringField,SubmitField,SelectField

from models.model import Produtos,Seller


class LoginForm(FlaskForm):
    usuario = StringField("Usuario")
    email = StringField("email")
    senha = PasswordField("Senha")
    submit = SubmitField("Entrar")








   
 


       



