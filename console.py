import pdb
from datetime import datetime
from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
tag_repository.delete_all()
merchant_repository.delete_all()

tag_groceries = Tag("Groceries")
tag_repository.save(tag_groceries)

merchant_asda = Merchant("ASDA")
merchant_repository.save(merchant_asda)

date = datetime(2020,12,4,13,4,20)
transaction_1 = Transaction("Groceries 1", 55.42, merchant_asda, tag_groceries, date)
transaction_repository.save(transaction_1)