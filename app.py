from flask import Flask, render_template

import repositories.transaction_repository as transaction_repository
from controllers.transactions_controller import transactions_blueprint



app = Flask(__name__)

app.register_blueprint(transactions_blueprint)
# app.register_blueprint(cities_blueprint)
# app.register_blueprint(sights_blueprint)




@app.route("/")
def home():
   transactions = transaction_repository.select_all()
   return render_template(
        "index.html", title="Home", transactions = transactions
    )

if __name__ == "__main__":
    app.run(debug=True)