from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.merchant import Merchant
from models.tag import Tag
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