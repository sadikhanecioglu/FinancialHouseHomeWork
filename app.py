from flask import Flask
from flasgger import Swagger
from api.route.user import user_api
from web.account.views import account_views
from flask_bootstrap import Bootstrap5
from flask_datepicker import datepicker



def init_application():
    app = Flask(__name__)
    
    app.config['SWAGGER'] = {'title':'FinancalHouse HomeWork'}
    app.config.update(dict(
    SECRET_KEY="FinanceHouse*!2019.2",
    WTF_CSRF_SECRET_KEY="CsrfFinanceHouse*!2019.2"
    ))
    swagger = Swagger(app)
    app.register_blueprint(user_api, url_prefix='/api')
    app.register_blueprint(account_views,url_prefix='/')
    return app


if __name__ == '__main__':
    app = init_application()
    Bootstrap5(app)
    datepicker(app)
    app.run(host='0.0.0.0',debug=True)    