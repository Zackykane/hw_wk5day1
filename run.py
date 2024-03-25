from flask import Flask, request
app = Flask(__name__)
cars = {
    1:{
        'id' : 1,
        'model' : 'Toyota',
        'make' : 'Corolla'
    },
    2 : {
        'id' : 2,
        'model' : 'Toyota',
        'make' : 'Camry'
    }
}
sale_receipts = {
    1 : {
        'car' : 2,
        'Condition' : 'New',
        'Color' : 'Black'
    },
    2 : {
        'car' : 1,
        'Condition' : 'New',
        'Color' : 'Red'
    }
}
@app.route('/')
def land():
    return {
        "Welcome to our Toyota dealership!!!!" : "Please hurry up and buy something!"
    }
@app.route('/cars')
def get_cars():
    return {
        'cars' : list(cars.values())
    }
@app.route('/car/<int:id>')
def get_ind_car(id):
    if id in cars:
        return {
            'car' : cars[id]
        }
    return {
        'UH OH, something went wrong' : "invalid car id"
    }

@app.route('/car', methods=["POST"])
def create_car():
    data = request.get_json()
    print(data)
    cars[data['id']] = data
    return {
        'car created successfully': cars[data['id']]
    }

@app.route('/car', methods=["PUT"])
def update_car():
    data = request.get_json()
    if data['id'] in cars:
        cars[data['id']] = data
        return {
            'car updated' : cars[data['id']]
        }
    return {
        'err' : 'no car found with that id'
    }
    
@app.route('/car', methods=["DELETE"])
def del_car():
    data = request.get_json()
    if data['id'] in cars:
        del cars[data['id']]
        return {
            'car gone': f"{data['car']} is no more. . . "
        }
    return {
        'err' : "can't delete that car they aren't there. . . "
    }