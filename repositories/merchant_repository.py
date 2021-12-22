from pdb import run
from db.run_sql import run_sql

from models.merchant import Merchant

#CREATE
def save(merchant):
    sql="INSERT INTO merchants (name, active) VALUES (%s, %s) RETURNING *"
    values = [merchant.name, merchant.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

#SELECT ALL
def select_all():
    merchants = []
    sql= "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row['name'], row['active'], row['id'])
        merchants.append(merchant)
    return merchants

#SELECT BY ID
def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['active'], result['id'])
    return merchant

#DELETE ALL
def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)