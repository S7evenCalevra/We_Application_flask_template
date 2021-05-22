# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user,logout_user
from io import BytesIO
from flask import Flask, render_template, request, send_file
from jinja2 import TemplateNotFound
from werkzeug.exceptions import abort
from . import Utils

#export STRIPE_PUBLISHABLE_KEY=pk_test_51IrSvtHNAU2EmjRhgART7p3mj5ooGKxGYpuIMuFnM76i5wYE8RW3BGRoZokSK2xZUsQQdBC7J0EkJl9as7kauf6K00Fp4ZwNy7

#export STRIPE_SECRET_KEY=sk_test_51IrSvtHNAU2EmjRhpPm7mqNrOvIQDUO9ql3qN7Rx7T7gl8zvXQjljwq55xpCxGGGzAO4rk971tdbroQe0IXqqsdU009liUP8sq

#export STRIPE_PRICE_ID=price_1IrU12HNAU2EmjRhUJRiKvc7
main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/download')
@login_required
def download_file():
	path = "test_files/sample.pdf"
	#path = "info.xlsx"
	#path = "simple.docx"
	#path = "sample.txt"
	return send_file(path, as_attachment=True)





#@main.route("/account/delete", methods=["POST"])
#@login_required
#def delete_account():
#    env = Utils.environment()
#
#    stripe.api_key = env["billing"]["stripe"]["token"]
#    for subscription in stripe.Subscription.list(customer=current_user.stripe_customer_id):
#        if subscription.customer == current_user.stripe_customer_id:
#            subscription.delete()

#    db.session.delete(current_user)
#    db.session.commit()

#    logout_user()
#    return redirect("/")


