from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/', methods=['GET'])
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/todos', methods=['POST'])
def add_new_todo():
    todos.append(request.json)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[position]
    return jsonify(todos)







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)