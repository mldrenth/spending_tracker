from pdb import run
from db.run_sql import run_sql

from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

#CREATE
def save(transaction):
    sql="INSERT INTO transactions (name, price, merchant_id, tag_id, timestamp) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [transaction.name, transaction.price, transaction.merchant.id, transaction.tag.id, transaction.timestamp]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

#SELECT ALL
def select_all():
    transactions = []
    sql= "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        tag = tag_repository.select(row['tag_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['name'], row['price'], merchant, tag, row['timestamp'], row['id'])
        transactions.append(transaction)
    return transactions

#SELECT BY ID
def select(id):
    transaction = None
    sql= "SELECT * FROM transactions WHERE id = %s "
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = merchant_repository.select(result['merchant_id'])
        tag = tag_repository.select(result['tag_id'])
        transaction = Transaction(result['name'], result['price'], merchant, tag, result['timestamp'], result['id'])
    return transaction


#UPDATE
def update(transaction):
    sql = "UPDATE transactions SET (name, price, merchant_id, tag_id, timestamp) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = (transaction.name, transaction.price, transaction.merchant.id, transaction.tag.id, transaction.timestamp, transaction.id)
    run_sql(sql, values)

#DELETE ALL
def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

#DELETE BY ID
def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)