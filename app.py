from flask import Flask, render_template

import repositories.transaction_repository as transaction_repository
from controllers.transactions_controller import transactions_blueprint
from controllers.merchants_controller import merchants_blueprint
from controllers.tags_controller import tags_blueprint


app = Flask(__name__)

app.register_blueprint(transactions_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(tags_blueprint)




@app.route("/")
def home():
   transactions = transaction_repository.select_all()
   transactions.sort(key=lambda r: r.timestamp)
   total_cost = transaction_repository.get_total_cost()
   return render_template(
        "index.html", title="Home", transactions = transactions, total_cost = total_cost
    )

if __name__ == "__main__":
    app.run(debug=True)