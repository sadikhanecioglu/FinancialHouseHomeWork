from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from web.account.forms import LoginForm
from flask import make_response
from core.apirequest import ApiRequest
from datetime import datetime,timedelta

account_views = Blueprint('account', __name__)




@account_views.route('/', methods=['GET', 'POST'])
def dashboard():
    if request.cookies['JWT']:
        return render_template("account/dashboard.html",jwt=request.cookies['JWT'])
    else:
        return redirect(url_for('account.login'))




@account_views.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if login_form.validate_on_submit():
        print(login_form.user)
        redirect_url = request.args.get(
            "next") or url_for("account.transcations")
        res = redirect(redirect_url)
        res.set_cookie("JWT", login_form.user['token'])
        return res
    else:
        return render_template("account/login.html", form=login_form)


@account_views.route('/transcations', methods=['GET', 'POST'])
def transcations():
    print(request.form)
    fromDate = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
    toDate =  datetime.today()
    if  'startDate' in request.form:
        fromDate = request.form['startDate']
    if 'toDate' in request.form:
        toDate = request.form['endDate']

    print(fromDate,toDate)        
    if request.cookies['JWT']:
        result = ApiRequest({'token': request.cookies['JWT']}).post("/api/v3/transaction/list", {"fromDate": fromDate,
                                                                                                 "toDate": toDate,
                                                                                                 "merchant": 1,
                                                                                                 "acquirer": 1,

                                                                                                 })
        if result.status_code == 401:
            return redirect(url_for('account.login'))
        print(result)
        if result.status_code == 200:
            data = result.json()
            print(data)
            return render_template("account/transcations.html", transcations=data)
        else:
            return render_template("account/transcations.html", error="Error")
    else:
        return redirect(url_for('account.login'))


@account_views.route('/transcations/<transcation_id>', methods=['GET', 'POST'])
def transcations_detail(transcation_id):
    print(transcation_id)
    if request.cookies['JWT']:
        result = ApiRequest({'token': request.cookies['JWT']}).post(
            "/api/v3/transaction", {"transactionId": transcation_id})
        if result.status_code == 401 or result.status_code == 403:
            return redirect(url_for('account.login'))
        print(result)
        if result.status_code == 200:
            data = result.json()
            print(data)
            return render_template("account/transcations.html", transcationdetail=data)
        else:
            return render_template("account/transcations.html", error="Error")
    else:
        return redirect(url_for('account.login'))
    
@account_views.route('/client/<transcation_id>', methods=['GET', 'POST'])
def transcations_client(transcation_id):
    print(transcation_id)
    if request.cookies['JWT']:
        result = ApiRequest({'token': request.cookies['JWT']}).post(
            "/api/v3/client", {"transactionId": transcation_id})
        if result.status_code == 401:
            return redirect(url_for('account.login'))
        print(result)
        if result.status_code == 200:
            data = result.json()
            print(data)
            return render_template("account/transcations_client.html", transcationdetail=data)
        else:
            return render_template("account/transcations_client.html", error="Error")
    else:
        return redirect(url_for('account.login'))    
