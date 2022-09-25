from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email,Length
from core.apirequest import ApiRequest
class LoginForm(FlaskForm):
    email = StringField("E-mail",validators=[DataRequired(),Email(),Length(min=5,max=100)])
    password = PasswordField("Password",validators=[DataRequired(),Length(min=4,max=50)])
    
    def __init__(self, formdata=..., **kwargs):
        super(LoginForm,self).__init__(formdata, **kwargs)
        self.user = None
        
    def validate(self):
        iv =  super(LoginForm,self).validate()
        if not iv:
            return False
        
        result = ApiRequest().post("/api/v3/merchant/user/login",{"email":self.email.data,"password":self.password.data})
        if result.status_code == 200:
            resultData = result.json()
            self.user = {}
            self.user['is_active'] = resultData['status'] == "APPROVED"
            self.user['token'] = resultData['token']
            self.user['email'] = self.email.data
            return True
        else:
            self.email.errors.append("Invalid Username or Password")
            return False
        
        