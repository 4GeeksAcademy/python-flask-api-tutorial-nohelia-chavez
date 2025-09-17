from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])

def get_todos():
  return jsonify(todos)



@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/todos', methods=['GET'])
def hello_todos():
    return "<h1>Hello!</h1>"


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)

    todos.append(request_body)     # agrega la nueva tarea enviada a la lista global (todos)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        todos.pop(position)  
    except IndexError:
        return jsonify({"msg": "La posición no existe"}), 404
    
    return jsonify(todos)




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)