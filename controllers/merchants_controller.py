from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

#New
#Get 
@merchants_blueprint.route("/merchants/new")
def new_merchant():
    return render_template('merchants/new.html', title = "Create New Merchant")

#POST
@merchants_blueprint.route("/merchants", methods=['POST'])
def create_merchants():
    name = request.form["name"]
    active = "active" in request.form.keys()
    merchant = Merchant(name, active)
    merchant_repository.save(merchant)
    return redirect('/')

@merchants_blueprint.route("/merchants/<id>/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', title = "Edit Merchant", merchant = merchant)

@merchants_blueprint.route("/merchants/<id>", methods = ["POST"])
def update_merchant(id):
    name = request.form['name']
    active = "active" in request.form.keys()
    merchant = Merchant(name, active, id)
    merchant_repository.update(merchant)
    return redirect('/')