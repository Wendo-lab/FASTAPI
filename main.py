from flask import Flask,render_template,request,redirect
import requests

app = Flask(__name__)


base_url = "http://localhost:8000"
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form["fname"]
        last_name = request.form["lname"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]
        payload = {"First_name": first_name, "Last_name": last_name, "email_address": email, "phone_number": phone, "password": password,"is_verified":"False"}
        r = requests.post((base_url + "/createCustomer"), json=payload)
        response = r.json()
        print(response)
        return redirect("/signup")

    else:
        return render_template("signup.html")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        payload = {"email_address": email, "password": password}
        r = requests.post((base_url + "/login/customer"), json=payload)
        response = r.json()
        print(response)
        return redirect("/login")
    else:
        return render_template("login.html")
        
@app.route("/types", methods=["GET", "POST"])
def mealtypes():
    if request.method == "POST":
        name = request.form["name"]
        payload = {"name": name}
        r = requests.post((base_url + "/createType"), json=payload)
        response = r.json()
        print(response)
        return redirect("/types")
    else:
        r = requests.get((base_url + "/type"))
        response = r.json()
        print(response)
        return render_template("types.html", types=response)
    
@app.route ("/editType", methods=[ "POST"])
def editType():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        payload = { "name": name}
        print (payload)
        r = requests.put((base_url + "/updatetype/" + id), json=payload)
        print(r.json())
        return redirect("/types")
    else:
        return render_template("types.html")


@app.route('/menu', methods=["GET", "POST"])
def menu():
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        availability = request.form['availability']
        users_id = request.form['user_id']
        types_id = request.form['type_id']
        payload = {"name": name, "description": description, "price": price, "availabilty_status":availability, "user_id":users_id, "type_id":types_id}
        r = requests.post((base_url + "/createMneu"), json=payload)
        response = r.json()
        print(response)
        return redirect("/menu")
    else:
        r = requests.get((base_url + "/menu"))
        response = r.json()
        print(response)
        return render_template("menu.html", menu=response)


@app.route("/user", methods=["GET", "POST"])
def user():
    if request.method == "POST":
        f_name = request.form["f_name"]
        l_name = request.form["l_name"]
        email = request.form['email']
        location = request.form['location']
        password = request.form['password']
        image = request.form['image']
        payload = {"first_name": f_name, "last_name": l_name, "email": email, "location": location, "password": password, "Image": image}
        r = requests.post((base_url + "/createUser"), json=payload)
        response = r.json()
        print(response)
        return redirect("/user")
    else:
        r = requests.get((base_url + "/users"))
        response = r.json()
        print(response)
        return render_template("user.html", user=response)


@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        description = request.form['description']
        quantity = request.form['quantity']
        delivery_address = request.form['delivery_address']
        additional_cost = request.form['additional_cost']
        order_status = request.form['order_status']
        menu_id = request.form['menu_id']
        payload = {"description": description, "quantity": quantity, "delivery_address": delivery_address, "additional_cost": additional_cost, "order_status": order_status, "menu_id": menu_id}
        r = requests.post((base_url + "/createOrder"), json=payload)
        response = r.json()
        print(response)
        return redirect("/order")
    else:
        return render_template("order.html")
app.run()



        
