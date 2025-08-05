from flask import *
from bank import customer,account
app=Flask(__name__)
accounts={}
@app.route("/")
def home():
    return render_template("Index.html")
@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        contact = request.form["contact"]
        initial_deposit = float(request.form["Initial_deposit"])

        acc_number = len(accounts) + 1
        Customer_obj= customer(name, address, contact)
        Account_obj= account(acc_number, Customer_obj)
        Account_obj.deposit(initial_deposit)
        Account_obj.transactions.append(f"Account opened with: {initial_deposit}")
        accounts[acc_number] = Account_obj

        return f"Account Created Successfully! Your account no. is {acc_number}"
    return render_template("create.html")
if __name__=="__main__":
    app.run(debug=True)