from flask import Flask, jsonify, request, abort


app = Flask(__name__)

app.testing = True

users = [
    {
        'id': 1,
        'firstname': 'dennis',
        'lastname': 'lubega',
        'email': 'lubega@gmail.com',
        'password': '12345',
    },
    {
        'id': 2,
        'firstname': 'atlas',
        'lastname': 'Tegz',
        'email': 'atlas@gmail.com',
        'password': '12345',
    }
]

meals = [
    {
        'id': 1,
        'mealname': "ricebeans",
        'price': 3000,
        'type1': "lunch"
    },
    {
        'id': 2,
        'mealname': 'rolex',
        'price': 4000,
        'type1': 'lunch'
    }
]

# Need add date to this
transactions = [
    {
        'id': 1,
        'mealname': "ricebeans",
        'price': 3000,
        'user_id': 1
    },
    {
        'id': 2,
        'mealname': "lasagna",
        'price': 10000,
        'user_id': 2
    },
    {
        'id': 3,
        'mealname': 'rolex',
        'price': 4000,
        'user_id' : 1
    }
]

menuDay = [
    {
        'id': 1,
        'mealname': "ricebeans",
        'price': 3000,
        'type1': "lunch"
    },
    {
        'id': 2,
        'mealname': "lasagna",
        'price': 10000,
        'type1': "breakfast"
    },
    {
        'id': 3,
        'mealname': "Rice and Matooke",
        'price': 10000,
        'type1': "lunch"
    },
    {
        'id': 4,
        'mealname': 'rolex',
        'price': 4000,
        'type1' : "lunch"
    }
]



# Registering a User
@app.route('/bookmealapi/v1.0/auth/signup', methods=['POST'])
def signUp():
    if not request.json or 'fname' not in request.json or 'lname' not in request.json or 'email' not in request.json or 'password' not in request.json or 'cnfmpassword' not in request.json:
        abort(400)

    user_id = users[-1].get("id") + 1
    firstname = request.json.get('fname')  
    lastname = request.json.get('lname') 
    email = request.json.get('email') 
    password = request.json.get('password') 
    cnfmpassword = request.json.get('cnfmpassword')

    if password != cnfmpassword:
        abort(400)

    for user in users:
        if  user["email"] == email:
            abort(400)  

    user = {
        'id': user_id,
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'password': password,
    } 


    users.append(user)
    return jsonify({'user': user, 'users': users}), 201  

# Login
@app.route('/bookmealapi/v1.0/auth/login', methods=['POST'])
def loginIn():   
    if not request.json or 'email' not in request.json or 'password' not in request.json:
        abort(400)

    email = request.json.get('email')    
    password = request.json.get('password')

    for user in users:
        if user['email'] ==  email and user['password'] ==  password:
            return jsonify({'message': "Successfully login"}), 200   
        else:
            return jsonify({'message': "User Not Found", 'users': users}), 400  


# Add Meal
@app.route('/bookmealapi/v1.0/meals', methods=['POST'])
def addMeal():
    if not request.json or 'mealname' not in request.json or 'price' not in request.json or 'type1' not in request.json:
        abort(400)

    mealname = request.json.get('mealname')
    price = request.json.get('price')
    type1 = request.json.get('type1')

    meal_id = meals[-1].get('id') + 1

    if type(price) is not int:
        abort(400)

    for meal in meals:
        if meal['mealname'] == mealname:
           abort(400)    
    
    meal = {
        'id': meal_id,
        'mealname': mealname,
        'price': price,
        'type1': type1
    }

    meals.append(meal)
    return jsonify({'meal': meal}), 201

# Select Meal
@app.route('/bookmealapi/v1.0/orders', methods=['POST'])
def selectMeal():
    if not request.json or 'mealname' not in request.json or 'price' not in request.json or 'userId' not in request.json:
       abort(400)
    mealname = request.json.get('mealname')
    price = request.json.get('price')
    user_id = request.json.get('userId')

    if type(price) is not int and type(user_id) is not int:
       abort(400)

    transactionId = transactions[-1].get('id') + 1   

    transaction = {
       'id': transactionId,
       'mealname': mealname,
       'price': price,
       'user_id' : user_id
    }   
    transactions.append(transaction)
    return jsonify({'transaction': transaction}), 201


# set Meal Options
@app.route('/bookmealapi/v1.0/menu', methods=['POST'])
def setMenu():
    if not request.json:
        abort(400)
    mealname = request.json.get('mealname')
    price = request.json.get('price') 
    type1 = request.json.get('type1')  

    meal ={
       "mealname":mealname,
       "price":price,
       "type1":type1
    }
    menuDay.append(meal)
    return jsonify({'menuDay': menuDay}), 201

  

  # update Meal Option
@app.route('/bookmealapi/v1.0/meals/<mealId>', methods=['PUT'])
def updateMealOption(mealId):
    if not request.json or 'mealname' not in request.json or 'type1' not in request.json:
        abort(400)
    mealname = request.json.get('mealname')
    price = request.json.get('price')
    type1 = request.json.get('type1')

    if type(price) is not int:
        abort(400)

    for meal in meals:
        if meal['id'] == int(mealId):
            meal['mealname'] = mealname
            meal['price'] = price
            meal['type1'] = type1
            return jsonify({'meal': meal}), 201 
    abort(404) 

# Modify Order
@app.route('/bookmealapi/v1.0/orders/<orderId>', methods=['PUT'])
def updateOrder(orderId):
    if not request.json or 'mealname' not in request.json or 'price' not in request.json:
        abort(400)

    mealname = request.json.get('mealname')
    price = request.json.get('price')

    if type(price) is not int:
        abort(400)

    for transaction in transactions:
        if transaction['id'] == int(orderId):
            transaction['mealname'] = mealname
            transaction['price'] = price
            return jsonify({'transaction': transaction}), 201 
    abort(404)   

# delete Meal Option
@app.route('/bookmealapi/v1.0/meals/<mealId>', methods=['DELETE'])
def deleteMealOption(mealId):
    for meal in meals:
        if meal['id'] == int(mealId):
            meals.remove(meal)
            return jsonify({'Meals': meals}), 204
    return jsonify({'id': '' + mealId}), 404
            



 # get all meals
@app.route('/bookmealapi/v1.0/meals', methods=['GET'])
def getAllMeals():
    return jsonify({'meals': meals}), 200

  # get all orders
@app.route('/bookmealapi/v1.0/orders', methods=['GET'])
def getAllOrders():  
    return jsonify({'transactions': transactions}), 200 

# get menu of the day
@app.route('/bookmealapi/v1.0/menu', methods=['GET'])
def getMenu():  
    return jsonify({'menuDay': menuDay}), 200    






  

        
