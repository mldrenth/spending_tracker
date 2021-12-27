from flask import Flask, render_template, redirect, request
from flask import Blueprint
from datetime import datetime
from models.merchant import Merchant
from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

transactions_blueprint = Blueprint("transactions", __name__)

#NEW
#GET 'transactions/new
@transactions_blueprint.route("/transaction/new")
def new_transaction():
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template('transaction/new.html', title = "Create New Transaction", tags = tags, merchants = merchants)

#POST 
@transactions_blueprint.route("/", methods=['POST'])
def create_transaction():
    name = request.form['name']
    price = request.form['price']
    merchant_id = request.form['merchant_id']
    tag_id = request.form['tag_id']
    timestamp = datetime.fromisoformat(request.form['timestamp'])
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    transaction = Transaction(name, price, merchant, tag, timestamp)
    transaction_repository.save(transaction)
    return redirect('/')

#EDIT
@transactions_blueprint.route("/transactions/<id>/edit")
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    timestamp = transaction.timestamp.isoformat()
    return render_template('transaction/edit.html', title = "Edit Transaction", transaction = transaction, merchants = merchants, tags = tags, timestamp = timestamp)

#UPDATE
@transactions_blueprint.route("/transactions/<id>", methods =['POST'])
def update_transaction(id):
    name = request.form['name']
    price = request.form['price']
    merchant_id = request.form['merchant_id']
    tag_id = request.form['tag_id']
    timestamp = datetime.fromisoformat(request.form['timestamp'])
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    transaction = Transaction(name, price, merchant, tag, timestamp,id)
    transaction_repository.update(transaction)
    return redirect('/')

#DELETE
@transactions_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/')