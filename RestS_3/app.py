from flask import Flask,jsonify,request,render_template

app=Flask(__name__)
stores=[
    {
        'name':'Amazon',
         'items':[
             {
                 'name':'bat',
                 'price':'1000',
             }
         ]
    }
]
@app.route("/")
def func():
    return render_template("index.html")
@app.route("/store")
def func1():
    return jsonify({'store':stores})
@app.route("/store/<string:name>")
def func2(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message':'Name not found'})
@app.route("/store/<string:name>/item")
def func3(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'name not found'})
@app.route("/store",methods=["POST"])
def func4():
    return_data=request.get_json()
    new_store={
        'name':return_data["name"],
        'item':[]
    }
    stores.append(new_store)
    return jsonify(new_store)
@app.route("/store/<string:name>/item",methods=["POST"])
def func5(name):
    return_data=request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={
                "name":return_data["name"],
                "price":return_data["price"]
            }
            store   ['item'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'name is not present'})

if __name__=="__main__":
    app.run(debug=True)