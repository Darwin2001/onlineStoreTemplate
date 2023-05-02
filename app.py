#!/usr/bin/env python3

from authentication.authTools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, render_template, request, redirect, url_for
from core.session import Sessions

app = Flask(__name__)
HOST, PORT = 'localhost', 8080
global username, products, db, sessions
username = 'default'
db = Database('database/storeRecords.db')
products = db.get_full_inventory()
sessions = Sessions()
sessions.add_new_session(username, db)
sales = db.get_full_sales_information()


@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    # print(products)
    return render_template('index.html', username=username, products=products, sessions=sessions)

@app.route('/thanks')
def thanks_page():
    """
    This page turns to a webpage that thanks the user for filling form and returns them to homepage.
    Created by Darwin Peraza 
    """

    return render_template("thanks.html")


@app.route('/contactUs')
def contact_page():
    """""
    Created by Darwin Peraza, This renders the contact us page 

    args:
        - None
    
    returns: 
        - None
    """
    return render_template('contactUs.html')

@app.route("/contactUs" , methods=['POST'])
def contact_send():
    email = request.form["email"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    problem_type = request.form["problem_type"]
    description = request.form["description"]

    db.insert_new_troubleshoot(email,first_name,last_name,problem_type,description)

    return redirect(url_for("thanks_page"))


@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('login.html')


# Route to logout user
@app.route('/logout')
def logout():
    """
    Removes the session using username to logout the user

    args:
        - None

    returns:
        - None
    
    modifies:
        - sessions: removes a previous session from the sessions object
    """
    sessions.remove_session(username)
    return redirect(url_for('index_page'))

@app.route('/home', methods=['POST'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object

    """
    username = request.form['username']
    password = request.form['password']
    if login_pipeline(username, password):
        sessions.add_new_session(username, db)
        # Added username to be send to the home.html - Monish
        return render_template('home.html', products=products, sessions=sessions, username=username)
    else:
        print(f"Incorrect username ({username}) or password ({password}).")
        return render_template('index.html')



@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/storeRecords.db: adds a new user to the database
    """
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    db.insert_user(username, key, email, first_name, last_name)
    # MSR - changed the render template to redirect to login 
    return  redirect(url_for('login_page'))


@app.route('/checkout')
def checkout_page():
    return render_template('checkout.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    """
    order = {}
    itemss = {}
    user_session = sessions.get_session(username)
    for item in products:
        # print(f"item ID: {item['id']}")
        if request.form[str(item['id'])] > '0':
            count = request.form[str(item['id'])]
            order[item['item_name']] = count
            user_session.add_new_item(
                item['id'], item['item_name'], item['price'], count)
    items = user_session.submit_cart()
    # sales = db.get_full_sales_information()
    return render_template('checkout.html', order=order, sessions=sessions, total_cost=user_session.total_cost, items=items)

@app.route('/admin',methods=["POST", "GET"])
def adminLogin():
      
      """

        This method checks for admin credentials, created by Darwin Peraza 


      """
      username = request.form['username-admin']
      password = request.form['password-admin']
      admins = db.admin_check()
      converted_admins = get_values(admins,"username")
      troubleshoot = db.get_all_troubleshoot()
      
      if(login_pipeline(username,password) and username in converted_admins):
        return render_template("admin.html", username=username, troubleshoot=troubleshoot)
      else:
        return redirect(url_for("login_page"))
          

def get_values(lst, key):

    """

    This method takes values from key value pairs and translates them into a list
    
    """
    result = []
    for dictionary in lst:
        if key in dictionary:
            result.append(dictionary[key])
    return result





if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
